import random
pigs=("Ниф-ниф","Наф-Наф","Нуф-нуф")
choice=random.choice(pigs)
pg=input("Угадайте одного из трех поросят: ")
while pg != choice:
	pg=input("Не угадали. Попробуйте еще: ")
print("Вы угадали. Это",choice)
input("Нажмите ENTER для продолжения")
