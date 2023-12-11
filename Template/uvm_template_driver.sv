class {name}_driver extends uvm_driver #({name}_transaction);
    `uvm_component_utils({name}_driver)
    
    virtual rails_if vif2;
    rails_transaction tr;
 
    
    function new(input string path = "{name}_driver", uvm_component parent = null);
        super.new(path,parent);
    endfunction
    
    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);

    endfunction
    
    virtual task run_phase(uvm_phase phase);

    
    endtask
  
endclass : rails_driver