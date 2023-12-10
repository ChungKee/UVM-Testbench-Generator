class rails_monitor extends uvm_monitor;
  `uvm_component_utils(rails_monitor)
    
  function new(input string inst = "rails_monitor", uvm_component parent = null);
    super.new(inst,parent);
  endfunction
    
  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);

  endfunction
    
 
endclass : rails_monitor