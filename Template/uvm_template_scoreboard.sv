
class {name} extends uvm_scoreboard;
    `uvm_component_utils({name})


    function new(input string inst = "{name}", uvm_component parent);
        super.new(inst, parent);
    endfunction
  
    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);

    endfunction
 
endclass : {name}