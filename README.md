# To-Do API

A simple to-do list API. You can add a task, see all tasks, and mark a task as done. 
Data is stored in memory (a Python list), so it resets when the server restarts. 
No database used since the task didn't need one.

## How to run it

### Using Docker
docker build -t todo-api .
docker run -p 8000:8000 todo-api

Then open http://localhost:8000/docs in your browser.

### Without Docker
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload

Then open http://localhost:8000/docs

## Endpoints

- POST /tasks - adds a new task. Needs a "title" in the request body.
- GET /tasks - returns the list of all tasks.
- PATCH /tasks/{task_id}/done - marks the task with that id as done.
## Reflection

The trickiest part for me was setting up the environment - remembering to 
activate the virtual environment every time I opened a new terminal, and 
making sure main.py was in the right folder instead of inside .venv by mistake. 
Most of my errors came from small setup mistakes like this, not the actual code.

I used FastAPI because it checks the input automatically and also gives a 
docs page where I could test the endpoints easily, without writing extra code 
for testing. I kept the data in memory since the task allowed it, and it was 
simpler while I was still learning how everything connects.

If I had another day, I would add a way to delete tasks, use a real database 
like SQLite so the data doesn't disappear on restart, and add better error 
messages. I would also try writing some automated tests instead of testing 
everything manually.