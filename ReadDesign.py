#%%
import os
import re

class module:
    def __init__(self, name) -> None:
        self.name = name
        self.child = []
        self.input_variable = []
        self.output_variable = []

class ReadingDesign:
    
    def __init__(self) -> None:
        self.root = []
        self.head = []

    def FindRoot(self, name):
        count = 0
        for rt in self.root:
            if name == rt.name:
                return count
            count = count + 1

        return count

    def GetVariable(self,line):
        ans = line.replace("output","")
        ans = ans.replace("input","")
        ans = ans.replace("wire","")
        ans = ans.replace("reg","")
        ans = ans.replace("signed","")
        ans = ans.replace(",","")
        ans = ans.replace("\n","")
        ans = ans.replace(" ","")
        return ans

    def ImportDesign(self):
        path = "Design"
        files = os.listdir(path)

        for file in files:
            f1 = open(path + "\\" + file,"r")
            for line in f1:
                if "module " in line and "endmodule" not in line:
                    name = line.replace("module","")
                    name = name.replace(" ","")
                    name = name.replace("(","")
                    name = name.replace("\n","")
                    self.root.append(module(name))
                    self.head.append(len(self.root) - 1)
                if "input " in line:
                    self.root[-1].input_variable.append(self.GetVariable(line))
                if "output " in line and "module" not in line:
                    self.root[-1].output_variable.append(self.GetVariable(line))
            f1.close()
        
        return None

    def LinkDesign(self):
        path = "Design"
        files = os.listdir(path)

        for file in files:
            f1 = open(path + "\\" + file,"r")
            child_index = 0
            parent_index = 0
            for line in f1:
                if "module " in line and "endmodule" not in line:
                    module = line.replace("module","")
                    module = module.replace(" ","")
                    module = module.replace("(","")
                    module = module.replace("\n","")
                    
                if "(" in line and "module" not in line:
                    for rt in self.root:
                        name = rt.name[:-1]
                        if name in line:
                            child_index = self.FindRoot(rt.name)
                            parent_index = self.FindRoot(module)
                            self.root[parent_index].child.append(self.root[child_index])
                            if child_index in self.head:
                                self.head.remove(child_index)
                            break
            f1.close()

    def PrintHierarchyDesign(self):
        print("\nThe Hierarchy of Design:")
        for hd in self.head:
            self.print_tree(self.root[hd], 0)
        
        return None
    
    def print_tree(self, node, indent=0):
        print("    " * indent + f"[{indent}] {node.name}")
        for child in node.child or []:
            self.print_tree(child, indent + 1)

    def WriteInterface(self):
        self.ImportDesign()
        self.LinkDesign()
        self.PrintHierarchyDesign()
        for hd in self.head:
            f1 = open("Result\\" + self.root[hd].name + "_if.sv","w")
            f1.write("interface " + self.root[hd].name + "_if;\n")
            for input in self.root[hd].input_variable:
                f1.write("    logic "+ input + ";\n")
            for output in self.root[hd].output_variable:
                f1.write("    logic "+ output + ";\n")
            f1.write("endinterface\n")
            f1.close()
"""
if __name__ == "__main__":
    RD = ReadingDesign()
    RD.ImportDesign()
    RD.LinkDesign()
    RD.PrintHierarchyDesign() 
    RD.WriteInterface()
"""
#%%