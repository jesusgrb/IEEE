clear; clc; close all;

%% Raw SCR Peak Data
SCR_data = [ ...
42 41 11;
83 47 41;
13 35 9;
66 95 52;
45 65 20;
19 24 20;
69 80 37;
34 24 18;
45 78 59;
17 54 20;
44 38 42;
41 51 27;
27 29 13;
63 49 33;
30 33 9;
58 51 37;
88 83 75;
61 64 48;
26 30 5;
91 73 49;
31 6 0;
33 28 14;
76 39 58;
59 70 66];

genres = {'Horror','Skill','Workout'};
colors = [0.8 0.2 0.2; 0.2 0.4 0.8; 0.3 0.7 0.3];

%% Figure 1: Boxplot by genre
figure;
boxplot(SCR_data, 'Labels', genres, 'Colors', 'k', 'Whisker', 1.5);
ylabel('SCR Peaks (\muS)');
%title('SCR Peak Distribution by Game Genre');

%% Figure 2: Mean and Std Dev Barplot
means = mean(SCR_data);
stds = std(SCR_data);

figure;
hold on;
for i = 1:3
    bar(i, means(i), 'FaceColor', colors(i,:), 'EdgeColor', 'k');
    errorbar(i, means(i), stds(i), 'k', 'LineWidth', 1.5);
end
set(gca, 'XTickLabel', genres, 'XTick', 1:3);
ylabel('Mean SCR Peak (\muS)');
%title('Mean and Std Dev of SCR Peaks by Genre');
hold off;

%% Regression Model Performance (Provided Values)
real_values = [60.67, 82, 31.33, 20.33, 39.67, 30.33, 48.33, 57];
pred_values = [59.68, 84.62, 30.77, 22.32, 36.45, 29.63, 47.23, 50.79];

% Figure 3: Real vs Predicted
figure;
scatter(real_values, pred_values, 80, 'filled');
hold on;
plot([0 100], [0 100], 'k--', 'LineWidth', 1.2);
xlabel('Real SCR Peak (\muS)');
ylabel('Predicted SCR Peak (\muS)');
%title('Real vs. Predicted SCR Peak Values');
axis([0 100 0 100]);
grid on;

%% Figure 4: Histograms
figure;
subplot(1,2,1);
histogram(real_values, 'FaceColor', [0.6 0.3 0.3]);
xlabel('Real SCR Peak (\muS)');
title('Distribution of Real SCR Peaks');

subplot(1,2,2);
histogram(pred_values, 'FaceColor', [0.3 0.6 0.8]);
xlabel('Predicted SCR Peak (\muS)');
title('Distribution of Predicted SCR Peaks');

%% Figure 5: Model Loss (synthetic visualization)
epochs = 1:1000;
loss_train = exp(-epochs/300) + 0.1*rand(1,1000);
loss_val = exp(-epochs/250) + 0.15*rand(1,1000);
mae_train = 1.2*exp(-epochs/250) + 0.1*rand(1,1000);
mae_val = 1.1*exp(-epochs/300) + 0.1*rand(1,1000);

figure;
subplot(2,1,1);
plot(epochs, loss_train, 'b', epochs, loss_val, 'r');
legend('Training Loss', 'Validation Loss');
ylabel('MSE');
title('Loss Curve');

subplot(2,1,2);
plot(epochs, mae_train, 'b--', epochs, mae_val, 'r--');
legend('Training MAE', 'Validation MAE');
xlabel('Epochs');
ylabel('MAE (\muS)');
title('MAE Curve');
