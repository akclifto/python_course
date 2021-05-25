from matplotlib import pyplot as plt

day = [1, 2, 3, 4, 5, 6, 7]
day_tmp = [27, 34, 30, 38, 25, 21, 29]  # celsius
night_tmp = [20, 27, 25, 32, 21, 16, 23]
plt.bar(day, day_tmp, color="orange")
plt.bar(day, night_tmp, color="orangered")
plt.title("Temperature Record (1 Week)\n")
plt.xlabel("\nDays")
plt.ylabel("\nTemperature (Celsius)")
plt.legend(["Day", "Night"])
plt.show()
