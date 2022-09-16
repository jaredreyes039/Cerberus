#!/bin/python3

from cryptography.fernet import Fernet as fn

class Cerberus:
	
	def __init__(self):
		self.key = None
		self.password_file = None
		self.password_dict = {}
		
	def create_key(self, path):
		self.key = fn.generate_key()
		with open(path, 'wb') as f:
			f.write(self.key)

	def load_key(self, path):
		with open(path, 'rb') as f:
			self.key = f.read()
			print("Key Loaded")
	
	def create_hell_file(self, path, initial_values=None):
		self.password_file = path
		
		if initial_values is not None:
			for key, value in initial_values.items():
				self.add_password(key, value)
				
	def load_hell_file(self, path):
		self.password_file = path
		with open(path, 'r') as f:
			for line in f:
				site, encrypted = line.split(":")
				self.password_dict[site] = fn(self.key).decrypt(encrypted.encode())
				print("Pass File Loaded...")
	def add_password(self, site, password):
		self.password_dict[site] = password
		
		if self.password_file is not None:
			with open(self.password_file, 'a+') as f:
				encrypted = fn(self.key).encrypt(password.encode())
				f.write(site + ":" + encrypted.decode() + "\n")
		else:
			print("Error: Key not initiated")
				
	def get_password(self, site):
		return self.password_dict[site]
	
			
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
	
	print("\n Passwords protected by you, for you. \n Security made simple, security made personal, sercurity guarded by Cerberus.")
	
	print("-" * 50)
	print("""Getting Started:
		1. Create or Load an Encryption Key
		2. Create or Load Password file w/ Current Key
		3. Create Passwords
	""")
	print("-" * 50)
	print("""Select an Action:
		(1) Create a new key
		(2) Load existing key
		(3) Create new Hell file
		(4) Load existing Hell file
		(5) Add new password
		(6) Get password
		(Q) Quit
		""")
	print("-" * 50)
	
	done = False
	
	while not done:
		choice = input("Enter Selection: ")
		if choice == "1":
			path = input("Enter path: ")
			try:
				cb.create_key(path)
			except:
				print("Error: Path not found")
		elif choice == "2":
			path = input("Enter path: ")
			try:
				cb.load_key(path)
			except:
				print("Error: Path not found")
		elif choice == "3":
			path = input("Enter path: ")
			try:
				cb.create_hell_file(path, password)
			except:
				print("Error: Could not find path or no passwords are entered")
		elif choice == "4":
			path = input("Enter path: ")
			try:
				cb.load_hell_file(path)
			except:
				print("Error: Path not found")
		elif choice == "5":
			site = input("Enter sitename: ")
			password = input("Enter password: ")
			try:
				cb.add_password(site, password)
			except:
				print("Error: Invalid input")
		elif choice == "6":
			site = input("Enter sitename: ")
			try:
				print(f"Password for {site} is {cb.get_password(site)}")
			except:
				print("Password not found")
		elif choice == "Q":
			done = True
			print("Hell's gates are rumbling shut. You're safe now.")
			print("Exiting Cerberus...")
		else:
			print("Invalid selection you fool!")
	
if __name__ == "__main__":
	main()
	
	
	
