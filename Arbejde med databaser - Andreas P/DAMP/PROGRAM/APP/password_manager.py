from cryptography.fernet import Fernet


def read_key():
  with open('./DATA/key.key', 'rb') as f:
    key = f.read()
  
  return key


def generate_key():
  key = Fernet.generate_key()

  with open('./DATA/key.key', 'wb') as f:
    f.write(key)