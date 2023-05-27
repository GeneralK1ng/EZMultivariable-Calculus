```matlab
% Define a vector with components (1, 2, 3)
v = [1 2 3];

% Calculate the directional angles and cosines
theta_x = acosd(v(1)/norm(v)); % angle with respect to x-axis
theta_y = acosd(v(2)/norm(v)); % angle with respect to y-axis
theta_z = acosd(v(3)/norm(v)); % angle with respect to z-axis
cos_x = v(1)/norm(v); % cosine of angle with respect to x-axis
cos_y = v(2)/norm(v); % cosine of angle with respect to y-axis
cos_z = v(3)/norm(v); % cosine of angle with respect to z-axis

% Define a unit sphere
[x,y,z] = sphere;

% Create a 3D plot
figure;
surf(x,y,z,'FaceAlpha',0.1,'EdgeAlpha',0.3);
hold on;

% Plot the vector v
quiver3(0,0,0,v(1),v(2),v(3),'LineWidth',2,'Color','red');

% Plot lines indicating the angles with respect to each axis
plot3([0 v(1)],[0 0],[0 0],'--k','LineWidth',1);
plot3([0 0],[0 v(2)],[0 0],'--k','LineWidth',1);
plot3([0 0],[0 0],[0 v(3)],'--k','LineWidth',1);

% Add labels to the plot
xlabel('x');
ylabel('y');
zlabel('z');
title('Relationship between Azimuth Angle and Cosine');

% Add text annotations for the angles and cosines
text(v(1),0,0,['\theta_x = ' num2str(theta_x) '^o'],'FontSize',10);
text(0,v(2),0,['\theta_y = ' num2str(theta_y) '^o'],'FontSize',10);
text(0,0,v(3),['\theta_z = ' num2str(theta_z) '^o'],'FontSize',10);
text(v(1),v(2),v(3),['\cos \theta_x = ' num2str(cos_x)],'FontSize',10);
text(v(1),v(2),v(3)+0.2,['\cos \theta_y = ' num2str(cos_y)],'FontSize',10);
text(v(1)+0.2,v(2),v(3),['\cos \theta_z = ' num2str(cos_z)],'FontSize',10);

```

This code will create a 3D plot with the vector `v` represented as a red arrow, and lines indicating the angles with respect to each axis. 