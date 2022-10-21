close all
clear all

z=1
% f1=@(x,y,z) x.*(3-x-2.*y);
% f2=@(x,y,z) y.*(2-x-y)
% ax=0;ay=0;bx=4;by=4;

% 
% f1=@(x,y,z) x-y;
% f2=@(x,y,z) 1-exp(x)
% ax=-2;ay=-2;bx=2;by=2;

% 
% f1=@(x,y,z) x-x.^3;
% f2=@(x,y,z) -y
% ax=-2;ay=-2;bx=2;by=2;


% 
% 
% f1=@(x,y,z) x.*(x-y);
% f2=@(x,y,z) y.*(2.*x-y)
% ax=-2;ay=-2;bx=2;by=2;


%f1=@(x,y,z) x.*(2-x-y);
%f2=@(x,y,z) x-y
%ax=-2;ay=-2;bx=2;by=2;


% f1=@(x,y,z)sin(y);
% f2=@(x,y,z) x-x.^3
% ax=-2;ay=-8;bx=2;by=8;

f1=@(x,y,z) cos(x)-y
f2=@(x,y,z) y.*sin(x)
ax=-4;ay=-4;bx=4;by=4;


Nx1=20; 
Ny1=20;
xx1=linspace(ax,bx,Nx1);
yy1=linspace(ay,by,Ny1);
[X1,Y1]=meshgrid(xx1,yy1);

%%
Nx=200; 
Ny=200;
xx=linspace(ax,bx,Nx);
yy=linspace(ay,by,Ny);
[X,Y]=meshgrid(xx,yy);

fontsize=16;
figure(1)
clf
hold
box on

% 
[Cx,hx]=contour(X,Y,f1(X,Y,z),[0 0],'r','Linewidth',0.5); % nullcline dx/dt=0
[Cy,hy]=contour(X,Y,f2(X,Y,z),[0 0],'k','Linewidth',0.5); % nullcline dy/dt=0


%% the trajectories 
hold on
X0 = rand(400,2);
X0(:,1)= ax + (bx-ax)*X0(:,1);
X0(:,2)= ay + (by-ay)*X0(:,2);

streamline(X,Y,f1(X,Y,z),f2(X,Y,z),X0(:,1),X0(:,2),[5e-3,1e4])



xlabel('$x$','Interpreter','Latex','Fontsize',20)
ylabel('$y$','Interpreter','Latex','Fontsize',20)
set(gca,'Fontsize',25)
axis tight
grid on

%% velocity field 
quiver(X1,Y1,f1(X1,Y1,z),f2(X1,Y1,z),'k','Linewidth',1.5,'MaxHeadSize',3)
grid on
axis([ax bx ay by])

leg=legend('$\dot{x_{1}}=0$','$\dot{x_{2}}=0$','Fontsize',20);
set(leg,'Interpreter','Latex')