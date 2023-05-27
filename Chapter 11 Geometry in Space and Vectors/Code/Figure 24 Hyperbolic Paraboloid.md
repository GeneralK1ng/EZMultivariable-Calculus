```matlab
% Define the range of x and y values
x = linspace(-1, 1, 50);
y = linspace(-1, 1, 50);
[X, Y] = meshgrid(x, y);

% Calculate the z coordinate of the hyperbolic paraboloid
Z = X.^2 - Y.^2;

% Create the 3D plot
figure;
surf(X, Y, Z, 'EdgeColor', 'none');
axis equal;
view(3);
xlabel('x');
ylabel('y');
zlabel('z');
title('Hyperbolic Paraboloid');
```

In this code, we create a range of `x` and `y` values using `linspace`. We then use `meshgrid` to create a 2D grid of `X` and `Y` values, and we calculate the z coordinate of the hyperbolic paraboloid using the standard equation for a hyperbolic paraboloid. We use `surf` to plot the hyperbolic paraboloid and `axis equal` to ensure that the x, y, and z axes have the same scale.