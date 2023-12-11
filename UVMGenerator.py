# %%
from queue import Queue

class Node:
    def __init__(self, name, child, type) -> None:
        self.name = name
        self.child = child
        self.type = type

class UVM_Generator:
    root = "top"
    def __init__(self) -> None:
        pass
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

        monitor    = Node("monitor",    child = None,               type = "monitor")
        driver     = Node("driver",     child = None,               type = "driver")
        scoreboard = Node("scoreboard", child = None,               type = "scoreboard")
        agent      = Node("agent",      child = [driver,monitor],   type = "agent")
        env        = Node("env",        child = [agent,scoreboard], type = "env")
        #env        = Node("env",        child = None,               type = "env")
        test       = Node("test",       child = [env],              type = "test")
        self.print_tree(test)
        self.CreateTestbench(test_name = "rails", node = test)

if __name__ == "__main__":

    UG = UVM_Generator()
    UG.DefaultInput()
   
# %%