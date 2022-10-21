close all
clear all


z=1
ax=-2;
ay=-2;
bx=2;
by=2;
% f1=@(x,y,z) 4.*x-y;
% f2=@(x,y,z) 2.*x+y;
% A=[4 -1;2 1]

% f1=@(x,y,z) 1.*x-y;
% f2=@(x,y,z) 1.*x+y;
% A=[1 -1;1 1]

% f1=@(x,y,z) y;
% f2=@(x,y,z) -2.*x-3.*y;
% A=[0 1;-2 -3]
% 


% f1=@(x,y,z) 5.*x+10.*y;
% f2=@(x,y,z) -1.*x-1.*y;
% A=[5 10;-1 -1]

f1=@(x,y,z) -x-2.*y;
f2=@(x,y,z) -x;
A=[2 -2;2 -2]

% 
% 
% f1=@(x,y,z) -3.*x+2.*y;
% f2=@(x,y,z) 1.*x-2.*y;
% A=[-3 2;1 -2]

% f1=@(x,y,z) -3.*x+4.*y;
% f2=@(x,y,z) -2.*x+3.*y;
% A=[-3 4;-2 3]


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

hold on
xx=-2:.2:2
xlength=length(xx)
[Evec Eval]=eig(A)

if (Evec(1,1)==0 & Evec(1,2)~=0)  
line([0 0],[-2 2],'Color','green','LineWidth',1)
hold on
plot(xx,xx.*(Evec(2,2)/Evec(1,2)),'Color','green','LineWidth',1)
hold on
elseif (Evec(1,2)==0 & Evec(1,1)~=0)
line([0 0],[-2 2],'Color','green','LineWidth',1)
hold on
plot(xx,xx.*(Evec(2,1)/Evec(1,1)),'Color','green','LineWidth',1)
hold on
elseif (Evec(1,1)==0 & Evec(1,2)==0)
line([0 0],[-2 2],'Color','green','LineWidth',1)
hold on
else
    hold on
plot(xx,xx.*(Evec(2,2)/Evec(1,2)),'Color','green','LineWidth',2)   
hold on
plot(xx,xx.*(Evec(2,1)/Evec(1,1)),'Color','green','LineWidth',2)
end



%% the trajectories 

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
axis([-2 2 -2 2])

leg=legend('$\dot{x_{1}}=0$','$\dot{x_{2}}=0$','eigenvalues','Fontsize',20);
set(leg,'Interpreter','Latex')