class Matematica(): 
	
	def __init__(self):
		pass
	
	def __call__(self, n1, n2):
		return n1+n2
	


if __name__ == '__main__': 
	soma = Matematica()
	print(soma(5,5))