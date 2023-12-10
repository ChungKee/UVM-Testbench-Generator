
class {name}_env extends uvm_env;
  `uvm_component_utils({name}_env)
 
  function new(input string inst = "{name}_env", uvm_component parent);
    super.new(inst, parent);
  endfunction
 
  virtual function void build_phase(uvm_phase phase);
    super.build_phase(phase);

  endfunction
 
  virtual function void connect_phase(uvm_phase phase);
    super.connect_phase(phase)

  endfunction
 
endclass : {name}_env