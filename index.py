from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World from Vercel!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from FastAPI API!"}

@app.get("/api/hello/{name}")
def hello_name(name: str):
    return {"message": f"Hello {name}!"}