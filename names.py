import random
def printName():
	file_name = input("Input the .txt file containing the roster: ")
	my_file = open(file_name, "r")
	
	list_names = []
	for line in my_file:
		stripped_line = line.strip()
		line_list = stripped_line.split()
		list_names.append(line_list)
		
	my_file.close()
	
	#print(list_names[0])
	string=' '.join(str(item) for item in list_names[random.randint(0,len(list_names)-1)])
	print(string)
	
	
printName();
