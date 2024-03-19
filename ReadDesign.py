#%%
import os
import re

class module:
    def __init__(self, name) -> None:
        self.name = name
        self.child = None
        self.input_variable = []
        self.output_variable = []
class ReadingDesign:
    
    def __init__(self) -> None:
        self.root = []

    def GetVariable(self,line):
        ans = line.replace("output","")
        ans = ans.replace("input","")
        ans = ans.replace("wire","")
        ans = ans.replace("reg","")
        ans = ans.replace("signed","")
        ans = ans.replace(",","")
        ans = re.sub(r'\[[^\]]*\]', '', ans)
        ans = ans.replace(" ","")
        return ans

    def ImportDesign(self):
        path = "Design"
        files = os.listdir(path)

        for file in files:
            f1 = open(path + "\\" + file,"r")
            for line in f1:
                if "module" in line and "endmodule" not in line:
                    name = line.replace("module","")
                    name = name.replace(" ","")
                    name = name.replace("(","")
                    self.root.append(module(name))
                if "input" in line and "module" not in line:
                    self.root[-1].input_variable.append(self.GetVariable(line))
                if "output" in line and "module" not in line:
                    self.root[-1].output_variable.append(self.GetVariable(line))
            f1.close()
        
        for m in self.root:
            for iv in m.input_variable:
                print(iv)
            for ov in m.output_variable:
                print(ov)
        return None

    def LinkDesign(self):
        pass

    def PrintHierarchyDesign(self):
        return None

if __name__ == "__main__":
    RD = ReadingDesign()
    RD.ImportDesign()

#%%