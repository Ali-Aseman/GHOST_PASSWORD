import string
import argparse
from random import choices
from random import choice, randint
from string import printable, digits
from multiprocessing import Process
from time import time
from rich.progress import track
from time import sleep

print("""
@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@#J::J#@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@B?.    ~#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@B7.    ^5&@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@G!     ~P@@@@@B7!P@@@@@@@@@@@@
@@@@@@@@@B~     ^G@@@@@G!    ~P&@@@@@@@@@
@@@@@@@@@&G!    .~P@@P~        ^5&@@@@@@@
@@@@#YP@@@@@B?.    ^^    .?J:    :J#@@@@@
@@#?.  ^5&@@@@#J.      .J#@@&Y:    .?#@@@
@@#?.    :Y&@@#J.      .J#@@@@&5^  .?#@@@
@@@@#J:    :J?.    ^^    .7B@@@@@PY#@@@@@
@@@@@@&Y^        ~P@@P!.    !G@@@@@@@@@@@
@@@@@@@@@P~   .!G@@@@@G^     ~B@@@@@@@@@@
@@@@@@@@@@@P!7B@@@@@P~     !G@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@&5^    .7B@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@#~    .?#@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@#J::J#@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@&&@@@@@@@@@@@@@@@@@@@@
""")
print()
print()
print("██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗███████╗██████╗ ██████╗  ██████╗  ██████╗ ")
print("██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔═══██╗██╔════╝ ")
print("██║  ███╗███████║██║   ██║███████╗   ██║   █████╗  ██████╔╝██████╔╝██║   ██║██║  ███╗")
print("██║   ██║██╔══██║██║   ██║╚════██║   ██║   ██╔══╝  ██╔═══╝ ██╔══██╗██║   ██║██║   ██║")
print("╚██████╔╝██║  ██║╚██████╔╝███████║   ██║   ███████╗██║     ██║  ██║╚██████╔╝╚██████╔╝")
print(" ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ")
print()
print()
__author__ = "ALi Akbar Mohajer"

password = open('password_List.txt', 'w')
listme = []

