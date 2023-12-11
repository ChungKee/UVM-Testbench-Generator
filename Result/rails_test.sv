class rails_test extends uvm_test;

    `uvm_component_utils(rails_test)

    rails_env e;  
  
    function new(input string inst = "rails_test", uvm_component parent);
        super.new(inst, parent);
    endfunction
    
    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);
        e = rails_env::type_id::create("e",this);

    endfunction
  
    virtual task run_phase(uvm_phase phase);
        phase.raise_objection(this);

        phase.drop_objection(this);
    endtask

endclass : rails_test
