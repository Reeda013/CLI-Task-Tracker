import sys, os
import time
import json

def add(args):
    
    description = " ".join(args[2:])

    #gets the tasks if file exists if not it initializes it
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            try:
                tasks = json.load(file)

            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []
    
    #Gets the appropriate id
    if tasks:
        max_id = max(task["id"] for task in tasks)
    else:
        max_id = 0

    #Data concerning the task
    task = {"id": max_id+1,
              "description": description,
              "status": "todo",
              "createdAt": time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()),
              "updatedAt": time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())}
    
    tasks.append(task)

    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
    
    print(f"{description} added with id: {max_id}")

def list(args):

    #Main skeleton
    if os.path.exists("tasks.json"):    

        with open("tasks.json", "r") as file:
            try:
                tasks = json.load(file)     
                if tasks:        

                        try:
                            printed = False #Flag to check if there was a print
                            for task in tasks:
                                #Check to see if there was more than the 
                                # desired number of arguments
                                if len(args)>3:
                                    print("Invalid arguments")
                                    break

                                status = args[2]
                                
                                #Check if the status is one of these 3
                                if status not in {"todo", "done", "in-progress"}:
                                    print("Invalid argument")
                                    break 
                                
                                #Print the tasks with the said status
                                if task["status"] == status:
                                    print(f"{task["id"]} - {task["description"]}")
                                    printed = True

                            if not printed: #if there was no print
                                print(f"No tasks marked as {status}")

                        except IndexError:    #if there is no argument
                        #Get the informations needed for each task
                            for task in tasks:
                                print(f"{task["id"]} - {task["description"]} : {task["status"]} ")
                else:   #tasks list is empty
                    print("No tasks to be listed")

            except json.JSONDecodeError:    #Json file is empty or corrupted
                print("No tasks to be shown")
    else:   #Json file doesn't exist
        print("No tasks to be shown")


#handling and calling each command
def main():
    if len(sys.argv) >= 2:
        command = sys.argv[1]
        if command == "add":
            add(sys.argv)
        elif command == "list":
            list(sys.argv)
        
        else:
            print(f"Unkown command: {command}")
    else:
        print("No command specified")

main()

