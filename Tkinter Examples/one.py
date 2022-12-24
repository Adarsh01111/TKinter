from tkinter import *
from pyopengltk import OpenGLFrame
from OpenGL import GL
from OpenGL import GLU
import numpy as np

verticies = (    (1, -1),    (1, 1),    (-1, 1),    (-1, -1),
                  )

edges = ((0,1),(2,1),(2,3),(0,3))

colors=[1.0, 0.0, 0.0,
        0.0, 1.0, 0.0,
        0.0, 0.0, 1.0]
colors=np.array(colors,dtype=np.float32)

def Cube():
    GL.glColor3f(1,0,0)
    

    GL.glBegin(GL.GL_LINES)
    for edge in edges:
        for vertex in edge:
            x=verticies[vertex]
            GL.glVertex2f(x[0],x[1])
            
            
    GL.glEnd()

class CubeSpinner( OpenGLFrame ):
    def initgl(self):
        
        GL.glClearColor(0.0, 1.0, 0.0, 0.0) 
        
        GLU.gluPerspective(45, (self.width/self.height), 5, 50.0)
       
        GL.glTranslatef(0.0,0.0, -5)
    def redraw(self):
        
        GL.glClear(GL.GL_COLOR_BUFFER_BIT|GL.GL_DEPTH_BUFFER_BIT)
        Cube()

def main():
    root = Tk()
    root.geometry('500x500')
    app = CubeSpinner(root, width=500, height=500)
    app.place(x=0,y=0)
    app.animate = 1
    app.after(100, app.printContext)
    
    app.mainloop()

if __name__=="__main__":
    main()