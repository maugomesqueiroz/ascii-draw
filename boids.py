import time
import random
import math
from typing import NewType
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
        self.velocity = (random.uniform(-1,1),random.uniform(-1,1))

    def update_position(self):
        self.x += 2*(self.velocity[0])
        self.y += 2*(self.velocity[1])

    def update_velocity(self, direction):

        new_x_vel = self.velocity[0] + direction[0]
        new_y_vel = self.velocity[1] + direction[1]

        norm = math.sqrt(new_x_vel**2+new_y_vel**2)

        particle.velocity = (
            new_x_vel/norm,
            new_y_vel/norm
        )


    def distance(self, other):
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)


height = 30
width = 150

# Creating list of particles
particles = []
for _ in range(25):
    particles.append(
        Particle(
            y=random.uniform(0,height),
            x=random.uniform(0,width),
            char=random.choice(CHARS),
            color=random.choice(COLORS),
        )
    )

# Starting random walk and canvas drawing
# For each timestep, rendering a blank canvas
# rendering each particle and updating its position

canvas = Canvas(size=(height, width))
for _ in range(400):
    canvas.render_canvas()

    for particle in particles:
        canvas.render_point(
            y=particle.y,
            x=particle.x,
            char=particle.char,
            color=particle.color
            )

        change_direction = (0,0)
        separation_vector = (0,0)
        alignment_vector = (0,0)
        neighbor_count = 1
        center_of_neighbors = (0,0)

        for other_particle in particles:

            distance = particle.distance(other_particle)

            # Separation: too close, I want to get away
            if distance < 2 and distance != 0 : 
                separation_vector = (
                    other_particle.x - particle.x,
                    other_particle.y - particle.y
                )

            # Alignment: I want my velocity as my neighbors
            if distance < 5: 
                alignment_vector = (
                    alignment_vector[0] + other_particle.velocity[0],
                    alignment_vector[1] + other_particle.velocity[1]
                )
            
                neighbor_count += 1

                center_of_neighbors = (
                    center_of_neighbors[0] + other_particle.x,
                    center_of_neighbors[1] + other_particle.y,
                )

        # Cohesion: I want to go to the geometric center
        center_of_neighbors = (
            (center_of_neighbors[0]/neighbor_count) - particle.x,
            (center_of_neighbors[1]/neighbor_count) - particle.y,
        )
     
        update_x = (-10*separation_vector[0]) + (5*alignment_vector[0]/neighbor_count) + (0.5*center_of_neighbors[0])
        update_y = (-10*separation_vector[1]) + (5*alignment_vector[1]/neighbor_count) + (0.5*center_of_neighbors[1])
   
        center_of_screen = (
            width/2 - particle.x,
            height/2 - particle.y,
        )

        update_x += 0.25 * center_of_screen[0]
        update_y += 0.25 * center_of_screen[1]

        change_direction = (
            change_direction[0] + update_x,
            change_direction[1] + update_y
        )  
        
        particle.update_velocity(change_direction)
        particle.update_position()

        # Check if it is going out of bounds:
        if particle.y >= height:
            particle.y -= height
        if particle.y < 0:
            particle.y += height

        if particle.x >= width:
            particle.x -= width
        if particle.x < 0:
            particle.x += width

 
    canvas.update_screen() 
    time.sleep(0.1)