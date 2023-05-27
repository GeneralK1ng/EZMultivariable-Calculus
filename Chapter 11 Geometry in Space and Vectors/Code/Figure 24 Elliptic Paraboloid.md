```matlab
% Define the semi-major and semi-minor axes of the ellipse base
a = 2;
b = 1;

% Define the range of x and y values
x = linspace(-5, 5, 50);
y = linspace(-5, 5, 50);
[X, Y] = meshgrid(x, y);

% Calculate the z coordinate of the elliptic paraboloid
Z = (X.^2/a^2) + (Y.^2/b^2);

% Create the 3D plot
figure;
surf(X, Y, Z, 'EdgeColor', 'none');
axis equal;
view(3);
xlabel('x');
ylabel('y');
zlabel('z');
title('Elliptic Paraboloid');

```

In this code, we define the semi-major and semi-minor axes of the ellipse base as `a` and `b`, respectively. We also create a range of `x` and `y` values using `linspace`. We then use `meshgrid` to create a 2D grid of `X` and `Y` values, and we calculate the z coordinate of the elliptic paraboloid using the standard equation for an elliptic paraboloid. We use `surf` to plot the elliptic paraboloid and `axis equal` to ensure that the x, y, and z axes have the same scale. 