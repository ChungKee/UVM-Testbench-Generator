class rails_test extends uvm_test;

  `uvm_component_utils(rails_test)
  
  function new(input string inst = "rails_test", uvm_component c);
    super.new(inst,c);
  endfunction
  
  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);

  endfunction
 
  virtual task run_phase(uvm_phase phase);
    phase.raise_objection(this);

    phase.drop_objection(this);
  endtask

endclass : rails_test
