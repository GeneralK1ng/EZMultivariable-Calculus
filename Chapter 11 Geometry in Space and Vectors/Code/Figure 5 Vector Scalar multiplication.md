```matlab
% Define the vector v
v = [1 2];

% Define the scalar k
k = 2;

% Compute the scalar product kv
kv = k*v;

% Visualize the vectors using a quiver plot
quiver(0, 0, v(1), v(2), 'LineWidth', 2);
hold on;
quiver(0, 0, kv(1), kv(2), 'r', 'LineWidth', 2);
axis equal;
xlim([-5 5]);
ylim([-5 5]);
xlabel('x');
ylabel('y');
title('Scalar Multiplication');
grid on;
legend('v', 'kv');

```

This code defines a 2D vector v and a scalar k, and then computes the scalar product kv. The resulting vector is then visualized using the `quiver` function, which plots the vectors as arrows on a 2D graph. The original vector v is plotted in blue, and the scaled vector kv is plotted in red.