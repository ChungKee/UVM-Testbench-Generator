module TwoFlipFlopSynchronizer #
(
    parameter Width = 3
)
(
    input  clk, reset,
    input  [Width:0] DataIn,
    output reg [Width:0] DataOut
);
    reg [Width:0]temp;
    always @(posedge clk or negedge reset) begin
        if(!reset)begin
            temp <= 0;
            DataOut <= 0;
        end
        else begin
            temp <= DataIn;
            DataOut <= temp;
        end
    end
endmodule

module WritePointerHandle #
(
    parameter  PtrWidth = 3
)
(
    Wclk, Wresetn, Push, SynGrayReadPtr, GrayWritePtr, WritePtr, full
);
    input Wclk, Wresetn, Push;
    input [PtrWidth : 0] SynGrayReadPtr;
    
    output reg [PtrWidth : 0] GrayWritePtr, WritePtr;
    output reg full;

    wire [PtrWidth : 0] NextGrayWritePtr, NextWritePtr;
    
    assign NextWritePtr = WritePtr + (Push & !full); 
    assign NextGrayWritePtr = (NextWritePtr >> 1) ^ NextWritePtr;

    always @(posedge Wclk or negedge Wresetn) begin
        if(!Wresetn)begin
            WritePtr <= 0;
            GrayWritePtr <= 0;
        end
        else begin
            WritePtr <= NextWritePtr;
            GrayWritePtr <= NextGrayWritePtr;
        end
    end

    always @(posedge Wclk or negedge Wresetn) begin
        
        if (!Wresetn) begin
            full <= 1'b0;
        end 
        else begin
            full <= (NextGrayWritePtr == {~SynGrayReadPtr[PtrWidth : PtrWidth-1], SynGrayReadPtr[PtrWidth - 2 : 0]});
        end    
    end

endmodule

module ReadPointerHandle #
(
    parameter  PtrWidth = 3
)
(
    Rclk, Rresetn, Pop, SynGrayWritePtr, GrayReadPtr, ReadPtr, empty
);
    input Rclk, Rresetn, Pop;
    input [PtrWidth : 0] SynGrayWritePtr;
    
    output reg [PtrWidth : 0] GrayReadPtr, ReadPtr;
    output reg empty;
    
    wire [PtrWidth : 0] NextGrayReadPtr, NextReadPtr;
    
    assign NextReadPtr = ReadPtr + (Pop & !empty); 
    assign NextGrayReadPtr = (NextReadPtr >> 1) ^ NextReadPtr;

    always @(posedge Rclk or negedge Rresetn) begin
        if(!Rresetn)begin
            ReadPtr <= 0;
            GrayReadPtr <= 0;
        end
        else begin
            ReadPtr <= NextReadPtr;
            GrayReadPtr <= NextGrayReadPtr;
        end
    end

    always @(posedge Rclk or negedge Rresetn) begin
        
        if (!Rresetn) begin
            empty <= 1'b1;
        end 
        else begin
            empty <= (NextGrayReadPtr == SynGrayWritePtr);
        end    
    end

endmodule

module AsynchronousFIFO #
(
    parameter DataSize = 3, 
    parameter AddrSize = 3
)

(
    Wclk, Rclk, Wresetn, Rresetn, Push, Pop, DataIn, DataOut, full, empty
);

input Wclk, Rclk;
input Wresetn, Rresetn;
input Push, Pop;
input [DataSize - 1 : 0] DataIn;

output [DataSize - 1 : 0] DataOut;
output reg full, empty;

parameter PtrWidth = $clog2(AddrSize);

reg [DataSize - 1 : 0] buffer [0 : AddrSize - 1];
wire [PtrWidth : 0] WritePtr, ReadPtr;
wire [PtrWidth : 0] SynGrayReadPtr,SynGrayWritePtr;
wire [PtrWidth : 0] GrayWritePtr,GrayReadPtr;

TwoFlipFlopSynchronizer #(PtrWidth) My2ffsynWrite
(
.clk(Wclk),
.reset(Wresetn),
.DataIn(GrayWritePtr),
.DataOut(SynGrayWritePtr)
);

TwoFlipFlopSynchronizer #(PtrWidth) My2ffsynRead
(
.clk(Rclk),
.reset(Rresetn),
.DataIn(GrayReadPtr),
.DataOut(SynGrayReadPtr)
);

WritePointerHandle #(PtrWidth) MyWPH
(
.Wclk(Wclk),
.Wresetn(Wresetn),
.Push(Push),
.SynGrayReadPtr(SynGrayReadPtr),
.GrayWritePtr(GrayWritePtr),
.WritePtr(WritePtr),
.full(full)
);

ReadPointerHandle #(PtrWidth) MyRPH
(
.Rclk(Rclk),
.Rresetn(Rresetn),
.Pop(Pop),
.SynGrayWritePtr(SynGrayWritePtr),
.GrayReadPtr(GrayReadPtr),
.ReadPtr(ReadPtr),
.empty(empty)
);

always @(posedge Wclk) begin
    if(Push && !full)begin
        buffer[WritePtr] <= DataIn;
    end
end
assign DataOut = buffer[ReadPtr];

endmodule