from anytree import Node
from anytree.exporter import UniqueDotExporter

class Visualization_UVM:
    def __init__(self) -> None:
        pass

    def DfsNode(self, UVM_node):
        root = Node(name=UVM_node.name)
        child_list = []
        for child in UVM_node.child or []:
            child_list.append(Node(child.name))
            child_list[-1] = self.DfsNode(child)
        root.children = child_list
        '''
        for child in UVM_node.child or []:
            root.children = self.DfsNode(child)
        '''
        return root
    
    def VisualizeUVMNode(self, UVM_node):
        root = self.DfsNode(UVM_node = UVM_node)
        UniqueDotExporter(root).to_picture("UVM_TestbenchHierarchy.png")