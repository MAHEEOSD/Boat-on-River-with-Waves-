
import math, sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

W, H = 1000, 600
BASE = 225                                  
t, amp, boat_x, boat_v, paused, last_ms = 0.0, 1.0, 200.0, 40.0, False, 0
clouds = [[120.0, 520.0, 1.0], [480.0, 560.0, 0.8], [800.0, 500.0, 1.2]]   # x, y, scale

def reset():
    global t, amp, boat_x, boat_v
    t, amp, boat_x, boat_v = 0.0, 1.0, 200.0, 40.0

def poly(p, c):                                         
    glColor3f(*c)
    glBegin(GL_POLYGON)
    for px, py in p:
        glVertex2f(px, py)
    glEnd()

def rect(x, y, w, h, c):
    poly([(x, y), (x + w, y), (x + w, y + h), (x, y + h)], c)

def circle(cx, cy, r, c):
    """Bresenham (midpoint) circle, filled with horizontal lines."""
    glColor3f(*c)
    x, y, d = 0, int(r), 3 - 2 * int(r)
    glBegin(GL_LINES)
    while x <= y:
        for a, b in ((x, y), (y, x)):                  
            for sy in (b, -b):
                glVertex2f(cx - a, cy + sy)
                glVertex2f(cx + a, cy + sy)
        if d < 0:
            d += 4 * x + 6
        else:
            d += 4 * (x - y) + 10
            y -= 1
        x += 1
    glEnd()

def text(x, y, s, c=(0, 0, 0), font=GLUT_BITMAP_HELVETICA_12):
    glColor3f(*c)
    glRasterPos2f(x, y)
    for ch in s:
        glutBitmapCharacter(font, ord(ch))

def surf(x, base, ph=0.0):
    """Water height at x = two sine waves moving with time t."""
    a = 12 * amp
    return base + a * math.sin(0.02 * x - 1.6 * t + ph) + 0.4 * a * math.sin(0.05 * x + 2.3 * t + ph)

def slope(x):                                           
    a = 12 * amp
    return a * 0.02 * math.cos(0.02 * x - 1.6 * t) + 0.4 * a * 0.05 * math.cos(0.05 * x + 2.3 * t)

def water(base, ph, c):
    glBegin(GL_QUAD_STRIP)                             
    for x in range(0, W + 1, 10):
        glColor4f(c[0] * 0.6, c[1] * 0.6, c[2] * 0.7, c[3])
        glVertex2f(x, 0)
        glColor4f(*c)
        glVertex2f(x, surf(x, base, ph))
    glEnd()
    glColor4f(1, 1, 1, 0.8)
    glLineWidth(2)
    glBegin(GL_LINE_STRIP)                              
    glVertex2f(x, surf(x, base, ph))
    glEnd()


def draw_sky():
    glBegin(GL_QUADS)                                 
    lo, hi = (0.8, 0.92, 1.0), (0.3, 0.6, 0.95)
    for x, y, c in ((0, 240, lo), (W, 240, lo), (W, H, hi), (0, H, hi)):
        glColor3f(*c)
        glVertex2f(x, y)
    glEnd()
    glPushMatrix()                                     
    glTranslatef(860, 500, 0)
    glRotatef(t * 15, 0, 0, 1)
    glColor3f(1, 0.85, 0.2)
    glLineWidth(3)
    glBegin(GL_LINES)
    for i in range(12):
        a = math.radians(i * 30)
        for r in (52, 75):
            glVertex2f(r * math.cos(a), r * math.sin(a))
    glEnd()
    glPopMatrix()
    circle(860, 500, 40, (1, 0.9, 0.3))
    for cx, cy, s in clouds:
        for dx, dy, r in ((0, 0, 24), (28, 8, 30), (58, 0, 24), (30, -6, 22)):
            circle(cx + dx * s, cy + dy * s, r * s, (1, 1, 1))

