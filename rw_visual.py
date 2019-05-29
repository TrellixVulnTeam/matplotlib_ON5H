import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断的模拟随机漫步
while True:

    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, c = rw.x_values,# cmap=plt.cm.BuGn,
                s = 15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if  keep_running == "n":
        break