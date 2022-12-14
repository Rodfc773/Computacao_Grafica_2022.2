from cmath import cos, sin
from contextlib import nullcontext
import string
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import glm
import pygame

# tamanho da tela
WINDOW_WIDHT = 1280
WINDOW_HEIGHT = 720

# camera
cameraPos = glm.vec3(10, 15, 30)
cameraFront = glm.vec3(0, 0, -1)
cameraUp = glm.vec3(0, 1, 0)
angle = 0

#posição inicial da bola
xi = 25
zi = 37.5

# mouse
old_mouse_x = 0
old_mouse_y = 0
angle_x = -1.57
angle_y = 1.57
mouse_speed = 0.1
mouse_sensitivity = 0.001


half_width = WINDOW_WIDHT / 2
half_height = WINDOW_HEIGHT / 2




def sphere():
    global xi, zi
    if (xi > 50 or xi  < 0) or (zi > 75 or zi < 0):
        xi = 25
        zi = 37.5
    glTranslatef(xi, 0.5, zi)
    glColor3f(0,0, 1)
    glutSolidSphere(0.5,128,128)
def draw_pixel(xo, zo):
    
    glBegin(GL_POINT)
    glVertex2f(xo,zo)
    glEnd()

def draw_wall(x0, y0, z0, x1, y1, z1):
    glBegin(GL_QUADS)
    glVertex3f(x0, y0, z0)
    glVertex3f(x1, y0, z1)
    glVertex3f(x1, y1, z1)
    glVertex3f(x0, y1, z0)
    glEnd()

def Square(A, B, C, D):
    glBegin(GL_POLYGON);

    glVertex3fv(A);
    glVertex3fv(B);
    glVertex3fv(C);
    glVertex3fv(D);

    glEnd();

def rep( t0, t1, t2, t3, t4, t5, t6, t7):
    glColor3f(1,1,1)
    Square(t0, t1, t2, t3)

    glColor3f(1,1,1)
    Square(t4, t5, t6, t7)

    glColor3f(1,1,1)
    Square(t0, t4, t7, t3)

    glColor3f(1,1,1)
    Square(t1, t5, t6, t2)

    glColor3f(1,1,1)
    Square(t3, t2, t6, t7)

    glColor3f(1,1,1)
    Square(t0, t1, t5, t4)

def RenderString(x, y, font):
    global string
    
    glColor3f(1, 1, 1)
    glRasterPos2f(x, y)
    glutBitmapString(font, string);
def trave():
    t1i =   [
                [23.5, 5.5, 0],
                [23, 5.5, 0],
                [23, 0, 0],
                [23.5, 0, 0],
                [23.5, 5.5, 0.5],
                [23, 5.5, 0.5],
                [23, 0, 0.5],
                [23.5, 0, 0.5],
            ]

    t2i =   [
                [28.02, 5.5, 0],
                [28, 5.5, 0],
                [28, 0, 0],
                [28.02, 0, 0],
                [28.02, 5.5, 0.5],
                [28, 5.5, 0.5],
                [28, 0, 0.5],
                [28.02, 0, 0.5],
            ]
    
    t3i =   [
                [28.02, 5.5, 0],
                [23, 5.5, 0],
                [23, 5, 0],
                [28.02, 5, 0],
                [28.02, 5.5, 0.5],
                [23, 5.5, 0.5],
                [23, 5, 0.5],
                [28.02, 5, 0.5],
            ]
    t4i =  [
            [28.02, 5.5, 75],
                [23, 5.5, 75],
                [23, 5, 75],
                [28.02, 5, 75],
                [28.02, 5.5, 74.5],
                [23, 5.5, 74.5],
                [23, 5, 74.5],
                [28.02, 5, 74.5],
         ]
    t5i = [
                 [28.02, 5.5, 75],
                [28, 5.5, 75],
                [28, 0, 75],
                [28.02, 0, 75],
                [28.02, 5.5, 74.5],
                [28, 5.5, 74.5],
                [28, 0, 74.5],
                [28.02, 0, 74.5],
    ]
    t6i = [
        
                [23.5, 5.5, 75],
                [23, 5.5, 75],
                [23, 0, 75],
                [23.5, 0, 75],
                [23.5, 5.5, 74.5],
                [23, 5.5, 74.5],
                [23, 0, 74.5],
                [23.5, 0, 74.5],
    ]
    
    rep(t1i[0], t1i[1], t1i[2], t1i[3], t1i[4], t1i[5], t1i[6], t1i[7])
    rep(t2i[0], t2i[1], t2i[2], t2i[3], t2i[4], t2i[5], t2i[6], t2i[7])
    rep(t3i[0], t3i[1], t3i[2], t3i[3], t3i[4], t3i[5], t3i[6], t3i[7])
    rep(t4i[0], t4i[1], t4i[2], t4i[3], t4i[4], t4i[5], t4i[6], t4i[7])
    rep(t5i[0], t5i[1], t5i[2], t5i[3], t5i[4], t5i[5], t5i[6], t5i[7])
    rep(t6i[0], t6i[1], t6i[2], t6i[3], t6i[4], t6i[5], t6i[6], t6i[7])
    

