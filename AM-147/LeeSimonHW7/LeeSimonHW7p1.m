% Simon Lee
%
% AM 147 - HW 7
%Finite Difference Approximation of derivative and numerical errors

close all; clear; clc;
forward = zeros(180,1)
central = zeros(180,1);
rel_err_forward = zeros(180,1);
rel_err_central = zeros(180,1);
h = zeros(180,1);
x0 = 0; % guess is cenetered around this
df = 100 % truue value

for k = 20:200
    h(k-19) = 2.^(-k/4);
    % forward difference
    forward(k-19) = (exp(100.*(h(k-19))) - exp(0))./h(k-19);
    rel_err_forward(k-19) = ((forward(k-19) - df)./df).*100;
    % central difference
    central(k-19) = (exp(100.*(h(k-19))) - exp(100.*(-h(k-19))))./(h(k-19).*2);
    rel_err_central(k-19) = ((central(k-19) - df)./df).*100;
end


figure(1)
loglog(h,rel_err_forward,'--ro','LineWidth',2,'MarkerSize',10)
hold on
loglog(h,rel_err_central,'-bs','LineWidth',2,'MarkerSize',10)
legend('Forward difference','Central difference')
set(gca,'FontSize',30)
xlabel('h','FontSize',30);
ylabel('Relative error','FontSize',30);
grid on
axis tight
