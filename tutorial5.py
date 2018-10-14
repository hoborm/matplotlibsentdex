from matplotlib import pyplot as plt



days=[1,2,3,4,5]
sleeping=[7,8,6,11,7]
eating=[2,3,4,3,2]
working=[7,8,7,2,2]
playing=[8,5,7,8,13]

ax=plt.subplot()

ax.stackplot(days, sleeping,eating,working,playing,colors=['c','m','y','k'],labels=['sleeping','eating','working','playing'])





plt.xlabel("x")
plt.ylabel("y")
plt.title("Interesting graph\nCheck it out")
plt.legend()

plt.show()