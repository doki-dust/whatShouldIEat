import random
import time
import documentProcessing

menu = open("storeDishes.md", "r", encoding="utf-8")
allDishes = int(menu.readline())

listOfDishes = documentProcessing.do_list(menu, [[] for i in range(allDishes)])

print("正在为您挑选餐厅及菜品......")
time.sleep(1)

store = random.randint(0, allDishes - 1)
print("这一顿就在" + '\033[0;36m %s \033[0m' % listOfDishes[store][0], end='')

listOfDishes = documentProcessing.remove_store(allDishes, listOfDishes)
if len(listOfDishes[store]) == 0:
    print("吃你一见倾心的菜品。")
else:
    print("吃：" + '\033[0;36m%s \033[0m' % random.choice(listOfDishes[store]), end="。")
