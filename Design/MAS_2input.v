// 
// Designer: <N26115011> 
//
module ALU(
    input signed [4:0] Din1,
    input signed [4:0] Din2,
    input [1:0] Sel,
    output reg signed [4:0] Answer
);
  always @* begin
    case (Sel)
      2'b00:Answer = Din1 + Din2;
      2'b11:Answer = Din1 - Din2;
      default: Answer = Din1;
    endcase
    
  end
  
endmodule

module QComparator(
    input signed [4:0] Din,
    input signed [4:0] Q,
    output [1:0] Answer
);
  assign Answer[0] = ~Din[4];
  assign Answer[1] = (Din >= Q); 

endmodule

module MAS_2input(
    input signed [4:0]Din1,
    input signed [4:0]Din2,
    input [1:0]Sel,
    input signed[4:0]Q,
    output [1:0]Tcmp,
    output signed [4:0]TDout,
    output signed [3:0]Dout
);

/*Write your design here*/
wire signed [4:0] temp;
assign Dout = temp[3:0];

ALU ALU1(Din1, Din2, Sel, TDout);
QComparator my_QComparator(TDout, Q, Tcmp);
ALU ALU2(TDout, Q, Tcmp, temp);


endmodule