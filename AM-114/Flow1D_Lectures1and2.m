clear
close all
set(groot,'defaultAxesTickLabelInterpreter','latex')
set(groot,'defaulttextinterpreter','latex')
set(groot,'defaultLegendInterpreter','latex')

%Please follow the instruction given in the comment

%fixp=[0;sqrt(7/2);-sqrt(7/2)] % Enter your Fixed points, If you do not have your fixed points yet, uncomment the next line

  fixp=[]  % If you do not know any of the fixed points uncomment this line

%fun=@(t,x) 3.*x.^3+7/4.*x-x.^5; % Define your function
%fun=@(t,x) 2.*x + x.^3 - x.^5; % assignment 1 problem 1 equation 2
%fun=@(t,x) sin(x).*(x.^2 - 5.*x + 6.) % assignment 1 problem 1 equation 3
fun=@(t,x) log(x.^2+1)-1 %assignment 1 problem 1 equation 1

at=0;bt=2;ax=-2;bx=5;    %!!! Change X-axis here!!!
x=[ax:0.1:bx]; % The x  interval for the trajectory plot(figure(1) and figure(2))
tspan=[at:0.05:bt] ;% The x  interval for the trajectory plot(figure(1) and figure(2))
x0=[-2,-0.3,0.3,-0.7,1,2,0.6,0,1.6] % Different Initial conditions for trajectory plot (figure(1))

xinit=-3:0.1:3; % Vector of Initial conditions for ploting the flow map vs x0 (figure(3))
tspanFlowMap=0:0.1:5.42 % Vector of Time for ploting the flow map vs x0 (figure(3))


%% Plotting the vector field

% fun=@(t,x) 3.*x.^3+7/4.*x-x.^5;  %defin the function



[t, xgrid] = meshgrid(tspan, x);
dxdt=fun(0,xgrid);
L = sqrt(1 + dxdt.^2); %define the length of the curve just for scaling
%  L =ones(size(xgrid));

quiver(t, xgrid, 1./L, dxdt./L, 0.7); % quiver(X,Y,U,V)
X0 = rand(400,2);
X0(:,1)= at + (bx-at)*X0(:,1);
X0(:,2)= ax + (bx-ax)*X0(:,2);
streamline(t, xgrid, 1./L, dxdt./L, X0(:,1),X0(:,2),[5e-3,1e4])
axis tight; 
set(gca,'FontSize',20)
xlabel('$t$','FontSize',22,'Interpreter','latex')
ylabel('$y$','FontSize',22,'Interpreter','latex')
title("Trajectories with different initial conditions")
axis([at bt ax bx])
k=1
% X=zeros(length(tspan),4)
%% Plotting the system trajectory
for i=1:length(x0)
[t,x_ode] = ode45(@(t,x)fun(t,x),tspan,x0(i));
X(:,k)=x_ode
hold on
p1=plot(t,X(:,k),'LineWidth',4);
xlabel('t','FontSize',12);
ylabel('x(t)','FontSize',12);
k=k+1
end
set(gca,'FontSize',20)

% x=[-5:0.1:5] 
% tspan=[0:0.05:2] 




%% Plotting the phase space
figure(2)
plot(x, fun(0,x),'linewidth',2)

if (isempty(fixp)==0)
for i=1:length(fixp)
hold on
plot(fixp(i), 0,'* c','MarkerSize',20,'MarkerFaceColor','c')
end
end
grid on
set(gca,'FontSize',20)
xlabel('$x$','FontSize',22,'Interpreter','latex')
ylabel('$f(x)$','FontSize',22,'Interpreter','latex')
%% Plotting the Flow map
figure(3)
l1=length(tspanFlowMap);
l2=length(xinit);
Times=[1,floor(l1/10),floor(l1/5),floor(l1/3),floor(l1/2),floor(l1)];
l3=length(Times);
Xinit=zeros(l2,l3);


for i= 1:length(xinit)
[t,x_ode] = ode45(@(t,x)fun(t,x), tspan,xinit(i));
% X(i,:)=x_ode
for j=1:l3;
Xinit(i,j)=x_ode(j); 
end
p1=plot(xinit,Xinit(:,1),'g','LineWidth',2);
end

for j=1:l3;
plot(xinit,Xinit(:,j),'LineWidth',2,'DisplayName',['$t=$',num2str(tspanFlowMap(Times(j))),'s']);
hold on
end
set(gca,'FontSize',20)
ylabel('$\mathcal{X}(x_0,t)$','FontSize',22,'Interpreter','latex')
xlabel('$x_0$','FontSize',22,'Interpreter','latex')
legend('show','FontSize',20)


if (isempty(fixp)==0)
for i=1:length(fixp)
hold on
plot(xinit,fixp(i)*ones(1,l2),'k--','LineWidth',2,'HandleVisibility','off');
hold on
plot(fixp(i)*ones(1,l2),xinit,'k--','LineWidth',2,'HandleVisibility','off');
end
end


