```matlab
% Define center and radius of sphere
center = [1, 2, 3];
radius = 2;

% Define coordinates of sphere surface
theta = linspace(0, 2*pi, 100);
phi = linspace(0, pi, 100);
[THETA, PHI] = meshgrid(theta, phi);
x = center(1) + radius*sin(PHI).*cos(THETA);
y = center(2) + radius*sin(PHI).*sin(THETA);
z = center(3) + radius*cos(PHI);

% Create 3D plot of sphere
figure;
surf(x, y, z, 'FaceAlpha', 0.5);
axis equal;
xlabel('x');
ylabel('y');
zlabel('z');
title('Sphere with center (1, 2, 3) and radius 2');

```

