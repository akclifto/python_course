from matplotlib import pyplot as plt

conts = ["Asia", "Europe", "Africa",
         "North America", "South America"]
pop = [4463000000, 741000000, 1216000000, 579000000, 422000000]
# isolate some data from the rest plt.explode to highlight it
explode = (0, 0, 0, 0.1, 0)
colors = ["g", "purple", "b", "r", "gold"]
# plt.pie(pop, labels=conts) # add labels directly to pie charts
plt.pie(pop, autopct="%1.1f%%", startangle=45, explode=explode, colors=colors)
# use a legend to add labels to pie chart
plt.legend(conts)
# to align everything...
plt.axis("equal")

plt.title("World Population by Continents, Sorry 'Straya\n")
plt.show()
