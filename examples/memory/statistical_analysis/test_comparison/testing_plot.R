library(ggplot2)

# Read in the train and test CSV files
train_data <- read.csv("arena-train_LSTMresults.csv", header = TRUE, stringsAsFactors = FALSE)
test_data <- read.csv("arena_test_LSTMresults.csv")

# Extract the lists of 100 values from each file
train_values <- train_data[1, 1]
train_values <- strsplit(train_values, ",")[[1]]
train_values <- gsub("\\[|\\]", "", train_values)
train_values <- as.numeric(train_values)

test_values <- test_data[1, 1]
test_values <- strsplit(test_values, ",")[[1]]
test_values <- gsub("\\[|\\]", "", test_values)
test_values <- as.numeric(test_values)

# Calculate the mean and standard deviation of each list
train_mean <- mean(train_values)
test_mean <- mean(test_values)
train_sd <- sd(train_values)
test_sd <- sd(test_values)

ci <- t.test(train_values, conf.level = 0.95)$conf.int
ci <- t.test(test_values, conf.level = 0.95)$conf.int
print(ci)

# Create a data frame for plotting
plot_data <- data.frame(
  group = c("Train", "Test"),
  mean = c(train_mean, test_mean),
  ymin = c(train_mean - 1.96 * train_sd / sqrt(length(train_values)),
           test_mean - 1.96 * test_sd / sqrt(length(test_values))),
  ymax = c(train_mean + 1.96 * train_sd / sqrt(length(train_values)),
           test_mean + 1.96 * test_sd / sqrt(length(test_values)))
)

# Create the plot
ggplot(plot_data, aes(x = group, y = mean)) +
  geom_errorbar(aes(ymin = ymin, ymax = ymax), width = 0.2) +
  geom_point(size = 3, shape = 21, fill = "white") +
  geom_line(size = 1, linetype = "dashed") +
  labs(x = "", y = "Mean") +
  theme_classic()

# Add t-distribution intervals to the data frame
plot_data$ymin_t <- qt(0.025, df = length(train_values) - 1) * train_sd / sqrt(length(train_values))
plot_data$ymax_t <- qt(0.975, df = length(train_values) - 1) * train_sd / sqrt(length(train_values))

# Create the plot with t-distribution intervals
ggplot(plot_data, aes(x = group, y = mean)) +
  geom_errorbar(aes(ymin = ymin, ymax = ymax), width = 0.2) +
  geom_errorbar(aes(ymin = mean + ymin_t, ymax = mean + ymax_t), width = 0.2, color = "red") +
  geom_point(size = 3, shape = 21, fill = "white") +
  geom_line(size = 1, linetype = "dashed") +
  labs(x = "", y = "Mean") +
  theme_classic()

welch_ttest <- t.test(train_values, test_values, var.equal = FALSE)
welch_ci <- welch_ttest$conf.int
welch_pvalue <- welch_ttest$p.value
print(welch_ci)
print(welch_pvalue)
