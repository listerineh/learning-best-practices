from api.app.models.todo import Todo


def json_to_todo(json_todo: dict) -> Todo:
    return Todo(
        id=json_todo.get('id'),
        title=json_todo.get('title'),
        description=json_todo.get('description'),
        done=json_todo.get('done')
    )


def todo_to_json(todo: Todo) -> dict:
    return dict(
        id=todo.id,
        title=todo.title,
        description=todo.description,
        done=todo.done
    )
