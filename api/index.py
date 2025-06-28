from fastapi import FastAPI
from main import app

# Vercelでは関数として公開する必要がある
def handler(request):
    return app