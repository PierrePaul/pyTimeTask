def commands():
	commands = ['search', 'commands', 'details']
	return commands

def search(string):
	string = str(string)
	return 'task/search=' + 	

def details(taskId):
	return 'task/?localid=' + str(int(taskId))
