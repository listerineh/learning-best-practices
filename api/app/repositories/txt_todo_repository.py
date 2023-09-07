from api.app.models.todo import Todo
from api.app.repositories.todo_repository import TodoRepository


file_path = "api/app/database/todos.txt"


class TxtTodoRepository(TodoRepository):

    def create(todo: Todo) -> bool:
        try:
            file = open(file_path, "a")
            file.write(f"{todo.id},{todo.title},{todo.description},{todo.done}\n")
            file.close()
            return True
        except Exception:
            return False


    #TODO: fix TODOs fields


    def get(id: int):
        file = open("todos.txt", "r")
        for line in file:
            todo = line.split(",")
            if int(todo[0]) == id:
                return Todo(
                    id=int(todo[0]), description=todo[1], done=bool(todo[2])
                )
        file.close()


    def update(todo: Todo):
        file = open(file_path, "r")
        lines = file.readlines()
        file.close()
        file = open(file_path, "w")
        for line in lines:
            todo = line.split(",")
            if int(todo[0]) == todo.id:
                file.write(f"{todo.id},{todo.description},{todo.done}\n")
            else:
                file.write(line)
        file.close()


    def delete(id: int):
        file = open(file_path, "r")
        lines = file.readlines()
        file.close()
        file = open(file_path, "w")
        for line in lines:
            todo = line.split(",")
            if int(todo[0]) != id:
                file.write(line)
        file.close()
