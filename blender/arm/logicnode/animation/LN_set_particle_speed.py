from arm.logicnode.arm_nodes import *

class SetParticleSpeedNode(ArmLogicTreeNode):
    """Use to set the speed of a particle source."""
    bl_idname = 'LNSetParticleSpeedNode'
    bl_label = 'Set Particle Speed'
    arm_version = 1

    def init(self, context):
        super(SetParticleSpeedNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_input('NodeSocketFloat', 'Speed', default_value=1.0)
        self.add_output('ArmNodeSocketAction', 'Out')

add_node(SetParticleSpeedNode, category=PKG_AS_CATEGORY)
