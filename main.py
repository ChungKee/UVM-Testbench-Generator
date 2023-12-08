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


    def CreateTest(self, test_name, parent = root):
        line = []
        
        with open("Template/uvm_test.sv", mode = 'r') as template:
            line.append(template.read())
            line = line[-1].replace('{name}',test_name)

        svfile = "Result/" + test_name + "_test.sv"
        
        with open(svfile, mode = "w") as result:
            for s in line:
                result.write(s)

    def NormalTest(self, test_name):
        self.CreateTest(test_name)
    
    def dfs(self, root):
        MyQ = Queue()
        MyQ.put(root)

        while not MyQ.empty():
            temp = MyQ.get()
            print(temp.name)
            if temp.child != None:
                for children in temp.child:
                    MyQ.put(children)

    def DefaultInput(self):
        subscriber = Node("subscriber", None, "subscriber")
        monitor    = Node("monitor", None, "monitor")
        driver     = Node("driver",None,"driver")
        sequencer  = Node("sequencer",None,"sequencer")
        scoreboard = Node("scoreboard",None,"scoreboard")
        agent      = Node("agent",[sequencer,driver,monitor,subscriber],"agent")
        env        = Node("env",[agent,scoreboard],"enviroment")
        sequence   = Node("sequence", None, "sequence")
        test       = Node("test",[env,sequence],"test")
        root       = Node("top",[test],"root")
        self.dfs(root)

if __name__ == "__main__":
    
    UG = UVM_Generator()
    #UG.NormalTest(test_name = "rails")
    UG.DefaultInput()
   