class Generate:
	def __init__(self):

		self.string = ""
		self.short = ""
		self.space = ""
		self.name = ""
		self.family = ""
		self.phone = ""
		self.point = point
		self.national_id = national_id
	def method_1(self, name, family):
		listme.append("=========METHOD 1=========")
		space = " "

		if space in name:
			name = name.replace(" ", " ")

		string = name = family + "\n"
		listme.append(string)
		string = name  + "0" + "\n"
		listme.append(string)
		string = name  + "1" + "\n"
		listme.append(string)
		string = name  + "123" + "\n"
		listme.append(string)
		string = name  + "12345" + "\n"
		listme.append(string)
		string = name  + "123456" + "\n"
		listme.append(string)
		string = name + "1122" + "\n"
		listme.append(string)
		string = name + "112233" + "\n"
		listme.append(string)
		string = name + "11223344" + "\n"
		listme.append(string)
		string = name + "1122334455" + "\n"
		listme.append(string)
		string = name + "112233445566" + "\n"
		listme.append(string)
		string = name + "11223344556677" + "\n"
		listme.append(string)
		string = name + "1122334455667788" + "\n"
		listme.append(string)
		string = name + "112233445566778899" + "\n"
		listme.append(string)
		if space in name:
			name = name.replace(" ", " ")
		if space in name:
			name = family.replace(" ", " ")

		string = family + name +"\n"
		listme.append(string)
		string = family + "0" + "\n"
		listme.append(string)
		string = family + "1" + "\n"
		listme.append(string)
		string = family + "123" + "\n"
		listme.append(string)
		string = family + "12345" + "\n"
		listme.append(string)
		string = family + "123456" + "\n"
		listme.append(string)
		string = family + "123456789" + "\n"
		listme.append(string)
		string = family + "@" + "\n"
		listme.append(string)
		string = family + "%" + "\n"
		listme.append(string)
		string = family + "&" + "\n"
		listme.append(string)
		string = family + "*" + "\n"
		listme.append(string)
		string = family + "1122" + "\n"
		listme.append(string)
		string = family + "112233" + "\n"
		listme.append(string)
		string = family + "11223344" + "\n"
		listme.append(string)
		string = family + "1122334455" + "\n"
		listme.append(string)
		string = family + "1122335566" + "\n"
		listme.append(string)
		string = family + "1122344556677" + "\n"
		listme.append(string)
		string = family + "1122334455667788" + "\n"
		listme.append(string)
		string = family + "112233445566" + "\n"
		listme.append(string)

		string = name + " " + family
		if space in string:
			ll = string.split(" ")
			for j in ll:
				self.short += j[0]

		string = self.short + "0" + "\n"
		listme.append(string)
		string = self.short + "1" + "\n"
		listme.append(string)
		string = self.short + "123" + "\n"
		listme.append(string)
		string = self.short + "12345" + "\n"
		listme.append(string)
		string = self.short + "123456" + "\n"
		listme.append(string)
		string = self.short + "123456789" + "\n"
		listme.append(string)
		string = self.short + "%" + "\n"
		listme.append(string)
		string = self.short + "*" + "\n"
		listme.append(string)
		string = self.short + "&" + "\n"
		listme.append(string)
		string = self.short + "123456789" + "\n"
		listme.append(string)
		string = self.short + "1122" + "\n"
		listme.append(string)
		string = self.short + "112233" + "\n"
		listme.append(string)
		string = self.short + "11223344" + "\n"
		listme.append(string)
		string = self.short + "112234455" + "\n"
		listme.append(string)
		string = self.short + "112233445566" + "\n"
		listme.append(string)
		string = self.short + "11223344577" + "\n"
		listme.append(string)
		string = self.short + "11667788" + "\n"
		listme.append(string)
		string = self.short + "11223344556" + "\n"
		listme.append(string)
	def method_2(self, name, phone):
		listme.append("==========METHOD 2==========\n")
		space = " "

		if space in name:
			name = name.replace(" ", " ")

			for i in range(11):
				string = name + phone[i:] + "\n"
				listme.append(string)
			for j in range(11):
				string = name + family + phone[j:] + "\n"
				listme.append(string)


	def method_3(self, name, family, phone):
		listme.append("=========METHOD 3=========\n")
		string = name + " " + family
		space = " "
		self.short = ""
		if space in string:
			ll = string.split(" ")
			for j in ll:
				self.short += j[0]

		for i in range(11):
			string = self.short + phone[i:] + "\n"
			listme.append(string)
			if len(string) <= 3:
				break

	def method_4(self, name, national_id):
		listme.append("=========METHOD 4=========\n")
		space = " "
		if space in name:
			name  = name.replace(" "," ")

		for i in range(10):
			string = name + national_id[i:] + "\n"
			listme.append(string)
			if len(string) <= 3:
				break

	def method_5(self, name, family, national_id):
		listme.append("=========METHOD 5=========\n")
		space = " "
		if space in name:
			name = name.replace(" ", " ")

		string  = name + family + national_id + "\n"
		listme.append(string)
		string = name + " " + family + national_id + "\n"
		space = " "
		self.short = ""
		if space in string:
			ll = string.split(" ")
			for j in ll:
				self.short += j[0]
		string = self.short = national_id + "\n"
		listme.append(string)
		for i in range(10):
			string = self.short + national_id[i:] + "\n"
			listme.append(string)

	def method_6(self, point, phone):
		listme.append("=========METHOD 6=========\n")

		for i in range(11):
			string = point = phone[i:] + "\n"
			listme.append(string)

	def method_7(self, point):
		listme.append("=========METHOD 7=========\n")

		string = point + "1" + "\n"
		listme.append(string)
		string = point + "0" + "\n"
		listme.append(string)
		string = point + "123" + "\n"
		listme.append(string)
		string = point + "12345" + "\n"
		listme.append(string)
		string = point + "123456" + "\n"
		listme.append(string)
		string = point + "123456789" + "\n"
		listme.append(string)
		string = point + "1122" + "\n"
		listme.append(string)
		string = point + "112233" + "\n"
		listme.append(string)
		string = point + "11223344" + "\n"
		listme.append(string)
		string = point + "1122334455" + "\n"
		listme.append(string)
		string = point + "112233445566" + "\n"
		listme.append(string)
		string = point + "112236677" + "\n"
		listme.append(string)
		string = point + "122334455667788" + "\n"
		listme.append(string)
		string = point + "1122334455667" + "\n"
		listme.append(string)

	def method_8(self, name, family, date):
		listme.append("=========METHOD 8=========\n")

		string = name + date + "\n"
		listme.append(string)
		string = name + date[2:] + "\n"
		listme.append(string)

		space = " "
		if space in string:
			ll = string.split(" ")
			string = ll[0] + date + "\n"
			listme.append(string)
			string = ll[1] + date + "\n"
			listme.append(string)
		string = name + family + date + "\n"
		listme.append(string)

	def method_9(self, name, national_id):
		listme.append("=========METHOD 9=========\n")\

		string = name + national_id

		space = " "
		if space in string:
			ll = string.split(" ")
			string = ll[0] + national_id + "\n"
			listme.append(string)
			string = ll[1] + "\n"
			listme.append(string)

	def method_10(self, name, national_id):
		listme.append("=========METHOD 10=========\n")

		for i in range(11):
			string = phone[i:] + "\n"
			listme.append(string)
			if len(phone[i:]) <= 5:
				break
		for j in range(10):
			string = national_id[j:] + "\n"
			listme.append(string)
			if len(national_id[j:]) <= 5:
				break
	def method_11(self, name, phone, date, national_id):
		listme.append("=========METHOD 11=========\n")

		for i in range(4):
			for j in range(11):
				string = name[:i + 1] + phone[j:] + "\n"
				listme.append(string)

		for i in range(4):
			for j in range(10):
				string = name[:i + 1] + national_id[j:] + "\n"
				listme.append(string)

		for i in range(4):
			for j in range(4):
				string = name[:i + 1] + date[j:] + "\n"
				listme.append(string)

	def method_20(self, name):
		listme.append("=========METHOD 20=========\n")
		for k in range(1, 10000):
			for i in range(4):
				if len(str(k)) == 1:
					k = str(k)
					k = "0" + "0" + "0" + k
				if len(str(k)) == 2:
					k = str(k)
					k = "0" + "0" + k
				if len(str(k)) == 3:
					k = str(k)
					k = "0" + k
				string = name[:i + 1] + str(k) + "\n"
				if len(string) != 8:
					listme.append(string)
			string = name = str(k) + "\n"
			listme.append(string)

