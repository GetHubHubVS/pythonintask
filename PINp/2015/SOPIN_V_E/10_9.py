print("Генератор персонажа")
points = 30
character = {"Сила" : 8, "Ловкость" : 8, "Здоровье" : 8, "Мудрость" : 8}
for i in character:
	print(character[i])
values = character.keys()
atr = input("Введите атрибут, который вы хотите изменить: ")
num = int(input("Введите количество очков (\"-\" для вычитания очков): "))
print(num)
points -= num
for value in character:
	if attr == value:
		print(atr)

class Character:
	def __init__(self, points):
		self.atrib = ("Сила", "Ловкость", "Здоровье", "Мудрость")
		self.values = [8, 8, 8, 8]
		self.ppool = points
	def update(self, chrt, num):
		print()
		for i in range (len(self.atrib)):
			if chrt.capitalize() == self.atrib[i]:
				self.ppool -= num
				if self.ppool < 0:
					num += self.ppool
					self.ppool = 0
				self.values[i] += num
			print(self.atrib[i], end = ' : ')
			print(self.values[i])
		print("\nОчки:", self.ppool)

pers = Character(30)
chrt, num = "some", 0
while chrt != "":
	pers.update(chrt, num)
	chrt = input("\nХарактеристика: ").strip()
	temp = input("Очки (\"-\" для уменьшения, Enter для выхода): ").strip()
	if len(temp):
		if temp.isdigit() or temp[0] == '-':
			num = int(temp)
print("Создание персонажа завершено...")
input("\nНажмите Enter для выхода")