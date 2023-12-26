import sqlite3

class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_tasks_table()
        
    def create_tasks_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        priority INTEGER NOT NULL
                        );''')
        
    def add_task(self):
        name = input("What is the task?")
        priority = int(input("What is the priority?"))
        
        if len(name) == 0 or priority < 1:
            return
        
        if self.find_task(name) is not None:
            return
        
        self.c.execute('''INSERT INTO tasks (name, priority) VALUES (?, ?)''', (name, priority))
        self.conn.commit()
        
    def find_task(self, task):
        for row in self.c.execute('''SELECT * FROM tasks'''):
            if row[1] == task:
                return row
        return None
    
    def show_tasks(self):
        for row in self.c.execute('''SELECT * FROM tasks'''):
            print(row)
    
    def change_priority(self):
        id = int(input("What is the task id that you wish to update? "))
        new_priority = input("What should the priority be set to? ")

        if id < 1:
            return
        
        self.c.execute('''UPDATE tasks
                       SET priority = ?
                       WHERE id = ?''', (new_priority, id))
        self.conn.commit()
    
    def delete_task(self):
        id = int(input("What is the task id you wish to delete? "))

        self.c.execute('''DELETE FROM tasks
                       WHERE id = ?
                       ''', (id, ))
        self.conn.commit()

    def show_menu(self):
        self.active = True
        while self.active:
            print('''1. Show Tasks\n2. Add Task\n3. Change Priority\n4. Delete Task\n5. Exit''')
            choice = int(input('Please choose an option: '))

            if choice == 1:
                self.show_tasks()
            elif choice == 2:
                self.add_task()
            elif choice == 3:
                self.change_priority()
            elif choice == 4:
                self.delete_task()
            elif choice == 5:
                self.active = False
            else:
                choice = int(input("Please choose a valid option: "))

app = Todo()
app.create_tasks_table()
app.show_menu()