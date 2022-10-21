% Simon Lee - Hw9
%
% Power iteration to compute PageRank


close all; clear; clc;
format long

% read in files and get the dimensions
A = readmatrix('AdjacencyMatrix.txt');
[rows,cols] = size(A);
n = rows;

% Code from lecture slides
S = A * inv(diag(ones(1,n)*A));

% check for dangling nodes
columnSum = sum(A, 1);
x0 = zeros(500,1); % we need this later
for i = 1:n
    if columnSum(i) == 0
        A(i,:) = 1/n;
    end
    x0(i) = 1/n;
end

% Part b of assignment
alpha = 0.25:0.25:1;

k = 1:10; % for plotting
G1 = zeros(500,500);
G2 = zeros(500,500);
G3 = zeros(500,500);
G4 = zeros(500,500);

% Construct Google matrix
G1 = alpha(1)*S+(1-alpha(1))/500*ones(500,500);
G2 = alpha(2)*S+(1-alpha(2))/500*ones(500,500);
G3 = alpha(3)*S+(1-alpha(3))/500*ones(500,500);
G4 = alpha(4)*S+(1-alpha(4))/500*ones(500,500);

% stores TV dist vector for part c
poweriter1 = zeros(500,1);
poweriter2 = zeros(500,1);
poweriter3 = zeros(500,1);
poweriter4 = zeros(500,1);

for a = 1:4
    % power iteration at specific alpha
    rel_err = zeros(10,1);
    xminus1 = x0;
    if a == 1
        for i = 1:10
            vec = G1*xminus1;
            rel_err(i) = TVdist(vec, xminus1);
            xminus1 = vec;
            if i == 10
                poweriter1(:) = vec;
            end

        end
        semilogy(k,rel_err,'r');
        hold on;
    end
    
    if a == 2
        for i = 1:10
            vec = G2*xminus1;
            rel_err(i) = TVdist(vec, xminus1);
            xminus1 = vec;
            if i == 10
                poweriter2(:) = vec;
            end
        end
        semilogy(k,rel_err,'g');
        
    end
    if a == 3
        for i = 1:10
            vec = G3*xminus1;
            rel_err(i) = TVdist(vec, xminus1);
            xminus1 = vec;
            if i == 10
                poweriter3(:) = vec;
            end

        end
        semilogy(k,rel_err,'b');
       
    end
    if a == 4
        for i = 1:10
            vec = G4*xminus1;
            rel_err(i) = TVdist(vec, xminus1);
            xminus1 = vec;
            if i == 10
                poweriter4(:) = vec;
            end

        end
        semilogy(k,rel_err,'k');
        legend('$\alpha=0.25$','$\alpha=0.50$','$\alpha=0.75$','$\alpha=1.00$','Interpreter','latex');
        xlabel('Power Iteration Index $k$','Interpreter','latex');
        ylabel('Relative Error','Interpreter','latex');
    end
end

% part c
pct_err = zeros(3,1);

for i = 1:3
    if i == 1
        pct_err(i) = TVdist(poweriter1, poweriter4) * 100;
    end
    if i == 2
        pct_err(i) = TVdist(poweriter2, poweriter4) * 100;
    end
    if i == 3
        pct_err(i) = TVdist(poweriter3, poweriter4) * 100;
    end
end

pct_err



        






