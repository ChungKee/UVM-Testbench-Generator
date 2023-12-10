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

    def CreateTest(self, test_name, type):
        line = []
        
        with open("Template/uvm_template_"+ type +".sv", mode = 'r') as template:
            line.append(template.read())
            line[-1] = line[-1].replace('{name}',     test_name)

        svfile = "Result/" + test_name + "_"+ type +".sv"

        with open(svfile, mode = "w") as result:
            for s in line:
                result.write(s)
    
    def CreateTestbench(self, test_name, node):
        if self.CheckType(node.type):
            self.CreateTest(test_name, node.type)
        for child in node.child or []:
            self.CreateTestbench(test_name, child)

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
        test       = Node("test",       child = [env],              type = "test")
        self.print_tree(test)
        self.CreateTestbench(test_name = "rails", node = test)

if __name__ == "__main__":

    UG = UVM_Generator()
    UG.DefaultInput()
   
# %%