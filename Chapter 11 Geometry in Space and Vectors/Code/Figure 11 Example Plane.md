```matlab
% Define the equation of the plane
syms x y z
eqn = 2*x - 3*y + 4*z == 5;

% Create a grid of points in the x-y plane
[X,Y] = meshgrid(-2:0.2:2);

% Solve for the corresponding z-values
Z = (5 - 2*X + 3*Y) / 4;

% Create a new figure and plot the plane
figure
surf(X,Y,Z)
hold on

% Plot the intersection of the plane with the x, y, and z axes
plot3([-2 2], [0 0], [0 0], 'k')
plot3([0 0], [-2 2], [0 0], 'k')
plot3([0 0], [0 0], [-1 2], 'k')

% Label the axes and add a title
xlabel('x')
ylabel('y')
zlabel('z')
title('Example Plane')

```



This code defines the equation of a plane as `2*x - 3*y + 4*z = 5` and creates a grid of points in the x-y plane. It then solves for the corresponding z-values using the equation of the plane and plots the resulting surface using the `surf` function. Finally, it adds three lines to show the intersection of the plane with the x, y, and z axes, and labels the axes and adds a title to the plot.