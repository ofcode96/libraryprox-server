from passlib.context import CryptContext
from passlib.handlers.bcrypt import bcrypt

password_context = CryptContext(schemes=['bcrypt'],deprecated='auto')

class Hasher :
   @staticmethod
   def verify_password (plain_pass,hashed_pass):
      return password_context.verify(plain_pass,hashed_pass)
   
   
   @staticmethod
   def get_password_hash (password):
      return password_context.hash(password)
