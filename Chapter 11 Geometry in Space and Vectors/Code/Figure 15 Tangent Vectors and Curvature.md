```matlab
% Define the time range
t = linspace(0, 2*pi, 100);

% Define the x, y, and z functions
x = cos(t);
y = sin(t);
z = t;

% Define the first derivative functions (the tangent vectors)
dx = -sin(t);
dy = cos(t);
dz = ones(size(t));

% Define the second derivative functions (the curvature vector)
ddx = -cos(t);
ddy = -sin(t);
ddz = zeros(size(t));

% Create the 3D plot
figure;
plot3(x,y,z,'LineWidth',2);
hold on;
quiver3(x,y,z,dx,dy,dz,0.5,'LineWidth',2);
quiver3(x,y,z,ddx,ddy,ddz,1.5,'LineWidth',2);
grid on;
xlabel('x');
ylabel('y');
zlabel('z');
title('3D Plot of Tangent Vectors and Curvature');
legend('Curve','Tangent Vectors','Curvature Vector');

```

In this code, we first define the time range `t`. We then define the x, y, and z functions as a curve in 3D space. We also define the first derivative functions, which represent the tangent vectors along the curve, and the second derivative functions, which represent the curvature vector. We use the `plot3` function to create a 3D plot of the curve, and the `quiver3` function to create arrows that represent the tangent vectors and curvature vector at each point along the curve. We use the `hold on` function to keep the curve plot and the vector plots in the same figure. Finally, we label the axes using `xlabel`, `ylabel`, and `zlabel`, add a grid using `grid on`, and add a legend using `legend`.	