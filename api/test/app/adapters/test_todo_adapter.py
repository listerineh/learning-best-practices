from api.app.adapters.todo_adapter import json_to_todo, todo_to_json


def test__todo_change_to_json__success(json_todo_mock, todo_mock):
    current_todo = json_to_todo(json_todo_mock)

    assert type(current_todo) == type(todo_mock)
    assert current_todo.id == todo_mock.id
    assert current_todo.title == todo_mock.title
    assert current_todo.description == todo_mock.description
    assert current_todo.done == todo_mock.done


def test__json_change_to_todo__success(json_todo_mock, todo_mock):
    current_json = todo_to_json(todo_mock)

    assert type(current_json) == type(json_todo_mock)
    assert current_json.get('id') == json_todo_mock.get('id')
    assert current_json.get('title') == json_todo_mock.get('title')
    assert current_json.get('description') == json_todo_mock.get('description')
    assert current_json.get('done') == json_todo_mock.get('done')
