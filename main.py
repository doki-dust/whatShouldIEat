import random
import time
import documentProcessing

menu = open("storeDishes.md", "r", encoding="utf-8")
allDishes = int(menu.readline())

listOfDishes = documentProcessing.do_list(menu, [[] for i in range(allDishes * 2)])

print("\033[7;40m正在为您挑选店家及菜品......\033[0m")
time.sleep(1)

store = random.randint(0, allDishes - 1)
print("这一顿就在" + '\033[0;36m%s\033[0m' % listOfDishes[store][0], end='')

listOfDishes = documentProcessing.remove_store(allDishes, listOfDishes)
if len(listOfDishes[store]) == 0:
    print("吃：" + '\033[0;36m你一见倾心的菜品\033[0m', end="。")
else:
    print("吃：" + '\033[0;36m%s\033[0m' % random.choice(listOfDishes[store]), end="。")

menu.close()
