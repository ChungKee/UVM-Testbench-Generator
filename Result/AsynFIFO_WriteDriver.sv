class AsynFIFO_WriteDriver extends uvm_driver #(AsynFIFO_WriteDriver_transaction);
    `uvm_component_utils(AsynFIFO_WriteDriver)
    
    virtual rails_if vif2;
    rails_transaction tr;
 
    
    function new(input string path = "AsynFIFO_WriteDriver", uvm_component parent = null);
        super.new(path,parent);
    endfunction
    
    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);

    endfunction
    
    virtual task run_phase(uvm_phase phase);

    
    endtask
  
endclass : AsynFIFO_WriteDriver