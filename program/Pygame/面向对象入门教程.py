class MyDog:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def bark(self):
		print('汪汪汪，我是'+ str(self.name)+'，''我的年龄是'+str(self.age))
	
	
	
	

a = MyDog('Tom',11)

print(a.name)
print(a.age)

a.bark()
