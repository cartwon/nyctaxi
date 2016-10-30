---

```{r}
library("dplyr")

rain <- read.csv("/Users/Yaqian/Dropbox/2016 Fall/Computational Social Science/Assignment 2/nyc_precipitation.csv")
taxi <- read.table("/Users/Yaqian/Dropbox/2016 Fall/Computational Social Science/Assignment 2/drivers_by_hour.tsv",
  sep="\t", header=FALSE)
names(taxi) <- c('date', 'hour', 'drivers_onduty', 'drivers_occupied', 't_onduty', 't_occupied', 'n_pass', 'n_trip', 'n_mile', 'earnings') 

# transform the datetime variable
taxi <- mutate(taxi, year=substr(date, 1, 4))
taxi <- mutate(taxi, month=substr(date, 6, 7))
taxi <- mutate(taxi, day=substr(date, 9, 10))
taxi$datetime <- ISOdatetime(taxi$year, taxi$month, taxi$day, taxi$hour, 0, 0)

# transform the datetime variable
rain <- mutate(rain, year=substr(DATE, 1, 4))
rain <- mutate(rain, month=substr(DATE, 5, 6))
rain <- mutate(rain, day=substr(DATE, 7, 8))
rain <- mutate(rain, hour=substr(DATE, 10, 11))
# Hour 00:00 will be listed as the first hour of each date, however since this data is by definition an accumulation of the previous 60 minutes, it actually occurred on the previous day. 
rain$datetime <- ISOdatetime(rain$year, rain$month, rain$day, rain$hour, 0, 0) - 3600
# select datetime and precip
rain <- rain[, c(4,9)]

# LEFT JOIN the datasets
data <- left_join(taxi, rain, by = "datetime")
# sort the data
data <- arrange(data, date, hour)
data <- select(data, -year, -month, -day)

# generate the dummy for rain or not
data$HPCP[is.na(data$HPCP)] <- 0
data$rain_dum <- ifelse(data$HPCP>0, 1, 0)
data <- rename(data, precip=HPCP)

write.table(data, file='data.tsv', quote=FALSE, sep='\t', col.names =TRUE, row.names=FALSE)
```
