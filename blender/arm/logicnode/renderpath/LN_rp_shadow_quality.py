from arm.logicnode.arm_nodes import *

class RpShadowQualityNode(ArmLogicTreeNode):
    """Configure shadow quality node"""
    bl_idname = 'LNRpShadowQualityNode'
    bl_label = 'Rp Shadow Quality'
    property0: EnumProperty(
        items = [('High', 'High', 'High'),
                 ('Medium', 'Medium', 'Medium'),
                 ('Low', 'Low', 'Low')
                 ],
        name='', default='Medium')

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_output('ArmNodeSocketAction', 'Out')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')

add_node(RpShadowQualityNode, category=PKG_AS_CATEGORY)
