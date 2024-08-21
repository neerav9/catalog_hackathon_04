import random
import getpass
import hashlib
import smtplib
from email.mime.text import MIMEText

users_db = {
    "Neerav": {
        "password": hashlib.sha256("Neerav@123".encode()).hexdigest(),
        "security_question": "What is the name of your pet?",
        "security_answer": hashlib.sha256("Tyson".encode()).hexdigest(),
        "email": "nuppu2@gitam.in"
    }
}

def send_otp(email):
    otp = random.randint(100000, 999999)
    msg = MIMEText(f"Your OTP is: {otp}")
    msg['Subject'] = 'Your OTP Code'
    msg['From'] = 'your-email@example.com'
    msg['To'] = email

    print(f"OTP sent to {email} (for the sake of this example, the OTP is {otp})")
    return otp

def authenticate_user():
    username = input("Enter your username: ")
    if username not in users_db:
        print("Invalid username!")
        return False
    
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    if users_db[username]['password'] != hashed_password:
        print("Invalid password!")
        return False
    
    print("Basic Authentication successful!")

    otp = send_otp(users_db[username]['email'])
    entered_otp = int(input("Enter the OTP sent to your email: "))
    
    if entered_otp != otp:
        print("Invalid OTP!")
        return False
    
    print("Two-Factor Authentication successful!")
    
    print(f"Security Question: {users_db[username]['security_question']}")
    answer = getpass.getpass("Enter your answer: ")
    hashed_answer = hashlib.sha256(answer.encode()).hexdigest()
    
    if users_db[username]['security_answer'] != hashed_answer:
        print("Incorrect answer to security question!")
        return False
    
    print("Security Question Authentication successful!")
    
    return True

def main():
    print("Welcome to the Three-Level Password System")
    
    if authenticate_user():
        print("Access Granted!")
    else:
        print("Access Denied!")

if __name__ == "__main__":
    main()
