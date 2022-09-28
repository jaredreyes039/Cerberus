#!/bin/python3

from cryptography.fernet import Fernet as fn

class Cerberus:

	def __init__(self):
		self.key = None
		self.password_file = None
		self.password_dict = {}

	def create_key(self, path):
		print("Creating Key...")
		self.key = fn.generate_key()
		with open(path + ".key", "wb") as f:
				f.write(self.key)
		print("Key File Created: " + path + '.key')
    
	def load_key(self, path):
		with open (path + ".key", 'rb') as file:
			self.key = file.read()
			print('Key Selected: ' + path + '.key')

	def create_hell_file(self, path, initial_values=None):
		self.password_file = path + ".pass"
		if initial_values is not None:
			for key, val in initial_values.items():
				self.add_password(key, value)
				print("HellPass File Created: " + path + '.pass')
		else:
			print("Invalid name. These roads will take you nowhere.")

	def load_hell_file(self, path):
		self.password_file = path + '.pass'
		with open (path + '.pass', "r") as f:
			for line in f:
				site, encrypted = line.split(":")
				self.password_dict[site] = fn(self.key).decrypt(encrypted.encode())

	def add_password(self, site, password):
		    self.password_dict[site] = password
		
		    if self.password_file is not None:
			    with open(self.password_file, 'a+') as f:
				    encrypted = fn(self.key).encrypt(password.encode())
				    f.write(site + ":" + encrypted.decode() + "\n")
		    else:
			    print("Error: Key not initiated")

	def get_password(self, site):
		try:
			return self.password_dict[site]
		except:
			print("Cerberus cannot sniff out that password. Please check your entry and try again!")

def main():
	password = {}
	cb = Cerberus()
	

	print("""
_________             ___.                              
\_   ___ \  __________\_ |__   ___________ __ __  ______
/    \  \/_/ __ \_  __ \ __ \_/ __ \_  __ \  |  \/  ___/
\     \___\  ___/|  | \/ \_\ \  ___/|  | \/  |  /\___ \ 
 \______  /\___  >__|  |___  /\___  >__|  |____//____  >
        \/     \/          \/     \/                 \/ 
	""")
	
	print("\nPasswords guarded by the three-headed hound himself!\n")
	print("Welcome, Keeper of Keys.")
	print("-" * 50)
	print("""Getting Started:
		1. Create or initiate a key file
		2. Create or initiate a HellPass file
		3. Create or retrieve a password 
	""")
	print("-" * 50)
	print("""Select an Action:
		(1) Create a new key
		(2) Load existing key
		(3) Create new HellPass file
		(4) Load existing HellPass file
		(5) Add new password
		(6) Get password
		(Q) Quit
		""")
	print("-" * 50)
	
	done = False
	
	while not done:
		choice = input("Enter Selection: ")
		if choice == "1":
			path = input("Enter key name: ")
			cb.create_key(path)
		elif choice == "2":
			path = input("Enter key name: ")
			cb.load_key(path)
		elif choice == "3":
			path = input("Enter HellPass name: ")
			cb.create_hell_file(path, password)
		elif choice == "4":
			path = input("Enter HellPass name: ")
			cb.load_hell_file(path)
		elif choice == "5":
			site = input("Enter sitename: ")
			password = input("Enter password: ")
			cb.add_password(site, password)
		elif choice == "6":
			site = input("Enter sitename: ")
			print(f"Password for {site} is {cb.get_password(site)}")
		elif choice == "Q":
			done = True
			print("Hell's gates are rumbling shut. You're safe now.")
			print("Exiting Cerberus...")
		else:
			print("Invalid selection you fool!")
	
if __name__ == "__main__":
	main()