import random
pigs=("Ниф-Ниф","Наф-Наф","Нуф-Нуф")
choice=random.choice(pigs)
pg=input("Угадайте одного из трех поросят: ")
points=1000
while pg != choice:
	pg=input("Не угадали. Попробуйте еще: ")
	points-=100
	if points <=0:
		break
if points <=0:
	print("К сожалению, у вас 0 очков, и вы проиграли. А это был поросенок по имени",choice)
else: print("Вы угадали. Это",choice,"! У вас",points,"очков!")
input("Нажмите ENTER для продолжения")
