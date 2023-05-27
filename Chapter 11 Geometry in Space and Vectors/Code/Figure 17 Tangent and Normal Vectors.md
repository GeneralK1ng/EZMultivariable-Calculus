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

% Calculate the magnitude of the tangent vectors
ds = sqrt(dx.^2 + dy.^2 + dz.^2);

% Normalize the tangent vectors to get the unit tangent vectors
tx = dx ./ ds;
ty = dy ./ ds;
tz = dz ./ ds;

% Define the second derivative functions (the curvature vector)
ddx = -cos(t);
ddy = -sin(t);
ddz = zeros(size(t));

% Calculate the cross product of the tangent vectors and the curvature vector to get the normal vectors
nx = ty .* ddz - tz .* ddy;
ny = tz .* ddx - tx .* ddz;
nz = tx .* ddy - ty .* ddx;

% Create the 3D plot
figure;
plot3(x,y,z,'LineWidth',2);
hold on;
quiver3(x,y,z,tx,ty,tz,0.5,'LineWidth',2);
quiver3(x,y,z,nx,ny,nz,0.5,'LineWidth',2);
grid on;
xlabel('x');
ylabel('y');
zlabel('z');
title('3D Plot of Unit Tangent and Normal Vectors');
legend('Curve','Unit Tangent Vectors','Unit Normal Vectors');

```

In this code, we first define the time range `t`. We then define the x, y, and z functions as a curve in 3D space. We also define the first and second derivative functions, which represent the tangent and curvature vectors, respectively. We use the `sqrt` function to calculate the magnitude of the tangent vectors, and divide the derivative functions by the magnitude to get the unit tangent vectors. We calculate the cross product of the unit tangent vectors and the curvature vector to get the unit normal vectors. We use the `plot3` function to create a 3D plot of the curve, and the `quiver3` function to create arrows that represent the unit tangent and normal vectors at each point along the curve. We use the `hold on` function to keep the curve plot and the vector plots in the same figure. Finally, we label the axes using `xlabel`, `ylabel`, and `zlabel`, add a grid using `grid on`, and add a legend using `legend`. 