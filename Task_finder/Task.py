class Task:
    def __init__(self, task_name, task_status, task_date):
        self.task_name = task_name
        self.task_status = 'incomplete'
        self.task_date = task_date
        self.task = {}

    def task_info(self):
        print(f'task_name: {self.task_name}, task_status: {self.task_status}, task_date: {self.task_date}')

    def add_task(self):
        if self.task_name in self.task:
            print(f'{self.task_name} is already added')
        else:
            self.task[self.task_name] = {'Name': self.task_name, 'Status': self.task_status, 'Date':
                                         self.task_date}
            print(f'{self.task_name} is added successfully')



