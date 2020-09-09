from arm.logicnode.arm_nodes import *

class ReadFileNode(ArmLogicTreeNode):
    """Read File node"""
    bl_idname = 'LNReadFileNode'
    bl_label = 'Read File'

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('NodeSocketString', 'File')
        self.add_input('NodeSocketBool', 'Use cache', default_value=1)
        self.add_output('ArmNodeSocketAction', 'Loaded')
        self.add_output('NodeSocketString', 'String')

add_node(ReadFileNode, category=PKG_AS_CATEGORY, section='file')
