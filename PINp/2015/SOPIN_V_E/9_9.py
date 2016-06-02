import random
words=("Валера","зачет","ргсу","Николай","общага","студент","работа")
choice=random.choice(words)
check=choice
numbers=len(choice)
symbol = random.randrange(numbers)
i=4
k=0
print("Давай поиграемв игру. Я загадываю слово, а ты его отгадываешь.\nСначала ты называешь буквы, а я проверяю, если ли она в слове! У тебя 5 попыток")
print("Слово загадано. В нем",numbers,"букв.")
vibor=input("Вводи букву: ")
while i>0:
	if vibor in check:
		print("Есть такая буква!")
	else: print("Нет такой буквы!")
	i-=1
	vibor=input("Вводи еще одну букву: ")
print("Попытки кончились. Теперь отгадывай слово!")
while vibor != choice:
	vibor=input("Это слово: ")
	if vibor !=choice: print("Неправильно. Попробуй еще")
print("Угадал! Это слово",choice)
input("Нажми ENTER, чтобы я тебя освободил!")