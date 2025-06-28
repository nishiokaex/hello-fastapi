from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Hello FastAPI", version="1.0.0")

@app.get("/")
async def root():
    """
    ルートエンドポイント
    """
    return {"message": "Hello World"}

@app.get("/health")
async def health_check():
    """
    ヘルスチェックエンドポイント
    """
    return {"status": "healthy"}

@app.get("/api/hello")
async def hello():
    """
    基本的なAPIエンドポイント
    """
    return {"message": "Hello from FastAPI!"}

@app.get("/api/hello/{name}")
async def hello_name(name: str):
    """
    パラメータ付きエンドポイント
    """
    return {"message": f"Hello {name}!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)