class Todo:
    def __init__(self, id, title, description, done):
        self.id: int = id
        self.title: str = title
        self.description: str = description
        self.done: bool = done
