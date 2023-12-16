class AsynFIFO_test extends uvm_test;

    `uvm_component_utils(AsynFIFO_test)

    AsynFIFO_env env;  
  
    function new(input string inst = "AsynFIFO_test", uvm_component parent);
        super.new(inst, parent);
    endfunction
    
    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);
        env = AsynFIFO_env::type_id::create("env",this);

    endfunction
  
    virtual task run_phase(uvm_phase phase);
        phase.raise_objection(this);

        phase.drop_objection(this);
    endtask

endclass : AsynFIFO_test
