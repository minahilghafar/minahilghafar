from Task import Task
from User import User

class Task_Management(Task,User):
    def __init__(self):
        Task.__init__(self,'', 'Incomplete','')
        User.__init__(self,'',0,'')
        self.history = {}
    def display_all_task(self):
        if not self.task:
            print('Task list is empty')
        else:
            print('\n ***** Current Task List ***** \n')
            for key in self.task.keys():
                print(f'Name: {self.task[key]["Name"]}, Status: {self.task[key]["Status"]},'
                f' Date: {self.task[key]["Date"]}')

    def update_task(self):
        if not self.task:
            print("task list is empty")
        else:
            task_name_to_update = input('Enter your task name to update: ')
            if task_name_to_update in self.task:
                update_status = "complete"
                self.task[task_name_to_update] = update_status
                print(f'{task_name_to_update} is marked completely')
                self.history[task_name_to_update] = {'old_status': self.task[task_name_to_update],
                                                     'new_status': update_status}
            else:
                print(f'{task_name_to_update} is not in task list')

    def delete_task(self):
        if not self.task:
            print("task list is empty")
        else:
            task_name_to_delete = input("Enter the name of task to delete: ")
            if task_name_to_delete in self.task:
                task_details = self.task[task_name_to_delete]
                del self.task[task_name_to_delete]
                print(f"\n{task_name_to_delete} is deleted successfully\n")
                self.history[task_name_to_delete] = {'deleted_task': task_details}
            else:
                print(f"{task_name_to_delete} is not in list")


    def display_history(self):

        if not self.history:
            print('History is not Available')
        else:
            print("\n******* User Info ***********\n")
            print(f"User_name: {self.user['name']}, Phone_number: {self.user['phone_number']},"
                  f" Address: {self.user['address']}")
            print('******* Task History ********')
            for task, details in self.history.items():
                if 'old_status' in details:
                    print(f'Task_status: {details['new_status']}')
                elif 'deleted_task' in details:
                    print(f'Task: {task} is deleted')








