%% INITIALIZE DATA
clear all; close all; clc;

load('years')
load('demand')
load('supply')

wassi = demand ./ supply;
wassi_log = log(wassi);

num_indices = size(supply, 2);

%% INITIALIZE PLOTS
RGB = [0 0 0; 0.4 0.4 0.4;0.7 0.7 0.7];
m = {'^','s','o'};
fsize = 12; 
fweight = 'bold';

%% PLOT DATA
figure
hold on
% Plot different supply values
for index = 1:num_indices
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

%% Log WASSI figure
figure
hold on
% Plot different WASSI indices
for index = 1:num_indices
    plot(years, wassi_log(:, index), ['-', m{index}], 'markeredgecolor', RGB(index, :),...
        'markerfacecolor',[1 1 1],'markersize', 7, 'color', RGB(index, :), 'linewidth', 1.5);
end

title('WASSI');
xlabel('Year');
ylabel('WASSI');
legend('Hydro', 'Hydro + Infra', 'Hyrdo + Infra + Inst');

tick_vals = [0.05, 0.1, 0.5, 1, 5, 10, floor(max(max(wassi)))];
yticks(log(tick_vals));
yticklabels(string(tick_vals));
hold off

%% Subplots WASSI Figure
fig = figure;
hold on
% Plot different WASSI indices
titles = ["Hydro", "Hydro + Infra", "Hyrdo + Infra + Inst"];
for index = 1:num_indices
    subplot(3, 1, index);
    plot(years, wassi(:, index), ['-', m{index}], 'markeredgecolor', RGB(index, :),...
        'markerfacecolor',[1 1 1],'markersize', 7, 'color', RGB(index, :), 'linewidth', 1.5);
    title(titles(index));
end

supAxes = [.09 .12 .85 .825];
suplabel('Year', 'x', supAxes);
suplabel('WASSI Index', 'y', supAxes);
suplabel('WASSI', 't', supAxes);
hold off
