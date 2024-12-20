import bpy # type: ignore
import bpy_extras # type: ignore

def editRRfunc():
    # Setup
    scene = bpy.data.scenes['Scene']
    cam = bpy.data.objects['Camera']
    objs = bpy.data.objects


    scene.render.use_border = True
    scene.render.border_min_x = .3
    scene.render.border_min_y = .3
    scene.render.border_max_x = .7
    scene.render.border_max_y = .7

    print(scene.render.resolution_x)
    print(scene.render.resolution_y)

def setRR(num_divisions, block_num):
    # Setup
    scene = bpy.data.scenes['Scene']
    cam = bpy.data.objects['Camera']
    objs = bpy.data.objects

    scene.render.use_border = True

    # Check if the number of divisions is valid
    if num_divisions < 1:
        print("The number of divisions must be at least 1")
        return 0
    
    # Calculate the division size
    div_size = 1 / (num_divisions+1)

    # Block number to row and column 
    ''' Sei num_divisions = 4  
    row:   0    1    2    3  
    c:  .----.----.----.----.
      0 |  1 |  2 |  3 |  4 |
        :----+----+----+----:
      1 |  5 |  6 |  7 |  8 |
        :----+----+----+----:
      2 |  9 | 10 | 11 | 12 |
        :----+----+----+----:
      3 | 13 | 14 | 15 | 16 |
        '----'----'----'----'
    '''
    row = (block_num-1) % num_divisions
    col = (block_num-1) // num_divisions

    print(f"Row: {row}, Col: {col}")

    # Set the render region
    scene.render.border_min_x = div_size 
    scene.render.border_min_y = div_size
    scene.render.border_max_x = 0
    scene.render.border_max_y = 0
