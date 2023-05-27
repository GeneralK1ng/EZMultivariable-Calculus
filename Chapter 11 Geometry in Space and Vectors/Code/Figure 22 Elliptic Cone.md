```matlab
% Define the semi-major and semi-minor axes of the ellipse base
a = 2;
b = 1;

% Define the range of z and theta values
z = linspace(-5, 5, 50);
theta = linspace(0, 2*pi, 50);
[Z, THETA] = meshgrid(z, theta);

% Calculate the x, y, and z coordinates of the elliptic cone
x = a*Z.*cos(THETA);
y = b*Z.*sin(THETA);
z = Z;

% Create the 3D plot
figure;
surf(x, y, z, 'EdgeColor', 'none');
axis equal;
view(3);
xlabel('x');
ylabel('y');
zlabel('z');
title('Elliptic Cone');

```

In this code, we define the semi-major and semi-minor axes of the ellipse base as `a` and `b`, respectively. We also create a range of `z` and `theta` values using `linspace`. We then use `meshgrid` to create a 2D grid of `Z` and `THETA` values, and we calculate the x, y, and z coordinates of the elliptic cone using the standard parametric equations for an elliptic cone. We use `surf` to plot the elliptic cone and `axis equal` to ensure that the x, y, and z axes have the same scale. 