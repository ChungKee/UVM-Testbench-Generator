class AsynFIFO_ReadDriver extends uvm_driver #(AsynFIFO_ReadDriver_transaction);
    `uvm_component_utils(AsynFIFO_ReadDriver)
    
    virtual rails_if vif2;
    rails_transaction tr;
 
    
    function new(input string path = "AsynFIFO_ReadDriver", uvm_component parent = null);
        super.new(path,parent);
    endfunction
    
    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);

    endfunction
    
    virtual task run_phase(uvm_phase phase);

    
    endtask
  
endclass : AsynFIFO_ReadDriver