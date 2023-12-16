
class AsynFIFO_scoreboard extends uvm_scoreboard;
    `uvm_component_utils(AsynFIFO_scoreboard)


    function new(input string inst = "AsynFIFO_scoreboard", uvm_component parent);
        super.new(inst, parent);
    endfunction
  
    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);

    endfunction
 
endclass : AsynFIFO_scoreboard