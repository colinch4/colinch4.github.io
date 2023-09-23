---
layout: post
title: "Trajectory generation and following in Python control"
description: " "
date: 2023-09-23
tags: [Python, ControlSystem]
comments: true
share: true
---

One of the fundamental aspects of control systems is generating and following trajectories. Trajectory generation involves creating a desired path or trajectory that a system should follow. Trajectory following, on the other hand, focuses on controlling the system to track the desired trajectory as closely as possible.

In this blog post, we will explore how to perform trajectory generation and following using Python and its control library. We will cover both one-dimensional and multi-dimensional trajectory generation and show how to implement them in Python.

## One-Dimensional Trajectory Generation

Let's start by generating a simple one-dimensional trajectory using a polynomial. We can use the `numpy` library to manipulate arrays and polynomials in Python. Below is an example code snippet that generates a trajectory of a point moving along the y-axis:

```python
import numpy as np

def generate_trajectory(time, coefficients):
    t = np.linspace(0, time, num=100)  # Generate 100 time points
    polynomial = np.poly1d(coefficients)  # Create a polynomial with given coefficients
    y = polynomial(t)  # Evaluate the polynomial at different time points
    return t, y

# Example usage
time = 10  # Total time duration
coefficients = [1, 0, -1]  # Coefficients for y(t) = t^2 - t

t, y = generate_trajectory(time, coefficients)
```

In the above code, we define a `generate_trajectory` function that takes the total duration `time` and the coefficients of the polynomial as inputs. It then creates a numpy array `t` representing the time points and evaluates the polynomial at those points to generate the trajectory `y`.

## Multi-Dimensional Trajectory Generation

To generate multi-dimensional trajectories, we often use parametric equations or spline interpolation. Parametric equations define the position of a point in terms of one or more parameters. Spline interpolation constructs a smooth curve that passes through given data points.

Let's generate a two-dimensional trajectory using spline interpolation. We can utilize the `scipy` library in addition to `numpy` for this purpose. Below is an example code snippet that generates a two-dimensional trajectory:

```python
import numpy as np
from scipy.interpolate import CubicSpline

def generate_trajectory(time, waypoints):
    t = np.linspace(0, time, num=100)  # Generate 100 time points
    x = waypoints[:, 0]  # Extract x-coordinates of waypoints
    y = waypoints[:, 1]  # Extract y-coordinates of waypoints
    spline_x = CubicSpline(t, x)  # Create a cubic spline for x-coordinates
    spline_y = CubicSpline(t, y)  # Create a cubic spline for y-coordinates
    trajectory_x = spline_x(t)  # Evaluate the spline at different time points
    trajectory_y = spline_y(t)
    return trajectory_x, trajectory_y

# Example usage
time = 10  # Total time duration
waypoints = np.array([[0, 0], [2, 3], [5, 1], [7, 4]])  # Array of waypoints

trajectory_x, trajectory_y = generate_trajectory(time, waypoints)
```

In the above code, we define a `generate_trajectory` function that takes the total duration `time` and an array of waypoints as inputs. It then extracts the x and y coordinates from the waypoints and creates cubic splines for both dimensions. The cubic splines are evaluated at different time points to obtain the final trajectory.

## Trajectory Following

Once we have generated a trajectory, the next step is to control a system to track that trajectory. The control strategy will vary depending on the system dynamics and requirements. One common approach is to use a feedback control law such as PID.

Here is a high-level code snippet that demonstrates how to implement trajectory following using PID control:

```python
import control

def follow_trajectory(trajectory, kp, ki, kd):
    system = control.TransferFunction([1], [1])  # System transfer function
    controller = control.TransferFunction([kp, ki, kd], [1, 0])  # PID controller transfer function
    feedback = control.feedback(controller * system, 1)  # Closed-loop transfer function
    t, y = control.step_response(feedback * trajectory)  # Simulate the response
    
    return t, y

# Example usage
trajectory = control.TransferFunction([1], [1, 1])  # Example trajectory
kp = 1.0  # Proportional gain
ki = 0.5  # Integral gain
kd = 0.2  # Derivative gain

t, y = follow_trajectory(trajectory, kp, ki, kd)
```

In the above code, we create a `follow_trajectory` function that takes the trajectory to follow and the gains of the PID controller as inputs. It creates transfer functions for the system and the PID controller using the `control` module. The closed-loop transfer function is obtained by multiplying the controller and system transfer functions. Finally, we simulate the response using the `step_response` function from the `control` module.

By adjusting the PID gains, we can achieve better tracking performance and reduce errors between the system output and the desired trajectory.

## Conclusion

Trajectory generation and following are essential tasks in control systems. In this blog post, we have explored how to generate trajectories using polynomials and spline interpolation in Python. We have also demonstrated how to implement trajectory following using PID control. By applying these techniques, you can design control systems that accurately track desired trajectories in various applications.

#Python #ControlSystem