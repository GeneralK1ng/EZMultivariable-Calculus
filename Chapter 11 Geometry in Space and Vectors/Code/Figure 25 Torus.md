```matlab 
% Define the radius of the torus
R = 3; % Major radius
r = 1; % Minor radius

% Define the range of theta and phi values
theta = linspace(0, 2*pi, 50); % Azimuthal angle
phi = linspace(0, 2*pi, 50); % Polar angle
[theta, phi] = meshgrid(theta, phi);

% Calculate the x, y, and z coordinates of the torus
x = (R + r*cos(phi)).*cos(theta);
y = (R + r*cos(phi)).*sin(theta);
z = r*sin(phi);

% Create the 3D plot
figure;
surf(x, y, z, 'EdgeColor', 'none');
axis equal;
view(3);
xlabel('x');
ylabel('y');
zlabel('z');
title('Torus');

```

In this code, we define the major radius `R` and the minor radius `r` of the torus. We then create a range of `theta` and `phi` values using `linspace` and use `meshgrid` to create a 2D grid of these values. We calculate the x, y, and z coordinates of the torus using the standard parametric equations for a torus. We use `surf` to plot the torus and `axis equal` to ensure that the x, y, and z axes have the same scale. 