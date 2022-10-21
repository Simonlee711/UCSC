close all
clear all



f = @(mu,x) mu.*x+x.^3-x.^5;
f1=@(mu,x)mu+3.*x.^2-5.*x.^4;
% Mu=-.90:.02:.90
% x0=-5:.05:5

xx=linspace(-10, 10, 1000);
mm=linspace(-2,10,1000);

[X,M]=meshgrid(xx,mm);

figure(1)
[cc,hh]=contour(M,X,f(M,X),[0 0]);


F1=f1(cc(1,:),cc(2,:));


idx1=F1>0; % unstable
idx2=F1<0; % stable

figure(2)
clf
plot(cc(1,find(idx2)),cc(2,find(idx2)),'b.')
hold
plot(cc(1,find(idx1)),cc(2,find(idx1)),'r.')
axis([-5 10 -10 10])
xlabel('$\mu$','Interpreter','Latex')
ylabel('$x^*(\mu)$','Interpreter','Latex')
grid
set(gca,'Fontsize',20)



 