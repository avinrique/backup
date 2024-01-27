import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Function to update the position of the dot
def update(frame, dot):
    dot.set_data(np.cos(frame), np.sin(frame))
    dot.set_3d_properties(np.sin(frame))

# Set up the figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a dot at the initial position
dot, = ax.plot([np.cos(0)], [np.sin(0)], [np.sin(0)], 'ro')

# Set up the animation
animation = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 100), fargs=(dot,), interval=50)

# Set axis limits
ax.set_xlim([-1.5, 1.5])
ax.set_ylim([-1.5, 1.5])
ax.set_zlim([-1.5, 1.5])

# Show the plot
plt.show()
