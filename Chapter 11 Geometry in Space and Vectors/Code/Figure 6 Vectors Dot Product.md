```matlab
% Define the vectors v and w
v = [1 2];
w = [3 4];

% Compute the dot product v . w
dot_product = dot(v, w);

% Compute the angle between the vectors
theta = acos(dot_product/(norm(v)*norm(w)));

% Plot the vectors
quiver(0, 0, v(1), v(2), 'LineWidth', 2);
hold on;
quiver(0, 0, w(1), w(2), 'r', 'LineWidth', 2);

% Draw a dotted line between the vectors
plot([v(1) w(1)], [v(2) w(2)], '--k');

% Set the axis limits and labels
axis equal;
xlim([-5 5]);
ylim([-5 5]);
xlabel('x');
ylabel('y');
title('Dot Product');

% Show the legend and angle
legend('v', 'w', 'dot product');
text(0, 2, sprintf('theta = %.2f', theta*180/pi));

```

This code defines two 2D vectors v and w, computes their dot product, and then uses the `quiver` and `plot` functions to draw the vectors and a dotted line between them on a 2D graph. The resulting graph shows the vectors v and w as blue and red arrows, respectively, and the dotted line between them indicates the projection of v onto w. The legend indicates which arrow corresponds to which vector, and also shows the value of the dot product. The angle between the vectors is computed using the `acos` function, and is displayed as text above the graph.

