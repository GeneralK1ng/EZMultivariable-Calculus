```matlab
% Define the two vectors
u = [1, 2, 3];
v = [4, 5, 6];

% Compute the cross product using the determinant formula
w = cross(u, v);

% Plot the vectors and their cross product
quiver3(0, 0, 0, u(1), u(2), u(3), 'b', 'LineWidth', 2);
hold on;
quiver3(0, 0, 0, v(1), v(2), v(3), 'r', 'LineWidth', 2);
quiver3(0, 0, 0, w(1), w(2), w(3), 'g', 'LineWidth', 2);
axis equal;
legend('u', 'v', 'u x v');

```

The resulting plot should show three vectors in 3D space, with labels and a legend indicating which vector is which. The u and v vectors should be shown in blue and red, respectively, and the cross product u x v should be shown in green. The length of the vectors can be adjusted as needed, and the plot can be rotated to see the relationships between the vectors and their cross product from different angles.