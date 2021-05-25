# import matplotlib # whole library
from matplotlib import pyplot as plt

months = [1, 2, 3]
income1 = [1000, 4000, 10000]
income2 = [3000, 2000, 7000]

"""
LINE CHARTS
"""
#  plot makes a line chart = plt.plot(x-axis, y-axis, marker="graphMarkerSymbol", color="ColorName") matplotlib.org for avail colors
plt.plot(months, income1, marker="o", color="r")
plt.plot(months, income2, marker="o", color="dodgerblue")
# add a title, labels, and legend
plt.title("Income Chart for company1 and company2\n")
plt.xlabel("\nMonths")
plt.ylabel("\nIncome")
plt.legend(["company1", "company2"])
# show the chart
plt.grid()
plt.show()