import json

print("Students record")

running = True
saved = False
modified = False
available_commands = """Available commands:
	insert <item>
	remove <item>
	list
	help
	exit"""
record = []

def askyesno(prompt):
	choice = input(prompt)
	return choice == "y" or choice == "Y"

def save():
	filename = "STUDENTS.RCRD"
	with open(filename, "w") as file:
		file.write(json.dumps(record))
		print(f"Record written to '{filename}'!")

while running:
	user_input = input("Enter a commmand: ")
	command_components = user_input.split(" ")
	command = command_components[0]

	if user_input == "":
		continue

	if command == "help" or command == "h":
		print(available_commands)
	elif command == "insert" or command == "i":
		modified = True

		if len(command_components) > 1:
			record.append(command_components[1])
			print(f"Inserted '{command_components[1]}'. Record size is now {len(record)}")
		else:
			print("Enter item to insert")
	elif command == "list" or command == "l":
		print("Listing record items...")
		if len(record) == 0:
			print("No items.")
		else:
			print(*record, sep=', ')
	elif command == "save" or command == "s":
		save()
		saved = True
		modified = False 
	elif command == "remove" or command == "r":
		to_remove = command_components[1]
		if to_remove not in record:
			print(f"'{to_remove}' is not in record!")
		else:
			record.remove(to_remove)
	elif command == "exit" or command == "e":
		if modified and not saved:
			if askyesno("Do you want to save? "):
				save()

		print("Bye")
		exit(0)
	else:
		print(f"Unknown command {command}")