% HW 2 - Simon Lee
%
% Bisection Method

function bis = bisection(a,b,f,tolerance)
    % f - nonlinear function
    % a - lower bound
    % b - upper bound
    % tolerance - threshold to exit approximation
    % algorithm straigh from class notes
    
    cond = (b-a)/2;
    
    while cond > tolerance
        c = (b+a)/ 2;
        if f(c) == 0
            break
        elseif (f(c) * f(a)) < 0
            b = c;
        else
            a = c;
        end
        

    end
    bis = c;
end
