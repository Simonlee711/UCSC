


clear all
close all
close all
set(groot,'defaultAxesTickLabelInterpreter','latex')
set(groot,'defaulttextinterpreter','latex')
set(groot,'defaultLegendInterpreter','latex')


ax=-2;
ay=-2;
az=-2;
bx=2;
by=2;
bz=2;


f1=@(x,y,z) -1.*x-1.*y-3.*z;
f2=@(x,y,z) -6.*x+1.*y;
f3=@(x,y,z) 0.*x+1.*y+2.*z;

% fun3d=@(t,y)[(3*y(1)-4*y(2)+1*y(3)) ;...
%     (1*y(1)-1*y(2));...
%     (2*y(1)-8*y(2)+2*y(3))]

Nx1=10; 
Ny1=10;
Nz1=10;
xx1=linspace(ax,bx,Nx1);
yy1=linspace(ay,by,Ny1);
zz1=linspace(az,bz,Nz1);
[X1,Y1,Z1]=meshgrid(xx1,yy1,zz1);

% This grid is computing/plotting nullclines and trajectories
Nx=100; 
Ny=100;
Nz=100;
xx=linspace(ax,bx,Nx);
yy=linspace(ay,by,Ny);
zz=linspace(az,bz,Nz);
[X,Y,Z]=meshgrid(xx,yy,zz);


tspan=0:0.01:1;

% for i=ax-2:0.5:bx+2
%     for j=ay-2:0.5:by+2
%         for k=az-2:0.5:bz+2
% 
% [t,y] = ode45(@fun3d,tspan,[i; j; k]);
% 
% plot3(y(:,1),y(:,2),y(:,3),'Linewidth',0.1,'HandleVisibility','off');    % 3D plot of trajectory
% 
% hold on
%         end
%     end
% end
axis([ax bx ay by az bz])


% clf
% hold
% grid
hold on
% Here we plot the nullclines (surfaces in 3D)

p1 = patch(isosurface(X, Y, Z, f1(X,Y,Z), 0));
p2 = patch(isosurface(X, Y, Z, f2(X,Y,Z), 0));
p3 = patch(isosurface(X, Y, Z, f3(X,Y,Z), 0));
hold on
isonormals(X,Y,Z,f1(X,Y,Z),p1)
set(p1, 'FaceColor', 'red', 'EdgeColor', 'none','FaceAlpha',0.2);
isonormals(X,Y,Z,f2(X,Y,Z),p2)
set(p2, 'FaceColor', 'blue', 'EdgeColor', 'none','FaceAlpha',0.2);
isonormals(X,Y,Z,f3(X,Y,Z),p3)
set(p3, 'FaceColor', 'green', 'EdgeColor', 'none','FaceAlpha',0.2);



% Initial condition for the trajectories 
p  = haltonset(3,'Skip',1e3,'Leap',1e2);
p  = scramble(p,'RR2');
X0 = net(p,2000);
X0(:,1)= ax-1 + (bx-ax+2)*X0(:,1);
X0(:,2)= ay-1 + (by-ay+2)*X0(:,2);
X0(:,3)= az-1 + (bz-az+2)*X0(:,3);

streamline(X,Y,Z,f1(X,Y,Z),f2(X,Y,Z),f3(X,Y,Z),X0(:,1),X0(:,2),X0(:,3),[5e-3,1e4])


% Here we plot the velocity field 
hold on
quiver3(X1,Y1,Z1,f1(X1,Y1,Z1),f2(X1,Y1,Z1),f3(X1,Y1,Z1),1,'k','Linewidth',1)
axis([ax bx ay by az bz])

legend('$\dot{x}=0$','$\dot{y}=0$','$\dot{z}=0$');
xlabel('$x$','Interpreter','Latex','Fontsize',20)
ylabel('$y$','Interpreter','Latex','Fontsize',20)
zlabel('$z$','Interpreter','Latex','Fontsize',20)
view(-30,30)
set(gca,'Fontsize',25)
axis tight







% end

