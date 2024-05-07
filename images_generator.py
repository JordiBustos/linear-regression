import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)

def generate_vectors_plot_2d(n, save_path=None, show=False):
  """Create a graph with n vectors.

  Args:
      n (int): number of vectors to plot
  """
  colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
  _, ax = plt.subplots()
  for i in range(n):
    x = np.random.randint(0, 10)
    y = np.random.randint(0, 10)
    ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color=colors[i % len(colors)])
    
  ax.set_xlim([0, 10])
  ax.set_ylim([0, 10])
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_aspect('equal')
  ax.grid(True)
  
  if save_path:
    plt.savefig(save_path)
  if show:
    plt.show()
  
def generate_vectors_plot_3d(n, save_path=None, show=False):
  """Create a graph with n vectors.

  Args:
      n (int): number of vectors to plot
  """
  colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  for i in range(n):
    x = np.random.randint(0, 10)
    y = np.random.randint(0, 10)
    z = np.random.randint(0, 10)
    ax.quiver(0, 0, 0, x, y, z, color=colors[i % len(colors)])
    
  ax.set_xlim([0, 10])
  ax.set_ylim([0, 10])
  ax.set_zlim([0, 10])
  ax.set_xlabel('x')
  ax.set_ylabel('y')
  ax.set_zlabel('z')
  ax.set_aspect('equal')
  ax.grid(True)
  
  if save_path:
    plt.savefig(save_path)
  if show:
    plt.show()
  
# Chapter 1 - Vectors
# generate_vectors_plot_2d(3, save_path='Images/1/vectors.png', show=True)
# generate_vectors_plot_3d(3, save_path='Images/1/vectors_3d.png', show=True)

