class AsynFIFO_ReadMonitor extends uvm_monitor;
    `uvm_component_utils(AsynFIFO_ReadMonitor)
      
      
    function new(input string inst = "AsynFIFO_ReadMonitor", uvm_component parent = null);
       super.new(inst,parent);
    endfunction
      
    virtual function void build_phase(uvm_phase phase);
       super.build_phase(phase);

    endfunction
      
 
endclass : AsynFIFO_ReadMonitor