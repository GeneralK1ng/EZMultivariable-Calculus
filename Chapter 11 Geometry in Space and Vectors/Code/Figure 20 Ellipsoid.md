```matlab
% Define the radii of the ellipsoid
a = 2;
b = 3;
c = 4;

% Define the range of u, v, and theta angles
u = linspace(0, pi, 50);
v = linspace(0, 2*pi, 50);
[theta, phi] = meshgrid(u, v);

% Calculate the x, y, and z coordinates of the ellipsoid
x = a*sin(theta).*cos(phi);
y = b*sin(theta).*sin(phi);
z = c*cos(theta);

% Create the 3D plot
figure;
surf(x, y, z, 'EdgeColor', 'none');
axis equal;
view(3);
xlabel('x');
ylabel('y');
zlabel('z');
title('Ellipsoid');

```

In this code, we define the radii of the ellipsoid as `a`, `b`, and `c`, and we create a range of `u`, `v`, and `theta` angles using `linspace`. We then use `meshgrid` to create a 2D grid of `theta` and `phi` angles, and we calculate the x, y, and z coordinates of the ellipsoid using the standard parametric equations for an ellipsoid. We use `surf` to plot the ellipsoid and `axis equal` to ensure that the x, y, and z axes have the same scale. 