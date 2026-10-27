import matplotlib as plt
#data
categories = ["A", "B", "C"]
price = [70, 80, 90]

#Create bar chart
plt.bar(categories,price)
plt.title("Example Bar Chart")
plt.xlabel("Category")
plt.ylabel("Price")
plt.ylim(0,100)
plt.show()