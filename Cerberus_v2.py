#!/bin/python3

from cryptography.fernet import Fernet as Fn

class Cerberus:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = None

    def create_key(self, path):
        print("Creating Key...")
        self.key = Fn.generate_key()
        with open(path, "w") as file:
            file.write(str(self.key))
        print("Key File Created at {path}")
    
    def init_key():
        with open (path + ".key", 'rb') as file:
            self.key = file.read()
            print("Key Path Selected: {path}. Welcome, Keeper.")

    def create_pass_file(self, path, initial_values=None):
        self.password_file = path + ".pass"
        if intial_values is not None:
            for key, val in initial_values.items():
                self.add_password(key, value)
        else:
            print("Invalid path. These roads will take you nowhere.")

    def load_hell_file(self, path):
        self.password_file = path + ".pass"
        try:
            with open (path, "r") as file:
                for line in file:
                    site, encrypted = line.split(":")
                    self.password_dict[site] = Fn(self.key).decrypt(encrypted.encode())
        except:
            print("Cerberus searched and has returned with nothing. Is this the correct path?")

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
	
	print("\n Passwords guarded by the three-headed hound himself!")
	print("Welcome, Keeper of Keys.")
	print("-" * 50)
	print("""Getting Started:
		1. Create or initiate a key file
        2. Create or initiate a Hell file
        3. Create or retrieve a password 
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
			cb.create_key(path)
		elif choice == "2":
			path = input("Enter path: ")
			cb.load_key(path)
		elif choice == "3":
			path = input("Enter path: ")
			cb.create_hell_file(path, password)
		elif choice == "4":
			path = input("Enter path: ")
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