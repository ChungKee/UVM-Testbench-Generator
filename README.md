# UVM-Testbench-Generator
 Can generate the uvm testbench automatically

## Feature
1. Main feature is to generate the UVM testbench (.sv) automatically 
2. Reading the design (.v) --> write the interface (.sv) and print the hierarchy of design 
3. Generate UVM graph (.pptx) and let the user to modify the UVM graph in powerpoint

## File
|Filename | Description|
|-        | -|
|Result   | Get the (.sv) from this file|
|Template | The uvm template|
|UVMGenerator.py     | Run this python code and get the uvm testbench in Result          |
|VisualizationUVM.py | Visualization of UVM hierarchy                                    |
|MakeUVMPowerPoint.py| Make the UVM graph in powerpoint version                          |
|ReadDesign          | Read the verilog design (.v) module and write the interface (.sv) |
## Easy Example

1. run UVMGenerator.py
2. Get the simple version of the hierarchy of testbench and design
```
The Hierarchy of UVM:
[0] test1
    [1] env
        [2] ReadAgent
            [3] ReadDriver
            [3] ReadMonitor
        [2] WriteAgent
            [3] WriteDriver
            [3] WriteMonitor
        [2] scoreboard
    [1] sequence
        [2] sequence_item

The Hierarchy of Design:
[0] MAS_2input
    [1] ALU
    [1] QComparator
    [1] ALU

```
3. Copy the .sv from Result file

## Input
1. Can choose TwoAgentInput() or OneAgentInput() to create UVM testbench.
    
    a. OneAgentInput :

    ![image](https://github.com/ChungKee/UVM-Testbench-Generator/blob/main/Template/UVM_OneAgent.png)

    b. TwoAgentInput : 

    ![image](https://github.com/ChungKee/UVM-Testbench-Generator/blob/main/Template/UVM_TestbenchHierarchy.png)

2. Customizing UVM testbench by modify TwoAgentInput() or OneAgentInput().

## Generate UVM graph (.pptx)
Two agent in powerpoint sample:
![image](https://github.com/ChungKee/UVM-Testbench-Generator/blob/main/Template/2Agent_Powerpoint.png)
Maximum with 4 agent:
![image](https://github.com/ChungKee/UVM-Testbench-Generator/blob/main/Template/4Agent_Powerpoint.png)