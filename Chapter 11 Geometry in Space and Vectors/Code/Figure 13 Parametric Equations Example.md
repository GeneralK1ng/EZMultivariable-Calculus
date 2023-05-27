```matlab
% Define the time range
t = 0:0.1:10*pi;

% Define the x, y, and z values
x = cos(t);
y = sin(t);
z = t;

% Create the 3D plot
figure;
plot3(x,y,z,'LineWidth',2);
grid on;
xlabel('x(t)');
ylabel('y(t)');
zlabel('z(t)');
title('3D Plot of x(t) = cos(t), y(t) = sin(t), z(t) = t');

```

This will create a 3D plot of the function, with x(t) as the x-axis, y(t) as the y-axis, and z(t) as the z-axis. The `xlabel`, `ylabel`, and `zlabel` functions are used to label the axes, and the `title` function is used to give the plot a title. The `grid on` function is used to add a grid to the plot for clarity. 