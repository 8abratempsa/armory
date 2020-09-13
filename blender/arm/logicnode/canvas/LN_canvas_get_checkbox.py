from arm.logicnode.arm_nodes import *

class CanvasGetCheckboxNode(ArmLogicTreeNode):
    """Get canvas checkbox value"""
    bl_idname = 'LNCanvasGetCheckboxNode'
    bl_label = 'Canvas Get Checkbox'
    arm_version = 1

    def init(self, context):
        super(CanvasGetCheckboxNode, self).init(context)
        self.add_input('NodeSocketString', 'Element')
        self.add_output('NodeSocketBool', 'Value')

add_node(CanvasGetCheckboxNode, category=PKG_AS_CATEGORY)
