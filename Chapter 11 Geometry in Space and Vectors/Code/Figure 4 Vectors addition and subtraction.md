```matlab
% Define the vectors v and w
v = [1 2];
w = [3 -1];

% Compute the sum vector u
u = v + w;

% Plot the vectors as arrows
quiver(0, 0, v(1), v(2), 'b', 'LineWidth', 2);
hold on;
quiver(v(1), v(2), w(1), w(2), 'r', 'LineWidth', 2);
quiver(0, 0, u(1), u(2), 'g', 'LineWidth', 2);

% Set the axis limits and labels
axis equal;
xlim([-1 5]);
ylim([-3 3]);
xlabel('x');
ylabel('y');
title('Vector Addition');

% Show the grid and legend
grid on;
legend('v', 'w', 'v + w');

```

This code defines two vectors v and w, computes their sum vector u, and then uses the `quiver` function to draw the vectors as arrows on a 2D graph. The resulting graph shows the vectors v, w, and u as blue, red, and green arrows, respectively. The legend indicates which arrow corresponds to which vector.