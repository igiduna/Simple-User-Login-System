users = []
passwords = []

def baby():
    print("I LOVE YOU BABY")

def login():
    username = input("\nUser: ")
    password = input("Password: ")

    for x in range(len(users)):
        if username == users[x] and password == passwords[x]:
            print("\nWelcome, " + username)
            break
    else:
        print("\nAccount doesn't exist")


def register():
    username = input("User: ")

    if username in users:
        print("\nThis Account Already Exists!")
        return

    password = input("Password: ")

    users.append(username)
    passwords.append(password)

    print("\nAccount registered successfully!")


while True:
    choice = int(input("""
\n[1] Login  
[2] Register
-> """))

    if choice == 1:
        login()
    elif choice == 2:
        register()

