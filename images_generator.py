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
  
def generate_graph_sum_of_two_vectors():
  vector1 = [1, 2]
  vector2 = [2, 1]

  # Sumar los vectores
  suma_vector = [vector1[0] + vector2[0], vector1[1] + vector2[1]]

  # Crear el gráfico
  plt.figure(figsize=(8, 6))

  # Graficar los vectores y su suma
  plt.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector 1')
  plt.quiver(0, 0, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector 2')
  plt.quiver(0, 0, suma_vector[0], suma_vector[1], angles='xy', scale_units='xy', scale=1, color='g', label='Suma')

  # Etiquetas y leyenda
  plt.xlabel('Eje X')
  plt.ylabel('Eje Y')
  plt.title('Suma de dos vectores en R^2')
  plt.axhline(0, color='black',linewidth=0.5)
  plt.axvline(0, color='black',linewidth=0.5)
  plt.grid(True)
  plt.legend()

  # Mostrar el gráfico
  plt.xlim(0, 4)
  plt.ylim(0, 4)
  plt.savefig("Images/1/sum_of_two_vectors.png")
  
# Chapter 1 - Vectors
# generate_vectors_plot_2d(3, save_path='Images/1/vectors.png', show=True)
# generate_vectors_plot_3d(3, save_path='Images/1/vectors_3d.png', show=True)
# generate_graph_sum_of_two_vectors()
