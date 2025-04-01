# Task-Tracker
A simple CLI task tracker/ todo list 

*(submission for https://roadmap.sh/projects/task-tracker)*

## Usage
```bash
#Adding tasks
python task-tracker add buy groceries

#Lists all the tasks
python task-tracker list

#Listing all tasks by status
python task-tracker todo
python task-tracker in-progress
python task-tracker done

#Updating tasks
python task-tracker update 1 read 10 pages

#Deleting tasks
python task-tracker delete 1

#Marking in progress or as done
python task-tracker mark-in-progress 1
python task-tracker mark-done 1
```

## Storage
Tasks are stored in a json file in the same directory as the main script with the following properties
>id:
unique and static id assigned to each task

>description:
the task itself


>status:
todo, done or in-progress


>createdAT:
time of creation	


>updatedAt:
last update




