class {name}_monitor extends uvm_monitor;
  `uvm_component_utils({name}_monitor)
    
  function new(input string inst = "{name}_monitor", uvm_component parent = null);
    super.new(inst,parent);
  endfunction
    
  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);

  endfunction
    
 
endclass : {name}_monitor