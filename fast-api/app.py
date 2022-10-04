from fastapi import FastAPI
from calc import calculate
from pydantic import BaseModel



class user_input(BaseModel):
    operator: str
    x: int
    y: int

app = FastAPI()


@app.post("/calculate")
def calculate_post(user_input: user_input):
    return calculate(user_input.operator, user_input.x, user_input.y)


# @app.get("/calculate")
# def calculate_get(operator: str, x: int, y: int):
#     return calculate(operator, x, y)

