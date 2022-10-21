% Simon Lee
%
% HW 8 - Model of Virus Spread

close all; clear; clc;
% declare inital conditions and time array
ic = [995, 5, 0, 0];
t = 0:0.5:100; 

% Gets ODE and RK4
[t,y] = ode45(@SIRD_dynamics, t, ic);
y2 = FixedStepRK4(@SIRD_dynamics, t, ic);

%plot
figure(1)
plot(t,y(:,1),'-b',t,y(:,2),'-r',t,y(:,3),'-g',t,y(:,4),'-k');
hold on 
plot(t,y2(:,1),'bo',t,y2(:,2),'ro',t,y2(:,3),'go',t,y2(:,4),'ko')
xlabel('Time (t)','Fontsize',12)
ylabel('affected totals' ,'Fontsize',12)
title('SIRD','Fontsize',12)
legend('$S(t)$','$I(t)$', '$R(t)$', '$D(t)$', 'Fontsize', 12,'Interpreter','latex')

