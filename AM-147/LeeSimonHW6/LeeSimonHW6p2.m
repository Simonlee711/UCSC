% HW 6 
% Simon Lee
% Least Squares Solution and Round off Errors

close all; clear; clc;
xhat_normal = {[0,0],[0,0],[0,0],[0,0]};
xhat_QR = {[0,0],[0,0],[0,0],[0,0]};
for i=1:4
    A = [1 1;10^(-i+4) 0;0 10^(-i+4)];
    A_Tran = transpose(A);
    b = [-10^(-i+4);1+10^(-i+4);1-10^(-i+4)];
    
    % we want to extract the index of these arrays
    xhat_QR{i} = A\b;
    xhat_normal{i} = (inv(A_Tran * A) * A_Tran * b);
end

% print statements
for i=1:4
   disp('i =')
   disp(i+4)
   disp(xhat_QR{i})
   disp(xhat_normal{i})
   
end

