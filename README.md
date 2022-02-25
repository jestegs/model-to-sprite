# model-to-sprite

![run](https://user-images.githubusercontent.com/63424655/155032956-3a35c1c4-3333-4600-984f-f45da9b04c4d.gif)

A Blender python file for rendering animations as sprites from different angles

##

Rotates a user-specified camera object to different angles and renders an animation from each as a series of images.

Just define render settings as normal, copy/paste the script into blender, and run it.

### How to Use

This script rotates a user created object called 'focus' to render different angles of an object at it's center.
The focus object is typically the parent of a camera and a light source, or anything that you want to remain constant from
the player's point of view.

All render settings are defined normally in blender, however it is important that the output location in Blender's Output Settings is a directory,
and not the default of a file prefix, or else it will screw up the script's naming conventions. Note also that the compass directions 
correspond starting with the south-facing angle of the sprite, so the first series of images will be named "anim_s_0001.png" or something similar.

Enter the names of the actions that you want to render an animation of as a list, change the number of angles you want to render (8 or 4),
and run the script from the top play button.
All animations will be rendered as a series of images in a folder under the output directory named after the action.
