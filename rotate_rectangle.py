
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Polygon

# 1. Define the rectangle corners as vectors
# We define a simple rectangle.
corners = np.array([
    [1, 1],
    [5, 1],
    [5, 3],
    [1, 3]
])

# 2. Set up the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 6)
ax.set_ylim(0, 4)
ax.set_aspect('equal', adjustable='box')
ax.grid(True)

# Create a Polygon patch that we can update
poly = Polygon(corners, closed=True, fc='lightblue', ec='darkblue')
ax.add_patch(poly)

# 3. Calculate the center of the rectangle
center = np.mean(corners, axis=0)
ax.plot(center[0], center[1], 'ro') # Mark the center

# 4. Define the animation logic
# Total duration of 5 seconds. At 60fps, this is 300 frames.
total_frames = 5 * 60
# We will do a full 360-degree (2*pi radians) rotation
total_rotation = 2 * np.pi

def rotate_vectors(vectors, angle, center_point):
    """
    Rotates a set of vectors around a center point.
    """
    # Create the 2D rotation matrix
    rotation_matrix = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle),  np.cos(angle)]
    ])
    
    # Translate vectors to origin, rotate, then translate back
    # The @ operator is used for matrix multiplication in numpy
    return (vectors - center_point) @ rotation_matrix.T + center_point

def update(frame):
    """
    This function is called for each frame of the animation.
    """
    # Calculate the current angle of rotation
    current_angle = (frame / total_frames) * total_rotation
    
    # Get the new rotated corners
    rotated_corners = rotate_vectors(corners, current_angle, center)
    
    # Update the polygon with the new corner positions
    poly.set_xy(rotated_corners)
    return poly,

# 5. Create and run the animation
# interval is the delay between frames in milliseconds. 1000ms / 60fps = 16.67
ani = animation.FuncAnimation(fig, update, frames=range(total_frames), blit=True, interval=1000/60)

plt.title("Rectangle rotating around its center for 5 seconds")
plt.show()

