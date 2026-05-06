from fastapi import FastAPI

app = FastAPI()


def add_func(a, b):
    return a + b

@app.get("/")
def home():
    return {"status": "Online", "message": "簡易版計算機API"}

@app.get("/add")
def calculate_add(a: float, b:float):
    result = add_func(a, b)
    return {"operation": "addition", "a":a, "b":b, "result": result}

