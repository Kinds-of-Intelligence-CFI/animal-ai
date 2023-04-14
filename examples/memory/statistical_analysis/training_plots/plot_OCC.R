library(ggplot2)

data1 <- read.csv("OCC LSTM Train/OCC_L_RecurrentPPO_0.csv")
data2 <- read.csv("OCC PPO Train/OCC_PPO_0.csv")

global_step <- data1[,2]
global_step_2 <- data2[,2]

episode_mean <- data1[,3]
episode_mean_2 <- data2[,3]

LSTM <- data.frame(global_step, episode_mean)
PPO <- data.frame(global_step_2, episode_mean_2)

LSTM$source <- "LSTM"
PPO$source <- "PPO"

colnames(PPO) <- c("global_step", "episode_mean", "source")
df <- rbind(LSTM, PPO)

# plot graph using ggplot2
ggplot(df, aes(x = global_step, y = episode_mean, color = source)) +
  geom_smooth(method = "auto",size=2) +
  labs(x = "Global Step", y = "Episode Mean Reward",
       title = "Arena Task") +
  scale_color_manual(values = c("#c260e2", "#6080e2")) +
  guides(color = guide_legend(title = "Test")) +
  theme_classic() +
  theme(axis.line = element_line(size = 0.5, color = "black"),
        axis.title = element_text(size = 14, face = "bold"),
        axis.text = element_text(size = 12),
        legend.position = "bottom",
        legend.title = element_blank(),
        legend.text = element_text(size = 12),
        panel.grid.major = element_line(size = 0.2),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        panel.border = element_blank(),
        plot.background = element_blank(),
        plot.title = element_text(size = 14, face = "bold",??hjust??=??0.5))

ggplot(df, aes(x = global_step, y = episode_mean, color = source)) +
  geom_point(size = 2, alpha = 0.7) +
  labs(x = "Global Step", y = "Episode Mean Reward",
       title = "Complex Task Training") +
  scale_x_continuous(limits = c(512, 2500000), breaks = seq(0, 2500000, by = 500000),
                     labels = scales::comma) +
  scale_color_manual(values = c("#c260e2", "#6080e2")) +
  guides(color = guide_legend(title = "Test")) +
  theme_classic() +
  theme(axis.line = element_line(size = 0.5, color = "black"),
        axis.title = element_text(size = 14, face = "bold"),
        axis.text = element_text(size = 12),
        legend.position = "bottom",
        legend.title = element_blank(),
        legend.text = element_text(size = 12),
        panel.grid.major = element_line(size = 0.2),
        panel.grid.minor = element_blank(),
        panel.background = element_blank(),
        panel.border = element_blank(),
        plot.background = element_blank(),
        plot.title = element_text(size = 14, face = "bold",??hjust??=??0.5))
