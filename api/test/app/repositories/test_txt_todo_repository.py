from api.app.repositories.txt_todo_repository import TxtTodoRepository
from unittest.mock import patch


def test__txt_todo_repository__single_create__success(todo_mock):
    with patch('api.app.repositories.txt_todo_repository.TxtTodoRepository.create', return_value=True) as mock_create:        
        result = TxtTodoRepository.create(todo_mock)
        mock_create.assert_called_once_with(todo_mock)
        assert result == True


def test__txt_todo_repository__multiple_create__success(todos_mock):
    with patch('api.app.repositories.txt_todo_repository.TxtTodoRepository.create', return_value=True) as mock_create:
        for todo in todos_mock:
            result = TxtTodoRepository.create(todo)
            mock_create.assert_called_with(todo)
            assert result == True


def test__txt_todo_repository__single_create__raises_exception(todo_mock):
    with patch('api.app.repositories.txt_todo_repository.open', side_effect=Exception):
        result = TxtTodoRepository.create(todo_mock)
        assert result == False
