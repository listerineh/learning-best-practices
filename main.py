import uvicorn
from api.app.controllers.todo_controller import app

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
