```matlab
% Define the time range
t = linspace(0, 2*pi, 100);

% Define the position functions x, y, and z
x = sin(t);
y = cos(t);
z = t;

% Define the velocity vector
vx = cos(t);
vy = -sin(t);
vz = ones(size(t));

% Define the acceleration vector
ax = -sin(t);
ay = -cos(t);
az = zeros(size(t));

% Calculate the tangent vector
tangent = [vx; vy; vz];
tangent = tangent./vecnorm(tangent);

% Calculate the normal vector
normal = cross([vx; vy; vz],[ax; ay; az]);
normal = normal./vecnorm(normal);

% Calculate the binormal vector
binormal = cross(tangent, normal);

% Create the 3D plot
figure;
plot3(x,y,z,'LineWidth',2);
hold on;
quiver3(x,y,z,tangent(1,:),tangent(2,:),tangent(3,:),0.5,'LineWidth',2,'color','r');
quiver3(x,y,z,normal(1,:),normal(2,:),normal(3,:),0.5,'LineWidth',2,'color','g');
quiver3(x,y,z,binormal(1,:),binormal(2,:),binormal(3,:),0.5,'LineWidth',2,'color','b');
grid on;
xlabel('x');
ylabel('y');
zlabel('z');
title('TNB Frame of a Curve');
legend('Curve','Tangent Vector','Normal Vector','Binormal Vector');

```

In this code, we first define the time range `t`. We then define the position functions `x`, `y`, and `z` as a curve's path in 3D space. We also define the velocity and acceleration vectors `vx`, `vy`, `vz`, `ax`, `ay`, and `az`, which represent the curve's velocity and acceleration vectors at each point along the path. We use the `plot3` function to create a 3D plot of the curve's path, and the `quiver3` function to create arrows that represent the TNB vectors at each point along the path. We use the `hold on` function to keep the path plot and the vector plots in the same figure. Finally, we label the axes using `xlabel`, `ylabel`, and `zlabel`, add a grid using `grid on`, and add a legend using `legend`. 