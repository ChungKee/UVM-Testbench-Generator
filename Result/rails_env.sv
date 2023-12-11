
class rails_env extends uvm_env;
    `uvm_component_utils(rails_env)

    rails_scoreboard s;
    rails_agent a;  
  
    function new(input string inst = "rails_env", uvm_component parent);
        super.new(inst, parent);
    endfunction
  
    virtual function void build_phase(uvm_phase phase);
        super.build_phase(phase);
        s = rails_scoreboard::type_id::create("s",this);
        a = rails_agent::type_id::create("a",this);

    endfunction
  
    virtual function void connect_phase(uvm_phase phase);
        super.connect_phase(phase)

    endfunction
 
endclass : rails_env