family = input(str("[?] Name >>> "))
name = input(str("[?] Family >>> "))
phone = input(str("[?] Phone Number >>> "))
national_id = input(str("[?] national_id >>> "))
point = input(str("[?] Mother_Name >>> "))
date = input(str("[?] Fother_Name >>> "))
# Pet = input(str("[+] Pet Name : "))

name = name.lower()
family = family.lower()
point = point.lower()
objective = Generate()

if national_id == '0':
	objective.method_1(name, family)
	objective.method_2(name, phone)
	objective.method_3(name, family, phone)
	objective.method_4(name, national_id)
	objective.method_5(name, family, national_id)
	objective.method_6(point, phone)
	objective.method_7(point)
	objective.method_8(name,family, date)
	objective.method_9(name, national_id)
	objective.method_10(phone, national_id)
	objective.method_11(name, phone, date, national_id)
	if phone == '0':
		objective.method_1(name, family)
		objective.method_2(name, phone)
		objective.method_3(name, family, phone)
		objective.method_4(name, national_id)
		objective.method_5(name, family, national_id)
		objective.method_6(point, phone)
		objective.method_7(point)
		objective.method_8(name,family, date)
		objective.method_9(name, national_id)
		objective.method_10(phone, national_id)
		objective.method_11(name, phone, date, national_id)
else:

		objective.method_1(name, family)
		objective.method_2(name, phone)
		objective.method_3(name, family, phone)
		objective.method_4(name, national_id)
		objective.method_5(name, family, national_id)
		objective.method_6(point, phone)
		objective.method_7(point)
		objective.method_8(name,family, date)
		objective.method_9(name, national_id)
		objective.method_10(phone, national_id)
		objective.method_11(name, phone, date, national_id)
		objective.method_20(name)


def process_data():
    sleep(0.07)


for _ in track(range(100), description='[green]Creact Password'):
    process_data()

i = len(listme) - 1
while i >= 0:
	if (len(listme[i]) < 7 or len(listme[i]) > 36):
		del listme[i]
	i -= 1
print(len(listme), "Creact Password :)")
for writing in listme:
	password.write(writing)

password.close()
