data <- read.csv("info_agua_tratado.csv")
esgoto <- read.csv("info_esgoto_tratado.csv")

quantile(data$tratada, na.rm = TRUE)

quantile(esgoto$tratado, na.rm = TRUE)

