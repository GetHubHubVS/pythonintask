import random
choice=random.randint(1,3)
random="Одной из стран блока 'Атланта' является "
if choice ==1:
	print(random+"Россия.")
elif choice ==2:
	print(random+"Англия.")
elif choice ==3:
	print(random+"Франция.")
input("Нажмите ENTER для продолжения")
