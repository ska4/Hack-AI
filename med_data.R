med_data <- read.csv("meddata.csv")

library(ggplot2)
library(tidyverse)
library(DT)
library(reticulate)
library(dotenv)


cough <- ggplot(med_data, aes(Cough, fill = Disease))+ geom_bar()
fever <- ggplot(med_data, aes(Fever, fill = Disease))+ geom_bar()
fatigue <- ggplot(med_data, aes(Fatigue, fill = Disease))+ geom_bar()
difficult_breathing <- ggplot(med_data, aes(Difficulty.Breathing, fill = Disease))+ geom_bar()
bp <- ggplot(med_data, aes(Blood.Pressure, fill = Disease))+ geom_bar()
chol <- ggplot(med_data, aes(Cholesterol.Level, fill = Disease))+ geom_bar()