def draw_floor(x, y, z, width, length): # x, y, z, largura, comprimento
    glBegin(GL_QUADS)
    glVertex3f(x, y, z)
    glVertex3f(x, y, z + length)
    glVertex3f(x + width, y, z + length)
    glVertex3f(x + width, y, z)
    glEnd()


def draw_block(x, y, z, width, length, height): # largura, comprimento, altura
    draw_wall(x, y, z, x, y + height, z+length) # plano zy, parte esquerda
    draw_wall(x, y, z, x+width, y + height, z) # plano xy, parte traseira
    draw_wall(x+width, y, z, x + width, y + height, z + length) # plano zy, parte direita
    draw_wall(x, y, z+length, x + width, y + height, z + length) # plano xy, parte dianteira
    #draw_floor(x, y, z, width, length) # parte de baixo
    draw_floor(x, y+height, z, width, length) # parte de cima
    
def draw_arredores(x, y, z, width, length, height):
    draw_wall(x, y, z, x, y + height, z+length) # plano zy, parte esquerda
    draw_wall(x, y, z, x+width, y + height, z) # plano xy, parte traseira
    draw_wall(x+width, y, z, x + width, y + height, z + length) # plano zy, parte direita
    draw_wall(x, y, z+length, x + width, y + height, z + length) # plano xy, parte dianteira
    
def Bresenham(xo ,zo, xf,zf, y):
    dz = zf - zo
    dx = xf - xo
    
    E = 2 * dz
    Ne = 2 * (dz - dx)
    
    d = 2 * dz - dx
    glColor3f(1.0, 1.0, 1.0)
    # glBegin(GL_LINE)
    
    while xo <= xf and zo <= zf:
        glPointSize(4.5)
        glBegin(GL_POINTS)
        glVertex3f(xo, y, zo)
        glEnd()
        
        if d <= 0:
            if xo == xf:
                d = d + E
            else:
                xo += 0.1
                d = d + E
        else:
            if xo == xf: 
                zo += 0.1 
                d = d + Ne
                
            elif zo == zf:
                xo += 0.1
                d = d + Ne
            else:
                xo += 0.1
                zo += 0.1
                d = d + Ne
            
        #glVertex3f(xo, y, zo)
        
        #glEnd()
def display():
    # limpa cor e buffers de profundidade
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # reseta transformações
    glLoadIdentity()

    # define camera
    gluLookAt(cameraPos.x, cameraPos.y, cameraPos.z,
              cameraPos.x + cameraFront.x, cameraPos.y + cameraFront.y, cameraPos.z + cameraFront.z,
              cameraUp.x, cameraUp.y, cameraUp.z)


    glPushMatrix() # push

    # campo
    tam = 50
    largura = 75
    glColor3f(0.0, 0.7, 0.4)
    draw_floor(0, 0, 0, tam, largura)
    glColor3f(0, 0.7, 0.4)
    draw_block(0, 0, 0, tam, largura, 2.5)
    glColor3f(1, 1, 0)
    glTranslatef(0, 2.5, 0)
    draw_arredores(0, 0, 0, tam, largura, 1.5)
    
    #Desenha a linha  pelo bresenham nas bordas
    Bresenham(0, 0, tam, 0,0)
    Bresenham(0, largura, tam, largura,0.0)
    Bresenham(tam, 0.0, tam, largura,0.0)
    Bresenham(0.0, 0.0, 0, largura,0.0)
    
    #Desenha as marcações do gol Esquerdo
    Bresenham(20, 0.0, 20, 4, 0)
    Bresenham(20, 4, 33, 4, 0)
    Bresenham(33, 0, 33, 4, 0)
    #Desenha a area fora do gol esquerdo
    Bresenham(17 , 0, 17, 10, 0)
    Bresenham(17 , 10 ,36, 10, 0)
    Bresenham(36 , 0 ,36, 10, 0)
    
    #Desenha as marcações do gol direito
    Bresenham(20 , largura - 4, 20, largura, 0)
    Bresenham(20, largura - 4, 33, largura - 4, 0)
    Bresenham(33, largura - 4, 33, largura, 0)

    #Desenha as marcações externa do gol direito
    Bresenham(17, largura - 10, 17, largura, 0)
    Bresenham(17, largura - 10, 36, largura - 10, 0)
    Bresenham(36, largura - 10, 36, largura,0)
    
    #Desnehando a linha central
    Bresenham(0, 37.5, 50, 37.5, 0)
    sphere()
    glPopMatrix()  # pop

    glPushMatrix()

    trave()
    #RenderString(0, 12, GLUT_BITMAP_TIMES_RIMAN_24)
    

    glPopMatrix()




    glutSwapBuffers()


