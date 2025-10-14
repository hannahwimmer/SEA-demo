import numpy as np
import matplotlib.pyplot as plt
from sea_demo.codes.assignment02_fitness import fitness_function


def plot_fitness_grid(fitness_function, fixed_dims, fixed_values, grid_points=100):
    """
    plots a contour of the fitness function by varying two dimensions while keeping the
    other two fixed.

    inputs:
    - fitness_function: callable, e.g., fitness_function(roast, blend, grind, brew_time)
    - fixed_dims: list of two strings, e.g., ['roast', 'blend'] (dims to keep fixed)
    - fixed_values: list of two floats, values for the fixed dimensions
    - grid_points: int, resolution of the grid
    output: contour plot
    """

    # all dimension names
    all_dims = ['roast', 'blend', 'grind', 'brew_time']
    variable_dims = [d for d in all_dims if d not in fixed_dims]

    # create grid
    X_vals = np.linspace(0, 100, grid_points)
    Y_vals = np.linspace(0, 100, grid_points)
    X, Y = np.meshgrid(X_vals, Y_vals)
    Z = np.zeros_like(X)

    # compute fitness
    for i in range(grid_points):
        for j in range(grid_points):
            args = dict(zip(fixed_dims, fixed_values))
            args[variable_dims[0]] = X[i,j]
            args[variable_dims[1]] = Y[i,j]
            Z[i,j] = fitness_function(**args)

    # plot
    plt.figure(figsize=(8,6))
    contour = plt.contourf(X, Y, Z, levels=20, cmap='viridis')
    plt.colorbar(contour, label='Quality Score')
    plt.xlabel(variable_dims[0].capitalize())
    plt.ylabel(variable_dims[1].capitalize())
    plt.title(f"Fitness Landscape (fixed {fixed_dims[0]}={fixed_values[0]}, {fixed_dims[1]}={fixed_values[1]})")
    plt.show()


# Example usage:
if __name__ == "__main__":
    plot_fitness_grid(
        fitness_function, fixed_dims=['roast','blend'], fixed_values=[50,50]
    )

