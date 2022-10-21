% Simon Lee - AM 147 Winter 2022
%
% Weird Numbers Program
% need symbolic toolbox to run program

close all; clear; clc;

% an array to store weird numbers
weird_Num = [];

% take in user input
prompt1 = 'Enter first positive integer: ';
prompt2 = 'Enter second positive integer: ';
num1 = input(prompt1);
num2 = input(prompt2);

% weird numbers algorithm itself
for i = num1:num2
    array = [];
    for divisors = 1:(i/2)
        r = rem(i,divisors);
        if r == 0
            array(end+1) = divisors;
        end
    end
    
    count = 0; % counter to see if number ever matches sum
   
    % checks first condition of whether sum is smaller than number
    if sum (array) > i;
        
        % if first condtion true, we want to know size and n choose k
        l = length(array);
        
        % loop to check every nchoosek possibility
        for j = 2:l
            comb = nchoosek(array,j);
            [combSize,numCols] = size(comb);
            for k = 1:combSize % another loop to calculate row sum
                rowSum = sum(comb(k,:)); %sum of row(k)
                if rowSum == i
                   % if count >0 we know its not a weird number
                   count = count + 1;
                   break;
                end
                
            end
            if(count == 1)
                break; %to optimize the code
            end
            
        end
        if count == 0
            weird_Num(end+1) = i; % appends to empty array
       
        end
    
    end
    
end
if size(weird_Num) == 0
    disp('[]') % prints empty array if no weird numbers
else
    msg1 = ['WeirdNum = ', num2str(weird_Num)];
    disp(msg1)
end

