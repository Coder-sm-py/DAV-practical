library(dplyr)

# Create a data frame
d <- data.frame(
  name = c("Addy", "Alchemy", "Frost", "Cherrisha"),
  age = c(7, 5, 9, 16),
  ht = c(46, NA, NA, 69),
  school = c("yes", "yes", "no", "no")
)

# Arrange the data by age
d.name <- arrange(d, age)

# Print the sorted data frame
print(d.name)

