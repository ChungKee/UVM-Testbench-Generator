# UVM-Testbench-Generator
 Can generate the uvm testbench automatically

## Details
- Easy implementation
- Suport agent, driver, environment, monitor, scoreboard, test, sequence, sequence_item
- Suport build_phase 


## File
|Filename | Description|
|-        | -|
|Result   | Get the .sv from this file|
|Template | The uvm template|
|UVMGenerator.py     | Run this python code and get the uvm testbench in Result        |
|VisualizationUVM.py | Visualization of UVM hierarchy                                  |
|MakeUVMPowerPoint.py| Make the UVM graph in powerpoint version                        |
|ReadDesign          | Read the verilog design(.v) module and write the interface(.sv) |
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



## Visualization
### Install
1. The visualization of UVM need to import anytree and graphviz
2. future --> Teach how to install the requirement of visualization

### How to get the pic?
1. Open the VisualizationFlag in UVMGenerator class.
2. The name of output picture is "UVM_TestbenchHierarchy.png"

#### One Agent   

![image](https://github.com/ChungKee/UVM-Testbench-Generator/blob/main/Template/UVM_OneAgent.png)

#### Two Agent

![image](https://github.com/ChungKee/UVM-Testbench-Generator/blob/main/Template/UVM_TestbenchHierarchy.png)