def draw_land():
    for cx, w, h, c in ((150, 200, 90, (0.3, 0.5, 0.4)), (450, 230, 120, (0.25, 0.45, 0.35)),
                        (760, 210, 100, (0.3, 0.52, 0.4)), (980, 160, 80, (0.28, 0.48, 0.38))):
        poly([(cx - w, 285), (cx + w, 285), (cx, 285 + h)], c)   
    rect(0, 240, W, 45, (0.25, 0.6, 0.3))                       

def draw_birds():
    glColor3f(0.1, 0.1, 0.1)
    glLineWidth(2)
    glBegin(GL_LINES)
    for k in range(3):
        bx, by = (200 + k * 90 + t * 30) % 1100 - 50, 470 + 15 * k + 10 * math.sin(t + k)
        for sx in (-1, 1):                                       # wings flap with sin
            glVertex2f(bx, by)
            glVertex2f(bx + sx * 14, by + 12 * math.sin(t * 8 + k))
    glEnd()

def draw_boat():
   
    glPushMatrix()
    glTranslatef(boat_x, surf(boat_x, BASE), 0)
    glRotatef(math.degrees(math.atan(slope(boat_x))), 0, 0, 1)
    if boat_v < 0:
        glScalef(-1, 1, 1)
    poly([(-70, 12), (95, 12), (60, -22), (-50, -22)], (0.55, 0.3, 0.12))   
    rect(-70, 4, 160, 8, (0.8, 0.15, 0.15))                    
    rect(-2, 12, 4, 108, (0.35, 0.2, 0.1))                      
    poly([(6, 118), (6, 30), (75, 30)], (0.98, 0.95, 0.9))        
    poly([(-6, 112), (-6, 30), (-55, 30)], (0.9, 0.35, 0.3))      
    poly([(2, 120), (2, 138), (26 + 5 * math.sin(t * 9), 129)], (0.9, 0.1, 0.1))   
    for px in (-30, 0, 30):
        circle(px, -6, 5, (0.75, 0.9, 1))                        
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    draw_sky()
    draw_birds()
    draw_land()
    water(BASE, 0.0, (0.1, 0.4, 0.75, 1.0))                     
    draw_boat()
    water(BASE - 30, 1.5, (0.2, 0.55, 0.85, 0.6))                
    text(20, 570, "Boat on River with Waves", font=GLUT_BITMAP_TIMES_ROMAN_24)
    text(20, 545, "Wave height: x%.1f   Boat speed: %d%s" % (amp, boat_v, "   [PAUSED]" if paused else ""))
    text(20, 15, "LEFT/RIGHT: Speed   + / - : Waves   SPACE: Pause   R: Reset   ESC: Exit", c=(1, 1, 1))
    glutSwapBuffers()

def timer(_):
    global t, boat_x, last_ms
    now = glutGet(GLUT_ELAPSED_TIME)
    dt = min((now - (last_ms or now)) / 1000.0, 0.05)
    last_ms = now
    if not paused:
        t += dt
        boat_x += boat_v * dt
        boat_x = (boat_x + 120) % (W + 240) - 120              
        for c in clouds:
            c[0] = (c[0] + 8 * c[2] * dt + 100) % (W + 200) - 100
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)

def keyboard(key, x, y):
    global paused, amp
    if key == b"\x1b":
        sys.exit(0)
    paused = not paused if key == b" " else paused
    if key in (b"+", b"=", b"-", b"_"):
        amp = max(0.25, min(3.0, amp + (0.25 if key in (b"+", b"=") else -0.25)))
    elif key in (b"r", b"R"):
        reset()

def special(key, x, y):
    global boat_v
    if key in (GLUT_KEY_LEFT, GLUT_KEY_RIGHT):
        boat_v = max(-120, min(120, boat_v + (20 if key == GLUT_KEY_RIGHT else -20)))

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(W, H)
    glutCreateWindow(b"Boat on River with Waves - PyOpenGL")
    glMatrixMode(GL_PROJECTION)
    gluOrtho2D(0, W, 0, H)                                       
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special)
    glutTimerFunc(16, timer, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
