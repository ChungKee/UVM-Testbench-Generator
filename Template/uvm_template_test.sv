class {name} extends uvm_test;

    `uvm_component_utils({name})
  
  
    function new(input string inst = "{name}", uvm_component parent);
        super.new(inst, parent);
    endfunction
    
    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);

    endfunction
  
    virtual task run_phase(uvm_phase phase);
        phase.raise_objection(this);

        phase.drop_objection(this);
    endtask

endclass : {name}
