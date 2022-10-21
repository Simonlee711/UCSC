% Simon Lee
%
% SIRD Dynamics function

function ivp = SIRD_dynamics(~, ic)
    %declare all things needed for ODE
    N = 1000; % population size
    b = 0.45; % beta
    g = 0.04; % gamma
    m = 0.01; % mu
    
    
    % Magic
    ivp = [((-b/N)*ic(2)*ic(1)); ((b/N)*ic(2)*ic(1))- (g*ic(2)) - m*ic(2); g*ic(2); m*ic(2) ];
end