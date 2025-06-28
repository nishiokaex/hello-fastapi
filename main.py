"""
TODO API - FastAPIを使用したシンプルなTODO管理システム
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import uuid

app = FastAPI(
    title="TODO API",
    description="シンプルなTODO管理システム",
    version="1.0.0"
)

# データモデル
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class Todo(TodoBase):
    id: str
    created_at: datetime
    updated_at: datetime

# インメモリデータベース（開発用）
todos_db: List[Todo] = []

@app.get("/")
async def root():
    """ルートエンドポイント"""
    return {"message": "TODO API へようこそ！"}

@app.get("/todos", response_model=List[Todo])
async def get_todos():
    """全てのTODOを取得"""
    return todos_db

@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: str):
    """特定のTODOを取得"""
    todo = next((todo for todo in todos_db if todo.id == todo_id), None)
    if not todo:
        raise HTTPException(status_code=404, detail="TODOが見つかりません")
    return todo

@app.post("/todos", response_model=Todo)
async def create_todo(todo: TodoCreate):
    """新しいTODOを作成"""
    new_todo = Todo(
        id=str(uuid.uuid4()),
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    todos_db.append(new_todo)
    return new_todo

@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: str, todo_update: TodoUpdate):
    """TODOを更新"""
    todo = next((todo for todo in todos_db if todo.id == todo_id), None)
    if not todo:
        raise HTTPException(status_code=404, detail="TODOが見つかりません")
    
    if todo_update.title is not None:
        todo.title = todo_update.title
    if todo_update.description is not None:
        todo.description = todo_update.description
    if todo_update.completed is not None:
        todo.completed = todo_update.completed
    
    todo.updated_at = datetime.now()
    return todo

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str):
    """TODOを削除"""
    todo_index = next((i for i, todo in enumerate(todos_db) if todo.id == todo_id), None)
    if todo_index is None:
        raise HTTPException(status_code=404, detail="TODOが見つかりません")
    
    deleted_todo = todos_db.pop(todo_index)
    return {"message": f"TODO '{deleted_todo.title}' が削除されました"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)