#TO-DO LIST
import os

class ToDoList:
    def __init__(self):
        self.works = []

    def add_work(self, work):
        self.works.append({'work': work, 'completed': False})

    def update_work(self, work_id, new_work):
        if 0 <= work_id < len(self.works):
            self.works[work_id]['work'] = new_work
        else:
            print("Invalid work ID.")

    def complete_work(self, work_id):
        if 0 <= work_id < len(self.works):
            self.works[work_id]['completed'] = True
        else:
            print("Invalid work ID.")

    def delete_work(self, work_id):
        if 0 <= work_id < len(self.works):
            del self.works[work_id]
        else:
            print("Invalid work ID.")

    def display_works(self):
        if not self.works:
            print("No works in the to-do list.")
        else:
            for idx, work in enumerate(self.works):
                status = "Completed" if work['completed'] else "Pending"
                print(f"{idx}. {work['work']} - {status}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    todo_list = ToDoList()

    while True:
        clear_screen()
        print("To-Do List Application")
        print("======================")
        todo_list.display_works()
        print("======================")
        print("Options:")
        print("1. Add a work")
        print("2. Update a work")
        print("3. Mark a work as complete")
        print("4. Delete a work")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            work = input("Enter the work: ")
            todo_list.add_work(work)
        elif choice == '2':
            work_id = int(input("Enter the work ID to update: "))
            new_work = input("Enter the new work: ")
            todo_list.update_work(work_id, new_work)
        elif choice == '3':
            work_id = int(input("Enter the work ID to mark as complete: "))
            todo_list.complete_work(work_id)
        elif choice == '4':
            work_id = int(input("Enter the work ID to delete: "))
            todo_list.delete_work(work_id)
        elif choice == '5':
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
