from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import math
from Camera import Camera
from Minimap import Minimap
from Scene import Scene

# PARAMETERS
WINDOW_SIZE = (1200, 600)
WALL_COLOR = (1,0.5,0.2)
BG_COLOR = (0,0,0) 
map = [  [1,1,1,1,1,1,1,1,1,1,1,1],
         [1,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,1,0,0,1,1,0,0,0,0,1],
         [1,0,0,0,0,1,1,0,0,0,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,0,0,0,0,0,0,0,0,1,1],
         [1,1,0,0,0,0,0,0,0,0,0,1],
         [1,0,0,0,0,0,0,1,0,0,0,1],
         [1,0,0,0,0,0,0,0,0,0,0,1],
         [1,0,0,1,1,1,0,0,0,0,0,1],
         [1,1,1,1,1,1,1,1,1,1,1,1]  ] 

scene = Scene(*WINDOW_SIZE)

# Left screen : Camera
camera = Camera((460,100), WINDOW_SIZE[0]//2, WINDOW_SIZE[1])
camera.setRotation(1.8)

# Right screen : minimap
minimap = Minimap(map)
minimap.setSkyColor(BG_COLOR)
minimap.setWallsColor(WALL_COLOR)

    
def move(key,x,y):
    (translationIncrement, rotationIncrement) = (5, 0.25)
    if key == b'z':
        if minimap.isInWall(*camera.calculateTranslatePos(translationIncrement)) == False:
            camera.forward(translationIncrement)
    if key == b's':
        if minimap.isInWall(*camera.calculateTranslatePos(-translationIncrement)) == False:
            camera.backward(translationIncrement)
    if key == b'q':
        camera.setRotation((camera.getRotation() - rotationIncrement) % (2*math.pi))
    if key == b'd':
        camera.setRotation((camera.getRotation() + rotationIncrement) % (2*math.pi))
        
    glutPostRedisplay()    
    

def update():
    """Clear screen & draw a new frame"""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    minimap.draw()
    camera.draw(minimap)
    minimap.drawPlayer(camera.getPosition(), camera.getRotation())
    glutSwapBuffers()
    

def main():
    """Open window & handle user events"""
    global scene
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(*WINDOW_SIZE)
    glutCreateWindow("Raycasting ({}x{} px)".format(WINDOW_SIZE[0], WINDOW_SIZE[1]))
    scene.init()
    glutDisplayFunc(update)
    glutKeyboardFunc(move)
    glutMainLoop()

if __name__ == "__main__":
    main()
    
    


