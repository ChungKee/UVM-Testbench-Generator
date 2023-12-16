class {name} extends uvm_sequence#({item_name}) ;
    `uvm_object_utils({name})
    
    {item_name} tr;  
  
    function new(string name = "{name}");
        super.new(name);
    endfunction
    
    virtual task body();
        tr = {item_name}::type_id::create("tr");
        start_item(tr);

        finish_item(tr);
    endtask
endclass : {name}