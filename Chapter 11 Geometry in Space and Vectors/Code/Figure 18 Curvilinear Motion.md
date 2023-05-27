```matlab
% Define the time range
t = linspace(0, 2*pi, 100);

% Define the position functions x, y, and z
x = 3*sin(2*t);
y = 3*cos(2*t);
z = t;

% Define the velocity functions vx, vy, and vz
vx = 6*cos(2*t);
vy = -6*sin(2*t);
vz = ones(size(t));

% Define the acceleration functions ax, ay, and az
ax = -12*sin(2*t);
ay = -12*cos(2*t);
az = zeros(size(t));

% Create the 3D plot
figure;
plot3(x,y,z,'LineWidth',2);
hold on;
quiver3(x,y,z,vx,vy,vz,0.5,'LineWidth',2);
quiver3(x,y,z,ax,ay,az,0.5,'LineWidth',2);
grid on;
xlabel('x');
ylabel('y');
zlabel('z');
title('3D Plot of Curvilinear Motion');
legend('Path','Velocity Vectors','Acceleration Vectors');

```

In this code, we first define the time range `t`. We then define the position functions `x`, `y`, and `z` as a particle's path in 3D space. We also define the velocity and acceleration functions `vx`, `vy`, `vz`, `ax`, `ay`, and `az`, which represent the particle's velocity and acceleration vectors at each point along the path. We use the `plot3` function to create a 3D plot of the particle's path, and the `quiver3` function to create arrows that represent the velocity and acceleration vectors at each point along the path. We use the `hold on` function to keep the path plot and the vector plots in the same figure. Finally, we label the axes using `xlabel`, `ylabel`, and `zlabel`, add a grid using `grid on`, and add a legend using `legend`.