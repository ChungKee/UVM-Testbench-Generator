# %%
from queue import Queue
from VisualizationUVM import Visualization_UVM

class UVMNode:
    def __init__(self, name, child, type) -> None:
        self.name = name
        self.child = child
        self.type = type

class UVM_Generator:
    root = "top"
    def __init__(self) -> None:
        self.VisualizationFlag = False
    
    def input_data(self,root) -> None:
        self.dfs(root)

    def CheckType(self, type):
        SupportType = ["test","env","agent","scoreboard","monitor","driver"]
        if type in SupportType:
            return True
        else:
            return False
        
    def WriteBuildPhase(self, testname, node, line):
        for child in node.child or []:
            for index, row in enumerate(line):
                if "utils" in row:
                    line.insert(index + 1, "\n")
                    DeclareVariable = "    "+testname + "_" + child.type + " " + child.type[0] + ";"
                    line.insert(index + 2, DeclareVariable)
                
                if "super.build_phase" in row:
                    temp = f"        {child.type[0]} = {testname}_{child.type}::type_id::create(\"{child.type[0]}\",this);\n"
                    line.insert(index + 1, temp)
        return line

    def CopyTemplate(self, test_name, type):
        line = []
        
        with open("Template/uvm_template_"+ type +".sv", mode = 'r') as template:
            for row in template:
                row = row.replace('{name}', test_name)
                line.append(row)
        return line
    
    def WriteSV(self, line, test_name, type):
        svfile = "Result/" + test_name + "_"+ type +".sv"
        with open(svfile, mode = "w") as result:
            for s in line or []:
                result.write(s)

    def CreateTestbench(self, test_name, node):
        line = []
        if self.CheckType(node.type):
            line = self.CopyTemplate(test_name, node.type)
            line = self.WriteBuildPhase(test_name, node, line)
            self.WriteSV(line, test_name, node.type)
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
        print("  " * indent + f"[{indent}] {node.name}")
        for child in node.child or []:
            self.print_tree(child, indent + 1)

    def DefaultInput(self):

        monitor    = UVMNode("monitor",    child = None,               type = "monitor")
        driver     = UVMNode("driver",     child = None,               type = "driver")
        scoreboard = UVMNode("scoreboard", child = None,               type = "scoreboard")
        agent      = UVMNode("agent",      child = [driver,monitor],   type = "agent")
        env        = UVMNode("env",        child = [agent,scoreboard], type = "env")
        #env        = UVMNode("env",        child = None,               type = "env")
        test       = UVMNode("test",       child = [env],              type = "test")
        print("The UVM testbench : ")
        self.print_tree(test)
        if self.VisualizationFlag == True :
            Visualization_UVM().VisualizeUVMNode(UVM_node=test)
        
        self.CreateTestbench(test_name = "rails", node = test)

if __name__ == "__main__":

    UG = UVM_Generator()
    UG.DefaultInput()
    '''
    monitor    = UVMNode("monitor",    child = None,               type = "monitor")
    driver     = UVMNode("driver",     child = None,               type = "driver")
    scoreboard = UVMNode("scoreboard", child = None,               type = "scoreboard")
    agent      = UVMNode("agent",      child = [driver,monitor],   type = "agent")
    env        = UVMNode("env",        child = [agent,scoreboard], type = "env")
    #env        = UVMNode("env",        child = None,               type = "env")
    test       = UVMNode("test",       child = [env],              type = "test")
    Visualization_UVM().VisualizeUVMNode(UVM_node=test)
    '''
# %%