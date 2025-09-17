clear; clc;

% Simulated time axis (in seconds, 5 minutes = 300s)
t = linspace(0, 300, 300);  % 1 Hz sampling for simplicity

% Simulated SCR data per genre (Mean ± variability)
scr_horror = 0.7 + 0.1*sin(2*pi*t/60) + 0.3*randn(size(t));
scr_skill  = 0.75 + 0.05*sin(2*pi*t/80) + 0.2*randn(size(t));
scr_exer   = 0.5 + 0.03*sin(2*pi*t/50) + 0.15*randn(size(t));

% Apply moving average to smooth signals
windowSize = 10;
scr_horror_smooth = movmean(scr_horror, windowSize);
scr_skill_smooth  = movmean(scr_skill, windowSize);
scr_exer_smooth   = movmean(scr_exer, windowSize);

% Plot
figure;
plot(t, scr_horror_smooth, 'r', 'LineWidth', 1.5); hold on;
plot(t, scr_skill_smooth, 'b', 'LineWidth', 1.5);
plot(t, scr_exer_smooth, 'g', 'LineWidth', 1.5);
xlabel('Time (s)');
ylabel('SCR (\muS)');
%title('SCR Peak Dynamics Across VR Game Genres');
legend('Horror', 'Skill', 'Exercise', 'Location', 'northeast');
grid on;

% Scientific annotation
text(20, 1.2, 'Elevated peaks in skill suggest sustained engagement', 'FontSize', 9);
