```matlab
% Define the x and y ranges
x = linspace(-5, 5, 100);
y = linspace(-5, 5, 100);

% Create a grid of x and y values
[X,Y] = meshgrid(x, y);

% Compute the corresponding z values
Z = X.^2 + Y.^2;

% Create a 3D plot of the function
figure;
surf(X, Y, Z);

% Add labels and title
xlabel('x');
ylabel('y');
zlabel('z');
title('z = x^2 + y^2');

```

This code creates a 3D surface plot of the function using the `surf` function. The `linspace` function is used to create a range of values for x and y, and the `meshgrid` function is used to create a grid of x and y values. The `.^` operator is used to perform element-wise exponentiation of X and Y. The `xlabel`, `ylabel`, `zlabel`, and `title` functions are used to add labels and a title to the plot.