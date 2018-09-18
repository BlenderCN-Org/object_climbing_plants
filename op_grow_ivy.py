import bpy
import numpy as np

from bpy.types import (
    Operator,
)
from bpy.props import (
    IntProperty,
)


class OBJECT_OT_grow_ivy(Operator):
    """Grow Ivy"""
    bl_idname = 'object.grow_ivy'
    bl_label = 'Grow Ivy'
    bl_description = 'Grow Ivy'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        return context.mode == 'OBJECT'

    def execute(self, context):
        return {'FINISHED'}
