import random
import string

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    
    
    password = ''.join(random.choice(chars) for _ in range(length))
    
    return password

def main():
    
     length = int(input("Enter the desired length of the password: "))
    
     password = generate_password(length)
    
     print("Generated Password : ", password)

if __name__ == "__main__":
    main()