```matlab
% Define the radii of the hyperboloid
a = 2;
b = 3;
c = 4;

% Define the range of u and v angles
u = linspace(-pi, pi, 50);
v = linspace(0, 2*pi, 50);
[theta, phi] = meshgrid(u, v);

% Calculate the x, y, and z coordinates of the hyperboloid
x = a*sinh(theta).*cos(phi);
y = b*sinh(theta).*sin(phi);
z = c*cosh(theta);

% Create the 3D plot
figure;
surf(x, y, z, 'EdgeColor', 'none');
axis equal;
view(3);
xlabel('x');
ylabel('y');
zlabel('z');
title('Hyperboloid of Two Sheets');

```

In this code, we define the radii of the hyperboloid as `a`, `b`, and `c`, and we create a range of `u` and `v` angles using `linspace`. We then use `meshgrid` to create a 2D grid of `theta` and `phi` angles, and we calculate the x, y, and z coordinates of the hyperboloid using the standard parametric equations for a hyperboloid of two sheets. We use `surf` to plot the hyperboloid and `axis equal` to ensure that the x, y, and z axes have the same scale. 