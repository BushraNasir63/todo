from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

tasks = []
next_id = 1

class NewTask(BaseModel):
    title: str


@app.post("/tasks")
def add_task(item: NewTask):
    global next_id
    task = {"id": next_id, "title": item.title, "done": False}
    tasks.append(task)
    next_id += 1
    return task

@app.get("/tasks")
def list_tasks():
    return tasks

@app.patch("/tasks/{task_id}/done")
def mark_done(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    raise HTTPException(status_code=404, detail="Task not found")



