class AsynFIFO_WriteMonitor extends uvm_monitor;
    `uvm_component_utils(AsynFIFO_WriteMonitor)
      
      
    function new(input string inst = "AsynFIFO_WriteMonitor", uvm_component parent = null);
       super.new(inst,parent);
    endfunction
      
    virtual function void build_phase(uvm_phase phase);
       super.build_phase(phase);

    endfunction
      
 
endclass : AsynFIFO_WriteMonitor