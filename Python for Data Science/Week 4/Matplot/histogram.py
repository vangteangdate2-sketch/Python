import matplotlib.pyplot as plt

scores = [45, 49, 50, 58, 60,
          63, 65, 66, 69, 70,
          72, 73, 75, 77, 80,
          81, 83, 85, 87, 99]

plt.figure(figsize = (9,5))

plt.hist(scores, bins = 5, edgecolor = "black")

plt.title("Distribution of Examinaton Scores")
plt.xlabel("Score")
plt.ylabel("Number of Students")

plt.show()
