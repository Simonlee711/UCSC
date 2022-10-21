% Simon Lee
%
% TVdist function 

function d = TVdist(a,b)
    % takes the 1 norm of the vector b-a
    ab = a - b;
    ab = abs(ab);
    norm1 = sum(ab);
    d = (1/2 * norm1);
end