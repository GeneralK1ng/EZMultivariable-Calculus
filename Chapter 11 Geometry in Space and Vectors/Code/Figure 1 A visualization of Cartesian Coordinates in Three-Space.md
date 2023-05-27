```matlab
% Clear the workspace and the command window
clear;
clc;

% Define the limits of the coordinate system
xlim([-3 3]);
ylim([-3 3]);
zlim([-3 3]);

% Set the aspect ratio and the view angle of the coordinate system
daspect([1 1 1]);
view(45, 30);

% Draw the x, y, and z-axes
line([0 3], [0 0], [0 0], 'Color', 'black', 'LineWidth', 2);
line([0 0], [0 3], [0 0], 'Color', 'black', 'LineWidth', 2);
line([0 0], [0 0], [0 3], 'Color', 'black', 'LineWidth', 2);

% Label the x, y, and z-axes
text(3, 0, 0, 'x', 'FontSize', 14, 'FontWeight', 'bold');
text(0, 3, 0, 'y', 'FontSize', 14, 'FontWeight', 'bold');
text(0, 0, 3, 'z', 'FontSize', 14, 'FontWeight', 'bold');

% Draw the xy, yz, and xz-planes
patch([-3 3 3 -3], [-3 -3 3 3], [0 0 0 0], 'g', 'FaceAlpha', 0.2);
patch([0 0 0 0], [-3 3 3 -3], [-3 -3 3 3], 'y', 'FaceAlpha', 0.2);
patch([-3 3 3 -3], [0 0 0 0], [-3 -3 3 3], 'm', 'FaceAlpha', 0.2);

% Label the xy, yz, and xz-planes
text(2, 2, 0, 'xy-plane', 'FontSize', 14, 'FontWeight', 'bold', 'Color', 'g');
text(0, 2, 2, 'yz-plane', 'FontSize', 14, 'FontWeight', 'bold', 'Color', 'y');
text(2, 0, 2, 'xz-plane', 'FontSize', 14, 'FontWeight', 'bold', 'Color', 'm');

% Label the trigonometric limits
text(-0.2, 0.2, 0, '0', 'FontSize', 14, 'FontWeight', 'bold');
text(3.2, -0.2, 0, '\pi', 'FontSize', 14, 'FontWeight', 'bold');
text(-0.2, 3.2, 0, '\pi', 'FontSize', 14, 'FontWeight', 'bold');
text(-0.2, -0.2, 3.2, '\pi', 'FontSize', 14, 'FontWeight', 'bold');

```

