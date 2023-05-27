```matlab
% Define two vectors
u = [1, 2, 3];
v = [2, 0, 1];

% Compute the projection of u onto v
proj_v_u = dot(u, v) / dot(v, v) * v;

% Plot the vectors and their projection
quiver3(0, 0, 0, u(1), u(2), u(3), 'LineWidth', 2);
hold on;
quiver3(0, 0, 0, v(1), v(2), v(3), 'LineWidth', 2);
quiver3(0, 0, 0, proj_v_u(1), proj_v_u(2), proj_v_u(3), 'LineWidth', 2, 'LineStyle', '--');
legend('u', 'v', 'proj_v u');
axis equal;

```

This code first defines two vectors `u` and `v`, and then computes the projection of `u` onto `v` using the formula we discussed earlier. It then uses the `quiver3` function to plot the vectors and their projection in 3D space. The `legend` function is used to label the vectors, and `axis equal` ensures that the axes are scaled equally.