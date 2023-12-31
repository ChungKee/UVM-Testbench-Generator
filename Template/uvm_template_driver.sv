class {name} extends uvm_driver #({name}_transaction);
    `uvm_component_utils({name})
    
    virtual rails_if vif2;
    rails_transaction tr;
 
    
    function new(input string path = "{name}", uvm_component parent = null);
        super.new(path,parent);
    endfunction
    
    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);

    endfunction
    
    virtual task run_phase(uvm_phase phase);

    
    endtask
  
endclass : {name}