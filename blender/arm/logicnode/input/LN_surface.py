from arm.logicnode.arm_nodes import *

class SurfaceNode(ArmLogicTreeNode):
    """Surface node"""
    bl_idname = 'LNMergedSurfaceNode'
    bl_label = 'Surface'
    property0: EnumProperty(
        items = [('Touched', 'Touched', 'Touched'),
                 ('Started', 'Started', 'Started'),
                 ('Released', 'Released', 'Released'),
                 ('Moved', 'Moved', 'Moved')],
        name='', default='Touched')

    def init(self, context):
        self.add_output('ArmNodeSocketAction', 'Out')
        self.add_output('NodeSocketBool', 'State')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')

add_node(SurfaceNode, category=PKG_AS_CATEGORY, section='surface')
