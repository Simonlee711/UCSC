% Simon Lee
%
% RK4 Method

function rk4 = FixedStepRK4(func, t, ic)
    % intializing dt and t
    dt = 0.5;
    y = zeros(201,4);
    y(1,:) = ic;    
    
    % RK4 Method Straight from Class
    for i = 1:199
        k1 = (dt)*func(t(i),y(i,:))';
        k2 = (dt)*func(t(i)+dt/2,y(i,:)+k1*dt/2)';
        k3 = (dt)*func(t(i)+dt/2,y(i,:)+k2*dt/2)';
        k4 = (dt)*func(t(i)+dt,y(i,:)+k3*dt)';   
        y(i+1,:) = y(i,:) + (k1+2*k2+2*k3+k4)/6;
    end
    
    rk4 = y;
end