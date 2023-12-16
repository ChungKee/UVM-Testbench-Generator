class {name} extends uvm_agent;
    `uvm_component_utils({name})
    
    {name}_config cfg;
 
  
    function new(input string inst = "{name}", uvm_component parent = null);
        super.new(inst,parent);
    endfunction
  
    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);

        if (cfg.is_active == UVM_ACTIVE) begin
        end
        
    endfunction
  
    virtual function void connect_phase(uvm_phase phase);
        super.connect_phase(phase);
        if (cfg.is_active == UVM_ACTIVE) begin
        end
        
    endfunction
 
endclass : {name}