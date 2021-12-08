# ASCII Draw

A simple package for drawing ASCII on canvas, using Python.

To use it, 

* Import the package
* Draw a canvas
* Draw points inside the canvas
* Update the screen


```python
from ascii_draw import Canvas

canvas = Canvas(size=(30,100))
canvas.render_canvas()
canvas.render_point(y=15,x=50)
canvas.update_screen() 
```

Be creative!

## Examples:

### Random Walk:
```python
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
```
![](img/random_walk.gif)

### BOIDS:

Bird-like movement for each particle by following three rules. Code is in boids_example.py

![](img/boids.gif)