from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open('key.key', 'wb') as f:
  f.write(key)

