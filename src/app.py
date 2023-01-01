import datetime

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    name: str
    surname: str
    age: int
    registration_date: datetime.date

    class Config:
        orm_mode = True


@app.get('/')
def get_hello_world(a: int, b: int):
    return a + b


@app.get('/sum_date')
def get_sum_date(current_date: datetime.date, offset: int):
    diff_days = datetime.timedelta(days=offset)
    return current_date + diff_days


@app.post('/user/validate')
def post_user_validate(user_info: User):
    return f'Will add user: {user_info.name} {user_info.surname} with age {user_info.age}'