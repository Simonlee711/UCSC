%{
File: SIR_model1.m
Author: Adrian Garcia
Purpose: Specifies the dynamics of a virus spread for (infection rate) k,
and (recovery rate) l. Then plots the total infected after t time steps.
%}
close all; clear; clc;
% Variable declaration
x_0 = [0.1, 0.25, 0.5, 0.75, 0.9]; % Initial susceptible population
t = [0, 100]; % Time step
N = 1000; % Population size
k = linspace(0, 1);
l = k;
z = zeros(length(k));
[X, Y] = meshgrid(k, l);
for a = 1:length(x_0)
    y_0 = [x_0(a), 1-x_0(a), 0.000]; % Initial conditions
    for i = 1:length(k)
        for j = 1:length(l)
            % Function call
            [~, y_ode45] = ode45(@(t, y_0)SIR_dynamics(y_0, k(i), l(j)), t, y_0);
            z(i, j) = y_ode45(end, 3);
        end
    end
    figure()
    % Plot
    s = surf(X, Y, z*N);
    % Plot config
    view([0,90]);
    set(s, 'edgecolor', 'none')
    xlabel('Recovery Rate', 'Fontsize', 14, 'Interpreter', 'latex')
    ylabel('Infection Rate', 'Fontsize', 14, 'Interpreter', 'latex')
    colormap jet
    colorbar
    ylabel(colorbar, 'Total Infected', 'Fontsize', 14, 'Interpreter', 'latex')
    title(sprintf('Total Infected when $x_0$ = %.2f', x_0(a)), 'Fontsize', 18, 'Interpreter', 'latex')
    subtitle(sprintf('(Population Size: $N$ = %.0f)', N), 'Fontsize', 12, 'Interpreter', 'latex')
end
% Function definition
function dy0_dt = SIR_dynamics(y_0, k, l)
    % Virus dynamics
    % dy0_dt = [dx_dt;dy_dt;dz_dt]
    dy0_dt = [-k*y_0(1)*y_0(2);
              k*y_0(1)*y_0(2)-l*y_0(2);
              l*y_0(2)];
end