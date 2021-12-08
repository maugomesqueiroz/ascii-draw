import time
import random

from ascii_draw import Canvas, Colors
    
COLORS =  [
    Colors.fg.lightblue,
    Colors.fg.lightcyan,
    Colors.fg.lightred,
    Colors.fg.pink
]

CHARS = ['o','*','x']

class Particle:
    def __init__(self,x,y,color,char):
        self.x = x
        self.y = y
        self.color = color
        self.char = char
    def update_position(self):
        self.x += random.uniform(-1,1)
        self.y += random.uniform(-1,1)


# Creating list of particles
particles = []
for _ in range(30):
    particles.append(
        Particle(
            y=15,
            x=50,
            char=random.choice(CHARS),
            color=random.choice(COLORS),
        )
    )

# Starting random walk and canvas drawing
# For each timestep, rendering a blank canvas
# rendering each particle and updating its position

canvas = Canvas(size=(30,100))
for _ in range(50):
    canvas.render_canvas()
    for particle in particles:
        canvas.render_point(
            y=particle.y,
            x=particle.x,
            char=particle.char,
            color=particle.color
            )
        particle.update_position()
    canvas.update_screen() 
    time.sleep(0.1)