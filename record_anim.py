"""
Omni Sprite Renderer
Render and save multiple angles of an animation as a series of images.

Usage:
    Camera and light source are set up manually.
    Program just rotates the camera and light object 
    around an empty and renders the output at each angle.
    
    Steps:
        1. Add an empty item called 'focus' and include everything
                that you want to stay consistent as a child (e.g. Camera and light source)
                
            This is what is going to rotate around the mesh and render each angle.
            
        2. Adjust camera/render settings to what you want the output to be, just like normal
        3. Change the "attributes for rendering" below for each time you run the script.
        4. Run the script.
    
(
    Remember to change Blender's render output location in scene settings (Output Properties)

    Paths ending in '\' are directories, otherwise Blender treats it as a file prefix,
    which might mess with this script's naming conventions.
)
"""

import os
import math

import bpy

# -----------------------------------------------------
# attributes for rendering

# names of animations ex. ["idle", "run", "attack"]
anim_names = ["idle", "run"]
# number of perspectives to record for each animation
number_of_angles = 8


# file prefixes
omni_prefixes = [
    "_s_",
    "_sw_",
    "_w_",
    "_nw_",
    "_n_",
    "_ne_",
    "_e_",
    "_se_"
]
four_prefixes = [
    "_s_",
    "_w_",
    "_n_",
    "_e_"
]

# -----------------------------------------------------


def record_anim():
    """
    Record animation 
    """
    global animation_name
    global number_of_angles
    
    assert (number_of_angles == 8 or number_of_angles == 4)
    
    user_output_path = bpy.context.scene.render.filepath
    if not os.path.exists(user_output_path):
        print(
                user_output_path + 
                " doesn't exist. Please create the directory first."
        )
        return
    dump_path = user_output_path
    
    # get focus object (empty with camera/light children)
    focus = bpy.context.scene.objects['focus']
    # get armature object
    armature = bpy.context.scene.objects['Armature']
    # get actions of scene
    actions = bpy.data.actions
    
    angle_step = 360 / number_of_angles
    
    for anim in anim_names:
        prefix_idx = 0
        anim_path = os.path.join(user_output_path, anim+"\\")
        
        # creates a new directory with the name of the animation
        # will return an ERROR if the directory already exists
        os.mkdir(anim_path)
        
        for angle_num in range(number_of_angles):
            angle = math.radians(angle_num * angle_step)
            
            # set animation to render
            armature.animation_data.action = actions[actions.find(anim)]
            # adjust equipment (focus angle)
            focus.rotation_euler.z = angle
            
            # render images
            # adds directory with anim name
            if number_of_angles == 8:
                dump_path = os.path.join(anim_path, str(anim+omni_prefixes[prefix_idx]))
            elif number_of_angles == 4:
                dump_path = os.path.join(anim_path, str(anim+four_prefixes[prefix_idx]))
            else:
                print("invalid number of angles")
                return
            
            bpy.context.scene.render.filepath = dump_path
            bpy.ops.render.render(animation=True)
            
            prefix_idx += 1
            
        print("Sprites rendered to:")
        print(anim_path)
    
    bpy.context.scene.render.filepath = user_output_path


if __name__ == "__main__":
    record_anim()
