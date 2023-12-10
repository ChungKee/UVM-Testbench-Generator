class rails_agent extends uvm_agent;
  `uvm_component_utils(rails_agent)
  
  rails_config cfg;
 
  function new(input string inst = "rails_agent", uvm_component parent = null);
    super.new(inst,parent);
  endfunction
 
  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);
  
  endfunction
 
  virtual function void connect_phase(uvm_phase phase);
	super.connect_phase(phase);

  endfunction
 
endclass : rails_agent