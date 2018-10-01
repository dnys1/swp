%% INITIALIZE DATA
clear all; close all; clc;

load('years')
load('demand')
load('supply')

wassi = demand ./ supply;
wassi(:,1) = zeros(size(years));

%% INITIALIZE PLOTS
RGB = [0 0 0; 0.4 0.4 0.4;0.7 0.7 0.7];
m = {'^','s','o'};
fsize = 12; 
fweight = 'bold';

%% PLOT DATA
figure
hold on
% Plot different supply values
for index = 1:size(supply, 2)
    plot(years, supply(:, index), ['-', m{index}], 'markeredgecolor', RGB(index, :),...
        'markerfacecolor',[1 1 1],'markersize', 7, 'color', RGB(index, :), 'linewidth', 1.5);
end
% Plot demand values
plot(years, demand, 'markeredgecolor', RGB(1, :),...
    'markerfacecolor',[1 1 1],'markersize', 7, 'color', RGB(1, :), 'linewidth', 1.5);

title('WASSI - Supply/Demand');
xlabel('Year');
ylabel('Supply (acre-ft)');
legend('Hydro', 'Hydro + Infra', 'Hyrdo + Infra + Inst', 'Demand');
hold off

figure
hold on
% Plot different WASSI indices
for index = 1:size(wassi, 2)
    plot(years, wassi(:, index), ['-', m{index}], 'markeredgecolor', RGB(index, :),...
        'markerfacecolor',[1 1 1],'markersize', 7, 'color', RGB(index, :), 'linewidth', 1.5);
end

title('WASSI');
xlabel('Year');
ylabel('WASSI Index');
legend('Hydro', 'Hydro + Infra', 'Hyrdo + Infra + Inst');
hold off
