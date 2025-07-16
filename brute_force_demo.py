# brute_force_demo.py

import time

# Mock login function simulating password check
def login(username, password):
    # In real life, you'd check a database or an API
    correct_password = "SecurePass123"
    return password == correct_password

def brute_force(username, password_list):
    for pwd in password_list:
        print(f"Trying password: {pwd}")
        if login(username, pwd):
            print(f"Password found! '{pwd}' is correct for user '{username}'")
            return pwd
        time.sleep(0.5)  # Slow down attempts for demo purposes
    print("Password not found in list.")
    return None

if __name__ == "__main__":
    user = input("Enter username to brute force: ")
    # Sample password list; in real tests, use larger wordlists
    passwords = ["password", "123456", "admin", "letmein", "SecurePass123", "qwerty"]

    brute_force(user, passwords)
