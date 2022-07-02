
z = input("[?] Do you want to use password creation for WiFi or vps and >>> ")
def pass_ghost():

	answer = input("""Choose Orphius Work:
	[+] 1. Normal Mode
	[+] 2. Choose Mode
	[+] 3. VPS Password Maker
	[+] 4. WIFI Password Maker
	[+] 5. String With Integer
	[+] 6. String And Integer
	Enter >>> """).upper() #get operator
	def normal(): #normal mode
		try: #try to run code
			chars = printable[0:94] #get all keyboard data
			length = int(input("Enter Password Lenght (If Want To Random Length, Enter 0): ")) #get length
			if length == 0: #if want to random length
				answer = input("Do You Want Choose Random Range(Y/N): ").upper() #get want choose random range
				if answer  == "Y": #if want to random length
					a = int(input("Enter Start Number: ")) #get start number
					b = int(input("Enter Stop Number: ")) #get stop number
					rand = randint(a,b) #get random number in range a to b
				elif answer == "N": #if not want choose random length
					rand = randint(8,20) #set to default random length
				else: #if entered unknown answer
					rand = randint(8,20) #again set to default random length
			count = int(input("Enter Password Count: ")) #get count of password
			file = input("Enter File Name Or Directory To Save (If Not Want Save to File, Enter NOT): ") #get want save to file
			if file.upper() == "NOT": #if not want save to file
				pass #dont execute ant code
			else: #if want save to file
				f = open(file,"a") # make or open file
				f.truncate(0) # clear file data
			start = time()
			for _ in range(count): # loop for all password count
				if length == 0:
					if answer == "Y":
						password = "".join(choice(chars) for _ in range(rand)) # make password with custom range
						rand = randint(a,b) # again set random range a to b
					else:
						password = "".join(choice(chars) for _ in range(rand)) # make password with default range
						rand = randint(8,20) # again set random range to default(8 to 20)
				else: # if not want random length
					password = "".join(choice(chars) for _ in range(length)) # make password with entered length
				print(password)
				if file.upper() != "NOT":   # if want save to file
					f.write(f"{password}\n") # print password to file
			end = time() - start
			print("".join("-" for _ in range(30))) # print separator line
			print("List Complete! :)")
			print(f"Maked {count} Password In {end} Seconds")
			if file.upper() != "NOT": #if want save to file
				print(f"Saved Password List To {file}")
			else:
				print("Dont Saved To Any File (Because You Entered NOT) :(")
			print("Enjoy! :)")
		except KeyboardInterrupt: #if entered CTRL + C (send exit request)
			print("Bye. :(")
		except ValueError: #if entered unknown answer
			print("Please Enter Integer Number")
		finally: # final block
			if file.upper() != "NOT": #if want save to file
				f.close() # close file
	def choose(): # choose mode
		try: #try execute code
			chars = input("Enter The Useable Character(a to z,0 to 9,A to Z, special character): ") #get useable character
			chars = list(chars) #set entered character as list data type
			count = int(input("Enter Password Count: ")) # get count if password
			length = int(input("Enter Password Lenght (If Want To Random Length, Enter 0): ")) #get length of password
			if length == 0: #if want random length
				answer = input("Do You Want Choose Random Range(Y/N): ").upper()
				if answer  == "Y":
					a = int(input ("Enter Start Number: "))
					b = int(input("Enter Stop Number: "))
					rand = randint(a,b)
				elif answer == "N":
					rand = randint(8,20)
				else:
					rand = randint(8,20)
			file = input("Enter File Name Or Directory To Save (If Not Want Save to File, Enter NOT): ")
			if file.upper() == "NOT":
				pass #dont execute any code
			else:
				f = open(file,"a") #open or make file
				f.truncate(0) #clear file data
			for i in range(0,len(chars) - 1):
				if " " == chars[i]: del chars[i] #remove space
			start = time()
			for _ in range(count):
				if length == 0:
					if answer == "Y":
						password = "".join(choice(chars) for _ in range(rand))
						rand = randint(a,b)
					else:
						password = "".join(choice(chars) for _ in range(rand))
						rand = randint(8,20)
				else:
					password = "".join(choice(chars) for _ in range(length))
				print(password)
				if file.upper() != "NOT":
					f.write(f"{password}\n")
			end = time() - start
			print("".join("-" for _ in range(30)))
			print("List Complete! :)")
			print(f"Maked {count} Password In {end} Seconds")
			if file.upper() != "NOT":
				print(f"Saved Password List To {file}")
			else:
				print("Dont Saved To Any File (Because You Entered NOT) :(")
			print("Enjoy! :)")
		except KeyboardInterrupt:
			print("Bye. :(")
		except ValueError:
			print("Please Enter Good Answer")
		finally:
			if file.upper() != "NOT":
				f.close()
	def vps():
		try:
			raw = [ #add more word into this list
				"admin",
				"network",
				"server",
				"administrator",
				"administrator".upper(),
				"@dmin",
				"@admin",
				"MyP@ssw0rd",
				"P@$$word",
				"P@$$worD",
				"P@$VVORD",
				"P@$$w0rd",
				"P@$VVORD",
				"pass",
				"P@ssw0rD",
				"POWER",
				"PC",
				"abc",
				"ABC",
				"vps",
				"Vps",
				"VPS",
				"$Y$TEM",
				"123",
				"2020",
				"Garena",
				"com",
				"Mirana",
				"google",
				"GOOGLE",
				"Google",
				"Shadow",
				"secret",
				"Secret",
				"SECRET"
				"temp",
				"TEMP",
				"Temp",
				"user",
				"User",
				"USER",
				"test",
				"Test",
				"TEST",
				"welcome",
				"Welcome",
				"WELCOME",
				"desktop",
				"Desktop",
				"DESKTOP",
				"remote",
				"Remote",
				"REMOTE",
				"password",
				"Password",
				"PASSWORD",
				"pc",
				"Pc",
				"manager",
				"Manager",
				"MANAGER",
				"support",
				"Support",
				"SUPPORT",
				"homegroup",
				"Homegroup",
				"homeGroup",
				"HomeGroup",
				"adm!in",
				"Adm!n",
				"ADM!N",
				"client",
				"Client",
				"CLIENT",
				"m@n@ger",
				"exit",
				"EXIT",
				"Exit",
				"webadmin",
				"Webadmin",
				"webAdmin",
				"WebAdmin",
				"WEBADMIN",
				"root",
				"Root",
				"ROOT",
				"info",
				"Info",
				"INFO",
				"@dm!n",
				"operator",
				"Operator",
				"OPERATOR",
				"panel",
				"Panel",
				"PANEL",
				"Administrador",
				"Administrator",
				"config",
				"Config",
				"CONFIG",
				"member",
				"Member",
				"MEMBER",
				"online",
				"Online",
				"ONLINE",
				"ghost",
				"Ghost",
				"GHOST",
				"asus",
				"Asus",
				"ASUS",
				"4dmin",
				"@dm!n",
				"Storage",
				"storage",
				"STORAGE",
				"personal",
				"Personal",
				"PERSONAL",
				"cube",
				"Cube",
				"CUBE",
				"setpassword",
				"setpassword".title(),
				"setpassword".upper(),
				"portable",
				"portable".title(),
				"portable".upper()
			]
			count = int(input("Enter Count : "))
			file = input("Enter File Name Or Directory To Save (If Not Want Save to File, Enter NOT): ")
			if file.upper() == "NOT":
				pass
			else:
				f = open(file,"a")
				f.truncate(0)
			i = 0
			ii = 0
			def wrt(fle, msg):
				if fle.upper() != "NOT":
					f.write(msg + "\n")
			start = time()
			while True:
				i += 1
				if i > count: break
				for x in raw:
					ii += 1
					for _ in range(100):
						num = f"{randint(1,9999)}{x}"
						print(num)
						wrt(file, num)
					for _ in range(5):
						num = f"{x}@{randint(1,9999)}"
						print(num)
						wrt(file, num)
					for _ in range(5):
						num = f"{x}@{randint(1,9999)}"
						print(num)
						wrt(file, num)
					print(f"{x}{i}")
					wrt(file, f"{x}{i}")
					print(f"{x}@{i}")
					wrt(file, f"{x}@{i}")
					print(f"{x}{i}{i}{i}")
					wrt(file , f"{x}{i}{i}{i}")
					print(f"{x}{i}{i}{i}{i}")
					wrt(file , f"{x}{i}{i}{i}{i}")
					print(f"{x}{i}{i}")
					wrt(file , f"{x}{i}{i}")
					print(f"{x}@{i}{i}{i}")
					wrt(file , f"{x}@{i}{i}{i}")
					print(f"{x}@{i}{i}")
					wrt(file , f"{x}@{i}{i}")
					print(f"{x}@{i}{i}{i}{i}")
					wrt(file,f"{x}@{i}{i}{i}{i}")
					print(f"{ii}{ii}{ii}")
					wrt(file, f"{ii}{ii}{ii}")
					print(f"{ii}{ii}{ii}{ii}")
					wrt(file , f"{ii}{ii}{ii}{ii}")
					print(f"{x}{ii}")
					wrt(file, f"{x}{ii}")
					print(f"{x}@{ii}")
					wrt(file, f"{x}@{ii}")
					print(f"{x}{ii}{ii}{ii}")
					wrt(file, f"{x}{ii}{ii}{ii}")
					print(f"{x}{ii}{ii}{ii}{ii}")
					wrt(file , f"{x}{ii}{ii}{ii}{ii}")
					print(f"{x}{ii}{ii}")
					wrt(file,f"{x}{ii}{ii}")
					print(f"{x}@{ii}{ii}{ii}")
					wrt(file, f"{x}@{ii}{ii}{ii}")
					print(f"{x}@{ii}{ii}")
					wrt(file, f"{x}@{ii}{ii}")
					print(f"{x}@{ii}{ii}{ii}{ii}")
					wrt(file, f"{x}@{ii}{ii}{ii}{ii}")
					print(f"{x}@{ii}")
					wrt(file, f"{x}@{ii}")
					print(f"{x}#{ii}")
					wrt(file, f"{x}#{ii}")
					print(f"{x}#{ii}{ii}{ii}")
					wrt(file, f"{x}#{ii}{ii}{ii}")
					print(f"{x}#{ii}{ii}")
					wrt(file, f"{x}#{ii}{ii}")
					print(f"{x}#{ii}{ii}{ii}{ii}")
					wrt(file,f"{x}#{ii}{ii}{ii}{ii}")
					print(f"{x}#{ii}")
					wrt(file, f"{x}#{ii}")
					print(f"{x}#{i}")
					wrt(file, f"{x}#{i}")
					print(f"{x}#{i}{i}{i}")
					wrt(file, f"{x}#{i}{i}{i}")
					print(f"{x}#{i}{i}")
					wrt(file, f"{x}#{i}{i}")
					print(f"{x}#{i}{i}{i}{i}")
					wrt(file, f"{x}#{i}{i}{i}{i}")
					for _ in range(5):
						num = f"{x}#{randint(1,9999)}"
						print(num)
						wrt(file,num)
					print(f"{x}+{ii}")
					wrt(file , f"{x}+{ii}")
					print(f"{x}+{ii}{ii}{ii}")
					wrt(file, f"{x}+{ii}{ii}{ii}")
					print(f"{x}+{ii}{ii}")
					wrt(file, f"{x}+{ii}{ii}")
					print(f"{x}+{ii}{ii}{ii}{ii}")
					wrt(file, f"{x}+{ii}{ii}{ii}{ii}")
					print(f"{x}+{ii}")
					wrt(file, f"{x}+{ii}")
					print(f"{x}+{i}")
					wrt(file, f"{x}+{i}")
					print(f"{x}+{i}{i}{i}")
					wrt(file, f"{x}+{i}{i}{i}")
					print(f"{x}+{i}{i}")
					wrt(file, f"{x}+{i}{i}")
					print(f"{x}+{i}{i}{i}{i}")
					wrt(file, f"{x}+{i}{i}{i}{i}")
					for _ in range(5):
						num = f"{x}+{randint(1,9999)}"
						print(num)
						wrt(file,num)
					print(f"{x}!{ii}")
					wrt(file, f"{x}!{ii}")
					print(f"{x}!{ii}{ii}{ii}")
					wrt(file, f"{x}!{ii}{ii}{ii}")
					print(f"{x}!{ii}{ii}")
					wrt(file, f"{x}!{ii}{ii}")
					print(f"{x}!{ii}{ii}{ii}{ii}")
					wrt(file, f"{x}!{ii}{ii}{ii}{ii}")
					print(f"{x}!{ii}")
					wrt(file, f"{x}!{ii}")
					print(f"{x}!{i}")
					wrt(file, f"{x}!{i}")
					print(f"{x}!{i}{i}{i}")
					wrt(file, f"{x}!{i}")
					print(f"{x}!{i}{i}")
					wrt(file,f"{x}!{i}{i}")
					print(f"{x}!{i}{i}{i}{i}")
					wrt(file, f"{x}!{i}{i}{i}{i}")
					for _ in range(5):
						num = f"{x}!{randint(1,9999)}"
						print(num)
						wrt(file, num)
					print(f"{x}.{ii}")
					wrt(file, f"{x}.{ii}")
					print(f"{x}.{ii}{ii}{ii}")
					wrt(file, f"{x}.{ii}{ii}{ii}")
					print(f"{x}.{ii}{ii}")
					wrt(file, f"{x}.{ii}{ii}")
					print(f"{x}.{ii}{ii}{ii}{ii}")
					wrt(file, f"{x}.{ii}{ii}{ii}{ii}")
					print(f"{x}.{ii}")
					wrt(file, f"{x}.{ii}")
					print(f"{x}.{i}")
					wrt(file, f"{x}.{i}")
					print(f"{x}.{i}{i}{i}")
					wrt(file, f"{x}.{i}{i}{i}")
					print(f"{x}.{i}{i}")
					wrt(file, f"{x}.{i}{i}")
					print(f"{x}.{i}{i}{i}{i}")
					wrt(file, f"{x}.{i}{i}{i}{i}")
					for _ in range(5):
						num = f"{x}.{randint(1,9999)}"
						print(num)
						wrt(file, num)
					print(f"{x}*{ii}")
					wrt(file, f"{x}*{ii}")
					print(f"{x}*{ii}{ii}{ii}")
					wrt(file, f"{x}*{ii}{ii}{ii}")
					print(f"{x}*{ii}{ii}")
					wrt(file, f"{x}*{ii}{ii}")
					print(f"{x}*{ii}{ii}{ii}{ii}")
					wrt(file, f"{x}*{ii}{ii}{ii}{ii}")
					print(f"{x}*{ii}")
					wrt(file, f"{x}*{ii}")
					print(f"{x}*{i}")
					wrt(file, f"{x}*{i}")
					print(f"{x}*{i}{i}{i}")
					wrt(file, f"{x}*{i}{i}{i}")
					print(f"{x}*{i}{i}")
					wrt(file, f"{x}*{i}{i}")
					print(f"{x}*{i}{i}{i}{i}")
					wrt(file, f"{x}*{i}{i}{i}{i}")
					for _ in range(5):
						num = f"{x}*{randint(1,9999)}"
						print(num)
						wrt(file, num)
					print(f"{x}_{ii}")
					wrt(file, f"{x}_{ii}")
					print(f"{x}_{ii}{ii}{ii}")
					wrt(file, f"{x}_{ii}{ii}{ii}")
					print(f"{x}_{ii}{ii}")
					wrt(file, f"{x}_{ii}{ii}")
					print(f"{x}_{ii}{ii}{ii}{ii}")
					wrt(file, f"{x}_{ii}{ii}{ii}{ii}")
					print(f"{x}_{ii}")
					wrt(file, f"{x}_{ii}")
					print(f"{x}_{i}")
					wrt(file, f"{x}_{i}")
					print(f"{x}_{i}{i}{i}")
					wrt(file, f"{x}_{i}{i}{i}")
					print(f"{x}_{i}{i}")
					wrt(file, f"{x}_{i}{i}")
					print(f"{x}_{i}{i}{i}{i}")
					wrt(file, f"{x}_{i}{i}{i}{i}")
					for _ in range(5):
						num = f"{x}_{randint(1,9999)}"
						print(num)
						wrt(file, num)
					print(f"{x}-{ii}")
					wrt(file, f"{x}-{ii}")
					print(f"{x}-{ii}{ii}{ii}")
					wrt(file, f"{x}-{ii}{ii}{ii}")
					print(f"{x}-{ii}{ii}")
					wrt(file, f"{x}-{ii}{ii}")
					print(f"{x}-{ii}{ii}{ii}{ii}")
					wrt(file, f"{x}-{ii}{ii}{ii}{ii}")
					print(f"{x}-{ii}")
					wrt(file, f"{x}-{ii}")
					print(f"{x}-{i}")
					wrt(file, f"{x}-{i}")
					print(f"{x}-{i}{i}{i}")
					wrt(file, f"{x}-{i}{i}{i}")
					print(f"{x}-{i}{i}")
					wrt(file, f"{x}-{i}{i}")
					print(f"{x}-{i}{i}{i}{i}")
					wrt(file,f"{x}-{i}{i}{i}{i}")
					for _ in range(5):
						num = f"{x}-{randint(1,9999)}"
						print(num)
						wrt(file, num)
			end = time() - start
			print("".join("-" for _ in range(30)))
			print("List Complete! :)")
			print(f"Maked {count} Password In {end} Seconds")
			if file.upper() != "NOT":
				print(f"Saved Password List To {file}")
			else:
				print("Dont Saved To Any File (Because You Entered NOT) :(")
			print("Enjoy! :)")
		except KeyboardInterrupt:
			print("Bye. :(")
		except ValueError:
			print("Please Enter Good Answer")
			exit()
		finally:
			if file.upper() != "NOT":
				f.close()
	def wifi():
		try:
			length = int(input("Enter Password Lenght (If Want To Random Length, Enter 0): ")) #get length
			if length == 0: #if want to random length
				answer = input("Do You Want Choose Random Range(Y/N): ").upper() #get want choose random range
				if answer  == "Y": #if want to random length
					a = int(input("Enter Start Number: ")) #get start number
					b = int(input("Enter Stop Number: ")) #get stop number
					rand = randint(a,b) #get random number in range a to b
				elif answer == "N": #if not want choose random length
					rand = randint(8,20) #set to default random length
				else: #if entered unknown answer
					rand = randint(8,20) #again set to default random length
			count = int(input("Enter Password Count: ")) #get count of password
			file = input("Enter File Name Or Directory To Save (If Not Want Save to File, Enter NOT): ") #get want save to file
			if file.upper() == "NOT": #if not want save to file
				pass #dont execute ant code
			else: #if want save to file
				f = open(file,"a") # make or open file
				f.truncate(0) # clear file data
			start = time()
			for _ in range(count): # loop for all password count
				if length == 0:
					if answer == "Y":
						password = "".join(choice(digits) for _ in range(rand)) # make password with custom range
						rand = randint(a,b) # again set random range a to b
					else:
						password = "".join(choice(digits) for _ in range(rand)) # make password with default range
						rand = randint(8,20) # again set random range to default(8 to 20)
				else: # if not want random length
					password = "".join(choice(digits) for _ in range(length)) # make password with entered length
				print(password)
				if file.upper() != "NOT":   # if want save to file
					f.write(f"{password}\n") # print password to file
			end = start - time()
			print("".join("-" for _ in range(30))) # print separator line
			print("List Complete! :)")
			print(f"Maked {count} Password In {end} Seconds")
			if file.upper() != "NOT": #if want save to file
				print(f"Saved Password List To {file}")
			else:
				print("Dont Saved To Any File (Because You Entered NOT) :(")
			print("Enjoy! :)")
		except KeyboardInterrupt:
			print("Bye. :(")
		except ValueError:
			print("Please Enter Good Answer")
			exit()
		finally:
			if file.upper() != "NOT":
				f.close()
	def string():
		try:
			start = input("Enter Start Word: ")
			end = input("Enter End Word: ")
			count = int(input("Enter Password Count(If Want Choose Range, Enter 0): "))
			if count == 0:
				a = int(input("Enter Start Number: "))
				b = int(input("Enter End Number: "))
			else:
				a = 1
				b = count
			file = input("Enter File Name Or Directory To Save (If Not Want Save to File, Enter NOT): ")
			if file.upper() == "NOT": #if not want save to file
				pass #dont execute ant code
			else: #if want save to file
				f = open(file,"a") # make or open file
				f.truncate(0) # clear file data
			start = time()
			for i in range(a,b + 1):
				print(f"{start}{i}{end}")
				if file.upper() != "NOT":
					f.write(f"{start}{i}{end}\n")
			end = time() - start
			print("".join("-" for _ in range(30))) # print separator line
			print("List Complete! :)")
			print(f"Maked {count} Password In {end} Seconds")
			if file.upper() != "NOT": #if want save to file
				print(f"Saved Password List To {file}")
			else:
				print("Dont Saved To Any File (Because You Entered NOT) :(")
			print("Enjoy! :)")
		except ValueError:
			print("Please Enter Good Answer")
		except KeyboardInterrupt:
			print("Bye. :(")
		finally:
			if file.upper() != "NOT":
				f.close()
	def str_int():
		try:
			word = input("Enter Word: ")
			count = int(input("Enter Password Count(If Want Choose Range, Enter 0): "))
			if count == 0:
				a = int(input("Enter Start Number: "))
				b = int(input("Enter End Number: "))
			else:
				a = 1
				b = count
			file = input("Enter File Name Or Directory To Save (If Not Want Save to File, Enter NOT): ")
			if file.upper() == "NOT":
				pass
			else:
				f = open(file,"a")
				f.truncate(0)
			start = time()
			for i in range(a,b + 1):
				print(f"{word}{i}")
				if file.upper() != "NOT":
					f.write(f"{word}{i}\n")
			end = time() - start
			print("".join("-" for _ in range(30))) # print separator line
			print("List Complete! :)")
			print(f"Maked {count} Password In {end} Seconds")
			if file.upper() != "NOT": #if want save to file
				print(f"Saved Password List To {file}")
			else:
				print("Dont Saved To Any File (Because You Entered NOT) :(")
			print("Enjoy! :)")
		except ValueError:
			print("Please Enter Good Answer")
		except KeyboardInterrupt:
			print("Bye. :(")
		finally:
			if file.upper() != "NOT":
				f.close()
	def merge():
		a = randint(1,6)
		if a == "1":
			task = Process(target=normal())
		elif a == "2":
			task = Process(target=choose())
		elif a == "3":
			task = Process(target=vps())
		elif a == "4":
			task = Process(target=wifi())
		elif a == "5":
			task = Process(target=string())
		elif a == "6":
			task = Process(target=str_int())

	if answer == "1":
		task = Process(target=normal())
	elif answer == "2":
		task = Process(target=choose())
	elif answer == "3":
		task = Process(target=vps())
	elif answer == "4":
		task = Process(target=wifi())
	elif answer == "5":
		task = Process(target=string())
	elif answer == "6":
		task = Process(target=str_int())
	else:
		merge()
