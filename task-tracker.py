import sys, os
import time
import json

def add(args):
    
    if len(args) >= 3:
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
        
        print(f"{description} added with id: {max_id+1}")
    else:
        print("No tasks to be added")

def list(args):

    #Main skeleton
    if os.path.exists("tasks.json"):    

        with open("tasks.json", "r") as file:
            try:
                tasks = json.load(file)     
                if tasks:        

                        try:
                            printed = False 
                            #Flag to check if there was a print
                            for task in tasks:
                                #Check to see if there was more than the 
                                # desired number of arguments
                                if len(args)>3:
                                    print("Invalid arguments")
                                    return

                                status = args[2]
                                
                                #Check if the status is one of these 3
                                if status not in {"todo", "done", "in-progress"}:
                                    print("Invalid arguments")
                                    return
                                
                                #Print the tasks with the said status
                                if task["status"] == status:
                                    print(f"{task["id"]} - {task["description"]}")
                                    printed = True

                            if not printed: 
                                #if there was no print
                                print(f"No tasks marked as {status}")
                                return

                        except IndexError:    
                            #if there is no argument
                            #Get the informations needed for each task
                            for task in tasks:
                                print(f"{task["id"]} - {task["description"]} : {task["status"]} ")
                else:   
                    #tasks list is empty
                    print("No tasks to be listed")

            except json.JSONDecodeError:    
                #Json file is empty or corrupted
                print("No tasks to be shown")
    else:   
        #Json file doesn't exist
        print("No tasks to be shown")


def update(args):
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            try:
                tasks = json.load(file)
                
                if len(args) <= 3:
                    print(f"not enough arguments")
                    return
                
                id = args[2]
                #Check if id is valid
                if not id.isdigit():
                    print(f"Invalid id: {id}")  
                    return

                description = " ".join(args[3:])
            
                #To check if we have found the correspondant task
                found = False 
                #Loop over tasks until task with correspondant id is found
                #Update the description and the last updated time
                for task in tasks:
                    if task["id"] == int(id):
                        task["description"] = description
                        task["updatedAt"] = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
                        found = True
                        break
                #If we loop over all the task and we don't find a correspondant id
                #We return a message
                if not found:
                    print(f"No task assigned to id: {id}")
                    return

                #Writing in the Json + confirmation message
                with open("tasks.json", "w") as file:           
                    json.dump(tasks, file, indent=4)    
                    print(f"changed {id} to {description}")
            
            #In case file is corrupted
            except json.JSONDecodeError:
                print("No task to be updated")
    #In case there is no file
    else:
        print("No tasks to be updated")
                    
def delete(args):
    if os.path.exists("tasks.json"):
        try:
            with open("tasks.json", "r") as file:
                tasks = json.load(file)
            
            if not tasks:
                print("No tasks to delete")
                return
            
            #Check if Id was given
            elif len(args) <= 2:
                print("Not enough arguments")
                return
            
            #Check if Id is valid
            elif not args[2].isdigit():
                print(f"Invalid Id: {args[2]}")
                return
            #Check if there is too many arguments
            elif len(args) >= 4:
                print(f"Invalid arguments: {" ".join(args[3:])}")
                return
            
            id = args[2]
            found = False

            #Iterate over each task
            for i,task in enumerate(tasks):
                #once we found it we delete it
                if task["id"] == int(id):
                    found = True
                    del tasks[i]
                    break
            
            if not found:
                print(f"No task with Id: {id}")
                return
           
            with open("tasks.json", "w") as file:
                json.dump(tasks, file, indent=4)
                print("Task deleted successfully")

        except json.JSONDecodeError:
            print("No tasks to be deleted")

    else:
        print("No tasks to be deleted")


def in_progress(args):

    if not os.path.exists("tasks.json"):
        print("No tasks to mark in progress")
        return

    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        #Base cases
        if not tasks:
            print("No tasks to mark in progress")
            return
        
        elif len(args) <= 2:
            print("Not enough arguments")
            return
        
        elif len(args) > 3:
            print("Operation supports 1 argument only")
            return
        
        elif not args[2].isdigit():
            print("Invalid Id")
            return
        
        id = args[2]
        found = False

        for task in tasks:
            if task["id"] == int(id):
                task["status"] = "in-progress"
                task["updatedAt"] = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
                found = True
                break
        
        if not found:
            print(f"No task with Id: {id}")
            return
        
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
            print(f"Marked {task["description"]} as in progress")

    except json.JSONDecodeError:
        print("No tasks to mark in progress")



#handling and calling each command
def main():
    if len(sys.argv) >= 2:
        command = sys.argv[1]
        if command == "add":
            add(sys.argv)
        elif command == "list":
            list(sys.argv)
        elif command == "update":
            update(sys.argv)
        elif command == "delete":
            delete(sys.argv)
        elif command == "mark-in-progress":
            in_progress(sys.argv)
        else:
            print(f"Unkown command: {command}")
    else:
        print("No command specified")

main()

