import pytest
from api.app.models.todo import Todo


@pytest.fixture
def json_todo_mock() -> dict:
    return {
        "id": 1,
        "title": "foo",
        "description": "bar",
        "done": False
    }


@pytest.fixture
def todo_mock() -> Todo:
    return Todo(
        id=1,
        title="foo",
        description="bar",
        done=False
    )


@pytest.fixture
def todos_mock(todo_mock):
    return [todo_mock for _ in range(10)]
