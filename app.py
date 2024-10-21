from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = [
    {"id": 1, "title": "買い物", "description": "スーパーで野菜を買う"},
    {"id": 2, "title": "レポート提出", "description": "10月18日までに提出"}
]

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        new_todo = {
            "id": len(todos) + 1,
            "title": request.form['title'],
            "description": request.form['description'],
            "due_date":request.form['due_date']
        }
        todos.append(new_todo)
        return redirect(url_for('index'))
    return render_template('add_task.html')

@app.route('/todo/<int:todo_id>')
def detail(todo_id):
    todo = next((todo for todo in todos if todo["id"] == todo_id), None)
    return render_template('detail.html', todo=todo)

@app.route('/tags')
def tags():
    return render_template('tag.html')

if __name__ == '__main__':
    app.run(debug=True)
