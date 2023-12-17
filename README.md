# UVM-Testbench-Generator
 Can generate the uvm testbench automatically

## Details
- Easy implementation
- Suport agent, driver, environment, monitor, scoreboard, test, sequence, sequence_item

## File
|Filename | Description|
|-        | -|
|Result   | Get the result from this file|
|Template | The uvm template|
|main.py  | Run this python code and get the uvm testbench in Result |

## Easy Example

1. run UVMGenerator.py
2. Get the hierarchy 
```
[0] test
  [1] env
    [2] agent
      [3] driver
      [3] monitor
    [2] scoreboard
```
3. Copy the result from Result file


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
