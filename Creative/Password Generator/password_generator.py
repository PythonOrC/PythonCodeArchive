from random import randint
from time import localtime
class passwordGen():
	def __init__(self, purpose='Unspecified', pswd_len=12, file_path='E:\Personal\Python\Creative\generatedPassword.txt'):

		self.weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
		self.Months = ['Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'Jun.', 'Jul.', 'Aug.', 'Sep.', 'Oct.', 'Nov.', 'Dec.']
		self.lowercase = [chr(i) for i in range(97, 123)]
		self.uppercase = [chr(i) for i in range(65, 91)]
		self.numbers = [str(i) for i in range(10)]
		self.random_list = self.lowercase + self.uppercase + self.numbers
		self.purpose = purpose
		self.pswd_len = pswd_len
		self.file_path = file_path

		self.generate()
	
	def generate(self):
		self.pswd = [self.random_list[randint(0, len(self.random_list)-1)] for i in range(self.pswd_len)]
		self.pswd = ''.join(self.pswd)

		self.save()
	
	def save(self):
		with open(self.file_path, 'a') as f:
			f.write(f'\
Time: {localtime().tm_hour}:{localtime().tm_min} on {self.weekdays[localtime().tm_wday]}, {self.Months[localtime().tm_mon-1]} {localtime().tm_mday}, {localtime().tm_year}\n\
Purpose: {self.purpose} \n\
Length: {self.pswd_len} \n\
Password: {self.pswd}\n\n\n\
')

		print(f'\nSaved password "{self.pswd}" to "{self.file_path}"')
		return

if __name__ == '__main__':
	purpose = input('Purpose: ')
	length = int(input('Password Length: '))
	gen = passwordGen(purpose=purpose, pswd_len=length)