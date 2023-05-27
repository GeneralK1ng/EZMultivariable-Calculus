```matlab
% Define the vectors v and w
v = [1 2 0];
w = [3 4 0];

% Compute the cross product v x w
cross_product = cross(v, w);

% Plot the vectors
quiver3(0, 0, 0, v(1), v(2), v(3), 'LineWidth', 2);
hold on;
quiver3(0, 0, 0, w(1), w(2), w(3), 'r', 'LineWidth', 2);
quiver3(0, 0, 0, cross_product(1), cross_product(2), cross_product(3), 'g', 'LineWidth', 2);

% Set the axis limits and labels
axis equal;
xlim([-5 5]);
ylim([-5 5]);
zlim([-5 5]);
xlabel('x');
ylabel('y');
zlabel('z');
title('Cross Product');

% Show the legend
legend('v', 'w', 'v x w');

```

This code defines two 3D vectors v and w in the x-y plane, computes their cross product, and then uses the `quiver3` function to draw the vectors as arrows in 3D space. The resulting graph shows the vectors v, w, and v x w as blue, red, and green arrows, respectively. The legend indicates which arrow corresponds to which vector.