def keyboard(key, x, y):
    global angle, cameraFront, cameraUp, cameraPos, light_ambient, light_specular, light_diffuse, zi, xi

    cameraSpeed = 0.5

    if not isinstance(key, int):
        key = key.decode("utf-8")
    #controles da camera
    if key == 'w' or key == 'W':
        cameraPos += cameraSpeed * cameraFront
    elif key == 'a' or key == 'A':
        cameraPos -= glm.normalize(glm.cross(cameraFront, cameraUp)) * cameraSpeed
    elif key == 's' or key == 'S':
        cameraPos -= cameraSpeed * cameraFront
    elif key == 'd' or key == 'D':
        cameraPos += glm.normalize(glm.cross(cameraFront, cameraUp)) * cameraSpeed
    elif key == 'q' or key == 'Q':
        cameraPos.y += cameraSpeed/2
    elif key == 'e' or key == 'E':
        cameraPos.y -= cameraSpeed/2
    elif key == 'm' or key == 'M':
        cameraPos = glm.vec3(10, 15, 30)
        cameraFront = glm.vec3(0, 0, -1)
        cameraUp = glm.vec3(0, 1, 0)
        angle = 0

    #controle da iluminação
    if key == 'r':
        glEnable(GL_LIGHT0)
    if key == 't':
        glDisable(GL_LIGHT0)
    
    #controle da bola
    if key == 'K' or key == 'k':
        zi += 0.5
        display()
    if key == 'I' or key == 'i':
        zi -= 0.5
        display()
        
    if key == 'L' or key == 'l':
        xi += 0.5
        display()
    if key == 'J' or key == 'j':
        xi -= 0.5
        display()


    glutPostRedisplay()


def change_side(w, h):
    global half_width, half_height
    if h == 0:
        h = 1
    ratio = w * 1/h

    glMatrixMode(GL_PROJECTION)

    glLoadIdentity()

    glViewport(0, 0, w, h)

    half_width = w / 2
    half_height = h / 2

    gluPerspective(45, ratio, 0.1, 100)

    glMatrixMode(GL_MODELVIEW)


def mouse_click(button, state, x, y):
    global old_mouse_x, old_mouse_y
    old_mouse_x = x
    old_mouse_y = y


def mouse_camera(mouse_x, mouse_y):
    global mouse_sensitivity, mouse_speed, angle_x, angle_y, cameraFront, old_mouse_x, old_mouse_y

    angle_x -= (mouse_x - old_mouse_x) * mouse_sensitivity
    angle_y -= (mouse_y - old_mouse_y) * mouse_sensitivity

    front = glm.vec3()
    front.x = glm.cos(angle_x) * glm.sin(angle_y)
    front.z = glm.sin(angle_x) * glm.sin(angle_y)
    front.y = glm.cos(angle_y)
    cameraFront = front

    old_mouse_x = mouse_x
    old_mouse_y = mouse_y
    glutPostRedisplay()


def setup_lighting():
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    #glEnable(GL_LIGHT1)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_NORMALIZE)

    glMaterialfv(GL_FRONT, GL_SPECULAR, [0.1, 0.1, 0.1, 1])

    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.8, 0.8, 0.8, 1])
    # glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.2, 0.2, 0.2, 1])

    glLightfv(GL_LIGHT0, GL_SPECULAR, [0.7, 0.7, 0.7, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.3, 0.3, 0.3, 1])
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 7, 0, 1])

    # spot light
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [1, 1, 1, 1])
    glLightfv(GL_LIGHT1, GL_SPECULAR, [1, 1, 1, 1])

    glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, [0, -1, 0])
    glLightfv(GL_LIGHT1, GL_POSITION, [0, 6, -1])

    glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 20)
    glLightf(GL_LIGHT1, GL_SPOT_EXPONENT, 2.0)


def main():
    # inicialização
    glutInit()  # inicia glut
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(WINDOW_WIDHT, WINDOW_HEIGHT)
    window = glutCreateWindow("Campo de futebol")

    #iluminação
    setup_lighting()

    #callbacks
    glutDisplayFunc(display)
    glutReshapeFunc(change_side)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(mouse_click)
    glutMotionFunc(mouse_camera)

    glutMainLoop()


main()