from cryptography.fernet import Fernet

def generate_key():
  key = Fernet.generate_key()

  with open('key.key', 'wb') as f:
    f.write(key)

generate_key()