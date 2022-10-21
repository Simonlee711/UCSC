clc
R(1) = Deaths(1);
for i = 2:52
    R(i) = R(i-1)+Deaths(i);
end
R0 = Deaths(1);
dRdt = Deaths(:);
for i = 2:52
    if(dRdt < 0.01) 
        dRdt(i) = 0;
    end
end
%Deaths per week plot
%figure
%plot(Weeks,Deaths)
%xlabel('Weeks')
%ylabel('Deaths per week')
l = 0.001899;
%k = 0.3681;
k = 1.3681;
S0 = 900000;
N = 900000;
figure
plot(Weeks,R-R0, '--')
xlabel('Week')
ylabel('Cumulative Deaths')
hold on
dRdt_t = [];
for i = 1:52
    if i == 1
        R0 = 0;
    else
        R0 = R(i-1);
    end
    dRdt_t(end+1) = l*(S0-(R(i)-R0)-S0*exp(-(k*(R(i)-R0))/(N*l)));
end
dRdt_2 = transpose(dRdt_t);
dRdt_new = cumtrapz(dRdt_2);
plot(Weeks,dRdt_new)
title('Experimental vs Model Bombay Plague')
xlabel('R-R0')
ylabel('Deaths')