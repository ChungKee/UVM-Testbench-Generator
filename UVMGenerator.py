# %%
from queue import Queue
from VisualizationUVM import Visualization_UVM
import os

class UVMNode:
    def __init__(self, name, child, type) -> None:
        self.name = name
        self.child = child
        self.type = type

class UVM_Generator:
    root = "top"
    def __init__(self) -> None:
        self.VisualizationFlag = False

    def CheckType(self, type):
        SupportType = ["test","env","agent","scoreboard","monitor","driver","sequence","sequence_item"]
        if type in SupportType:
            return True
        else:
            return False
        
    def WriteBuildPhase(self, testname, node, line):
        for child in node.child or []:
            for index, row in enumerate(line):
                if "component_utils" in row:
                    line.insert(index + 1, "\n")
                    DeclareVariable = "    "+testname + "_" + child.name + " " + child.name + ";"
                    line.insert(index + 2, DeclareVariable)
                
                if "super.build_phase" in row and child.type != "driver":
                    temp = f"        {child.name} = {testname}_{child.name}::type_id::create(\"{child.name}\",this);\n"
                    line.insert(index + 1, temp)
                
                if "is_active" in row and child.type == "driver":
                    temp = f"            {child.name} = {testname}_{child.name}::type_id::create(\"{child.name}\",this);\n"
                    line.insert(index + 1, temp)

        return line

    def CopyTemplate(self, test_name, node):
        line = []
        
        with open("Template/uvm_template_"+ node.type +".sv", mode = 'r') as template:
            for row in template:
                row = row.replace('{name}', test_name + "_" + node.name)
                if "{item_name}" in row:
                    row = row.replace('{item_name}', test_name + "_" + node.child[0].name)
                line.append(row)
        return line
    
    def WriteSV(self, line, test_name, name):
        svfile = "Result/" + test_name + "_"+ name +".sv"
        with open(svfile, mode = "w") as result:
            for s in line or []:
                result.write(s)

    def CreateTestbench(self, test_name, node):
        line = []
        if self.CheckType(node.type):
            line = self.CopyTemplate(test_name, node)
            line = self.WriteBuildPhase(test_name, node, line)
            self.WriteSV(line, test_name, node.name)
        for children in node.child or []:
            self.CreateTestbench(test_name, children)

    def dfs(self, root):
        MyQ = Queue()
        MyQ.put(root)

        while not MyQ.empty():
            temp = MyQ.get()
            print(temp.name)
            if temp.child != None:
                for children in temp.child:
                    MyQ.put(children)
    
    def print_tree(self,node, indent=0):
        print("    " * indent + f"[{indent}] {node.name}")
        for child in node.child or []:
            self.print_tree(child, indent + 1)

    def DefaultInput(self):
        test_name = "AsynFIFO"
        monitor    = UVMNode("monitor",    child = None,               type = "monitor")
        driver     = UVMNode("driver",     child = None,               type = "driver")
        scoreboard = UVMNode("scoreboard", child = None,               type = "scoreboard")
        agent      = UVMNode("agent",      child = [driver,monitor],   type = "agent")
        env        = UVMNode("env",        child = [agent,scoreboard], type = "env")
        test       = UVMNode("test",       child = [env],              type = "test")
        
        print("The UVM testbench : ")
        self.print_tree(test)
        
        if self.VisualizationFlag == True :
            Visualization_UVM().VisualizeUVMNode(UVM_node=test)
        
        self.CreateTestbench(test_name = test_name, node = test)

    def TwoAgentInput(self):
        test_name = "AsynFIFO"
        WriteMonitor  = UVMNode("WriteMonitor",  child = None,                                type = "monitor")
        WriteDriver   = UVMNode("WriteDriver",   child = None,                                type = "driver")
        ReadMonitor   = UVMNode("ReadMonitor",   child = None,                                type = "monitor")
        ReadDriver    = UVMNode("ReadDriver",    child = None,                                type = "driver")
        scoreboard    = UVMNode("scoreboard",    child = None,                                type = "scoreboard")
        ReadAgent     = UVMNode("ReadAgent",     child = [ReadDriver,ReadMonitor],            type = "agent" )
        WriteAgent    = UVMNode("WriteAgent",    child = [WriteDriver,WriteMonitor],          type = "agent")
        env           = UVMNode("env",           child = [ReadAgent, WriteAgent, scoreboard], type = "env")
        sequence_item = UVMNode("sequence_item", child = None,                                type = "sequence_item")
        sequence      = UVMNode("sequence",      child = [sequence_item],                     type = "sequence")
        test          = UVMNode("test",          child = [env,sequence],                      type = "test")
        
        
        print("The UVM testbench : ")
        self.print_tree(test)
        
        if self.VisualizationFlag == True :
            Visualization_UVM().VisualizeUVMNode(UVM_node=test)
        if not os.path.exists("Result"):
            os.makedirs("Result")
        files = os.listdir("Result")
        for file in files:
            os.remove("Result/"+file)

        self.CreateTestbench(test_name = test_name, node = test)
        

if __name__ == "__main__":

    UG = UVM_Generator()
    UG.TwoAgentInput()


# %%