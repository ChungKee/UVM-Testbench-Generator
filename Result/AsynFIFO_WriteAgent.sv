class AsynFIFO_WriteAgent extends uvm_agent;
    `uvm_component_utils(AsynFIFO_WriteAgent)

    AsynFIFO_WriteMonitor WriteMonitor;
    AsynFIFO_WriteDriver WriteDriver;    
    AsynFIFO_WriteAgent_config cfg;
 
  
    function new(input string inst = "AsynFIFO_WriteAgent", uvm_component parent = null);
        super.new(inst,parent);
    endfunction
  
    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);
        WriteMonitor = AsynFIFO_WriteMonitor::type_id::create("WriteMonitor",this);

        if (cfg.is_active == UVM_ACTIVE) begin
            WriteDriver = AsynFIFO_WriteDriver::type_id::create("WriteDriver",this);
        end
        
    endfunction
  
    virtual function void connect_phase(uvm_phase phase);
        super.connect_phase(phase);

    endfunction
 
endclass : AsynFIFO_WriteAgent