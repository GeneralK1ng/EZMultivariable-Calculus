```matlab
% Define the time range
t = linspace(0, 2, 100);

% Define the initial position and velocity of the ball
x0 = 0;
y0 = 0;
z0 = 0;
v0 = 10; % initial velocity

% Define the acceleration due to gravity
g = 9.81; % m/s^2

% Define the position function as a vector-valued function
x = x0 + v0.*cos(pi/4).*t;
y = y0 + v0.*sin(pi/4).*t;
z = z0 + v0.*sin(pi/4).*t - 0.5.*g.*t.^2;

% Create the 3D plot
figure;
plot3(x,y,z,'LineWidth',2);
grid on;
xlabel('x (m)');
ylabel('y (m)');
zlabel('z (m)');
title('3D Plot of a ball being thrown in the air');

```

In this code, we first define the time range `t`. We then define the initial position and velocity of the ball (`x0`, `y0`, `z0`, and `v0`). We also define the acceleration due to gravity `g`. We then define the position function `x`, `y`, and `z` as vector-valued functions, where `x` and `y` represent the horizontal position of the ball (which is constant in this example), and `z` represents the vertical position of the ball, which changes over time due to the acceleration due to gravity. We use these position values to create a 3D plot using the `plot3` function, and label the axes using `xlabel`, `ylabel`, and `zlabel`. 