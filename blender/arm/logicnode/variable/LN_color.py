from arm.logicnode.arm_nodes import *

class ColorNode(ArmLogicTreeNode):
    """Color node"""
    bl_idname = 'LNColorNode'
    bl_label = 'Color'
    arm_version = 1

    def init(self, context):
        super(ColorNode, self).init(context)
        self.add_input('NodeSocketColor', 'Color', default_value=[0.8, 0.8, 0.8, 1.0])
        self.add_output('NodeSocketColor', 'Color', is_var=True)

add_node(ColorNode, category=PKG_AS_CATEGORY)
