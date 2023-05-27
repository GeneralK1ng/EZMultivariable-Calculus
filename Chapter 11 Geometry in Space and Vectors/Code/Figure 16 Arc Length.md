```matlab
% Define the time range
t = linspace(0, 2*pi, 100);

% Define the x, y, and z functions
x = cos(t);
y = sin(t);
z = t;

% Calculate the arc length
dx = diff(x);
dy = diff(y);
dz = diff(z);
ds = sqrt(dx.^2 + dy.^2 + dz.^2);
s = [0 cumsum(ds)];

% Create the 3D plot
figure;
plot3(x,y,z,'LineWidth',2);
hold on;
scatter3(x,y,z,10,s,'filled');
grid on;
xlabel('x');
ylabel('y');
zlabel('z');
title('3D Plot of Arc Length');
cb = colorbar;
cb.Label.String = 'Arc Length';

```

In this code, we first define the time range `t`. We then define the x, y, and z functions as a curve in 3D space. We use the `diff` function to calculate the first derivative of each function, which represents the tangent vector along the curve. We then use the `sqrt` function to calculate the magnitude of the tangent vector at each point along the curve, which represents the arc length. We use the `cumsum` function to add up the arc length values along the curve to get the total arc length `s`. We use the `plot3` function to create a 3D plot of the curve, and the `scatter3` function to create a scatter plot of the same curve with the arc length values as color. We use the `hold on` function to keep the curve plot and the scatter plot in the same figure. Finally, we label the axes using `xlabel`, `ylabel`, and `zlabel`, add a grid using `grid on`, add a title using `title`, and add a colorbar using `colorbar`. 