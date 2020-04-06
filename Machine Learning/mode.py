from scipy import stats

speed = [99,87,87,88,111,86,103,87,94,78,77,85,86,86]

x = stats.mode(speed)

print(x)