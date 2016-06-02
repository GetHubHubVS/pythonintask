import random
points = 1000
words =("Валера","зачет","ргсу","Николай","общага","студент","работа")
choice=random.choice(words)
check = choice
i=0
anagramma = ""
while choice:
	symbol = random.randrange(len(choice))
	anagramma += choice[symbol]
	choice = choice[:symbol] + choice[(symbol+1):]
print("Привет. Давай сыграем в Анаграммы!")
print("Я загадал слово: ", anagramma)
vibor = input ("Твое слово: ")
while (vibor != check):
	if(vibor == ""):
		print(i,"буква: ",check[i])
		i+=1
	if points <= 0:
		break
	vibor=input("Неправильно. Попробуй еще раз: ")
	points-=100
if vibor == check: 
	print("\nПравильно! Это слово:", check)
	print("Ты набрал",points,"очков! Молодец!")
else: 
	print("К сожалению, у тебя 0 очков, и ты проиграл. Загаданное слово:",check)
input ("Нажмите ENTER для продолжения")