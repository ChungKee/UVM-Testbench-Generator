class AsynFIFO_ReadAgent extends uvm_agent;
    `uvm_component_utils(AsynFIFO_ReadAgent)

    AsynFIFO_ReadMonitor ReadMonitor;
    AsynFIFO_ReadDriver ReadDriver;    
    AsynFIFO_ReadAgent_config cfg;
 
  
    function new(input string inst = "AsynFIFO_ReadAgent", uvm_component parent = null);
        super.new(inst,parent);
    endfunction
  
    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);
        ReadMonitor = AsynFIFO_ReadMonitor::type_id::create("ReadMonitor",this);

        if (cfg.is_active == UVM_ACTIVE) begin
            ReadDriver = AsynFIFO_ReadDriver::type_id::create("ReadDriver",this);
        end
        
    endfunction
  
    virtual function void connect_phase(uvm_phase phase);
        super.connect_phase(phase);

    endfunction
 
endclass : AsynFIFO_ReadAgent