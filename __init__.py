# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>

bl_info = {
    "name": "Climbing Plants",
    "author": "florianfelix",
    "version": (0, 1, 0),
    "blender": (2, 80, 0),
    "location": "",
    "description": "Growing Plants",
    "wiki_url": "",
    "category": "Object",
}

if 'bpy' in locals():
    from importlib import reload
    reload(op_grow_ivy)

import bpy

from object_climbing_plants import op_grow_ivy


def btn_grow_ivy(self, context):
    layout = self.layout
    layout.operator(op_grow_ivy.OBJECT_OT_grow_ivy.bl_idname)


classes = (
    op_grow_ivy.OBJECT_OT_grow_ivy,
)


def register():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)


if __name__ == "__main__":
    register()
