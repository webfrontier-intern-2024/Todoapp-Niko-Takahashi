from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# 静的ファイルの提供
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

# 仮のタスクデータ
class Todo:
    def __init__(self, title, tags):
        self.title = title
        self.tags = [Tag(name) for name in tags]

class Tag:
    def __init__(self, name):
        self.name = name

todos = [
    Todo("買い物をする", ["家事"]),
    Todo("レポートを書く", ["勉強", "重要"]),
]

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos})

@app.post("/add/")
def add_todo(title: str = Form(...), tags: str = Form(...)):
    new_todo = Todo(title, tags.split(","))
    todos.append(new_todo)
    return {"message": "タスクが追加されました"}
