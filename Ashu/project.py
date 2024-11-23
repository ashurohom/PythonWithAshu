task_count =int(input("Enter Task Count : "))
store_task = []

def task(task_count,store_task):
        for i in range(task_count):
            new_task =(input("Enter Your Task : "))
            store_task.append(new_task)
            print(f'Task {new_task} Added!')
task(task_count,store_task)        


# print("\nAll Tasks:")
# for i, task in enumerate(store_task, start=1):
#     print(f"Task {i}: {task}")      

        
def show_task():
     for i, task in enumerate(store_task, start=1):
        print(f"Task {i}: {task}")  
show_task()
     