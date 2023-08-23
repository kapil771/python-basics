# import statistics

# example_list = [4, 6, 2, 6, 7, 8, 2, 5, 6, 78, 4, 6, 7, 2, 2]
# x = statistics.mean(example_list)
# stdev = statistics.stdev(example_list)

# print(x)
# print(stdev)

from statistics import mean, stdev

example_list = [4, 6, 2, 6, 7, 8, 2, 5, 6, 78, 4, 6, 7, 2, 2]
x = mean(example_list)
stdev = stdev(example_list)

print(x)
print(stdev)
