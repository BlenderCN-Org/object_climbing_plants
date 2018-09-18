import bpy
from bpy.types import (
    Operator,
)
from bpy.props import (
    IntProperty,
)
from mathutils import (
    Matrix,
    Vector
)
from mathutils.noise import (
    random_unit_vector,
    seed_set,
)
import bmesh
import numpy as np


class Particle():
    def __init__(self, id=0, branch_id=0, co=Vector((0, 0, 0)), parent=None):
        self.id = id
        self.branch_id = branch_id
        self.parent = parent
        self.children = []
        self.rest = Matrix.Translation(co)
        self.current = self.rest.copy()
        self.vel = Vector()

    def direction(self):
        if self.parent:
            return self.rest.translation - self.parent.rest.translation
        return Vector((0, 0, 1))


class Plant():
    def __init__(self, seed=Vector((0, 0, 0))):
        self.seed = seed
        self.particles = [Particle(co=self.seed)]
        self.step = 0

    def sim(self):
        self.grow_from(self.particles[-1])
        self.step += 1
        return

    def grow_from(self, p):
        growvec = p.direction().normalized()
        growvec += random_unit_vector(size=3) * 0.5
        growvec = growvec.normalized() * 0.1
        child = Particle(
            id=self.particles[-1].id + 1,
            co=p.rest.translation + growvec,
            parent=p)
        p.children.append(child)
        self.particles.append(child)
        print('added particle {id}'.format(id=child.id))


def setverts(self, context):
    ob = context.active_object if context.active_object else None
    if not ob:
        print('No active object')
        return
    self.bm = bmesh.new()
    for p in self.plant.particles:
        self.bm.verts.new(p.rest.translation)
    self.bm.verts.ensure_lookup_table()
    self.bm.to_mesh(ob.data)

    context.area.tag_redraw()


class OBJECT_OT_grow_ivy(Operator):
    """Grow Ivy"""
    bl_idname = 'object.grow_ivy'
    bl_label = 'Grow Ivy'
    bl_description = 'Grow Ivy'
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(self, context):
        return context.mode == 'OBJECT'

    def modal(self, context, event):
        # print(event.type, event.value)
        if event.type == 'ESC':
            print('FINISHED with {count} Particles\n'.format(
                count=len(self.plant.particles)))
            return {'FINISHED'}
        if event.type in ['MIDDLEMOUSE', 'WHEELDOWNMOUSE', 'WHEELUPMOUSE']:
            return {'PASS_THROUGH'}

        if event.type == 'TIMER':
            pass

        elif event.type == 'LEFTMOUSE' and event.value == 'PRESS':
            print('\nRUNNING SIM STEP')
            self.plant.sim()

            print('SETTING VERTS')
            setverts(self, context)
            return {'RUNNING_MODAL'}

        return {'RUNNING_MODAL'}

    def execute(self, context):
        # self._timer = context.window_manager.event_timer_add(
            # 0.1, window=context.window)
        print('\nEXECUTE')
        self.plant = Plant()
        setverts(self, context)
        return {'FINISHED'}

    def invoke(self, context, event):
        # self.init_loc_x = context.object.location.x
        # self.value = event.mouse_x
        seed_set(0)
        self.execute(context)
        context.window_manager.modal_handler_add(self)
        return {'RUNNING_MODAL'}
