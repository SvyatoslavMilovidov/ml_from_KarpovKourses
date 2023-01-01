from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_hello_world(a: int, b: int):
    return a + b
