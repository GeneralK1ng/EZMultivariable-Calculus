```matlab
% Define two vectors
u = [2 3 1];
v = [-1 4 2];

% Calculate the dot product and the angle between the vectors
dot_uv = dot(u, v);
norm_u = norm(u);
norm_v = norm(v);
cos_theta = dot_uv / (norm_u * norm_v);
theta = acosd(cos_theta);

% Plot the vectors and the angle between them
figure;
quiver3(0, 0, 0, u(1), u(2), u(3), 'b', 'LineWidth', 2);
hold on;
quiver3(0, 0, 0, v(1), v(2), v(3), 'r', 'LineWidth', 2);
axis equal;
xlabel('x');
ylabel('y');
zlabel('z');
title(['Dot product = ', num2str(dot_uv), ', Cosine of angle = ', num2str(cos_theta), ', Angle = ', num2str(theta), ' degrees']);
legend('u', 'v', 'Location', 'best');
view(-30, 30);

% Add a plane to show the projection of u onto v
u_proj = dot_uv / norm_v^2 * v;
patch([0 u(1) u_proj(1) u_proj(1)], [0 u(2) u_proj(2) 0], [0 u(3) u_proj(3) 0], 'g', 'FaceAlpha', 0.2, 'EdgeColor', 'none');

% Add text labels for the vectors and the angle
text(u(1)/2, u(2)/2, u(3)/2, 'u', 'Color', 'b', 'FontSize', 14);
text(v(1)/2, v(2)/2, v(3)/2, 'v', 'Color', 'r', 'FontSize', 14);
text(u_proj(1)/2, u_proj(2)/2, u_proj(3)/2, 'proj_{v}(u)', 'Color', 'g', 'FontSize', 14);
text(u(1)/2, u(2)/2, u(3)/2, ['\theta = ', num2str(theta), '^\circ'], 'Color', 'k', 'FontSize', 14);

```

