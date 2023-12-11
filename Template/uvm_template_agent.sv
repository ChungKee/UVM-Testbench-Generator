class {name}_agent extends uvm_agent;
    `uvm_component_utils({name}_agent)
    
    {name}_config cfg;
 
  
    function new(input string inst = "{name}_agent", uvm_component parent = null);
        super.new(inst,parent);
    endfunction
  
    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);
    
    endfunction
  
    virtual function void connect_phase(uvm_phase phase);
        super.connect_phase(phase);

    endfunction
 
endclass : {name}_agent