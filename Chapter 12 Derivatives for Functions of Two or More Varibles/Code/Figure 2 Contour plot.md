```matlab
% Define the x and y ranges
x = linspace(-5, 5, 100);
y = linspace(-5, 5, 100);

% Create a grid of x and y values
[X,Y] = meshgrid(x, y);

% Compute the corresponding z values
Z = X.^2 + Y.^2;

% Create a contour plot of the function
figure;
contour(X, Y, Z);

% Add labels and title
xlabel('x');
ylabel('y');
title('Contour plot of z = x^2 + y^2');

```

This code creates a contour plot of the function using the `contour` function. The `linspace` function is used to create a range of values for x and y, and the `meshgrid` function is used to create a grid of x and y values. The `.^` operator is used to perform element-wise exponentiation of X and Y.

The concept of level curves is closely related to contour plots. Level curves are simply the curves that correspond to constant values of z. In other words, they are the curves where z = constant. In the case of the function z = x^2 + y^2, the level curves are circles centered at the origin, since the value of z only depends on the distance from the origin.

In the contour plot, each contour line represents a different level curve, with the values of z increasing as you move outward from the origin. The contour lines are labeled with their corresponding z-values to make it clear which level curve they represent.