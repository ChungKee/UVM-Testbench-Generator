
class AsynFIFO_env extends uvm_env;
    `uvm_component_utils(AsynFIFO_env)

    AsynFIFO_scoreboard scoreboard;
    AsynFIFO_WriteAgent WriteAgent;
    AsynFIFO_ReadAgent ReadAgent;  
  
    function new(input string inst = "AsynFIFO_env", uvm_component parent);
        super.new(inst, parent);
    endfunction
  
    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);
        scoreboard = AsynFIFO_scoreboard::type_id::create("scoreboard",this);
        WriteAgent = AsynFIFO_WriteAgent::type_id::create("WriteAgent",this);
        ReadAgent = AsynFIFO_ReadAgent::type_id::create("ReadAgent",this);

    endfunction
  
    virtual function void connect_phase(uvm_phase phase);
        super.connect_phase(phase)

    endfunction
 
endclass : AsynFIFO_env