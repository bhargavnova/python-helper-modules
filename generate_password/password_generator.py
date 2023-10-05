import random
import string

def generate_password(length=5, include_chars=string.ascii_lowercase):
  result_str = ''.join((random.choice(include_chars) for i in range(length)))
  print(result_str)
   

def generate_batch_passwords(amount=1, length, include_chars):
  for x in range(amount):
    generate_password(length,include_chars)