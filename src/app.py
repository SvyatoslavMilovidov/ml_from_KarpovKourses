import datetime

import psycopg2
from loguru import logger
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


@app.get('/user/{user_id}')
def get_user_info(user_id: int):
    conn = psycopg2.connect(
        database="startml",
        user="robot-startml-ro",
        password="pheiph0hahj1Vaif",
        host="postgres.lab.karpov.courses",
        port=6432
    )
    cursor = conn.cursor()
    sql_text = f'''
    SELECT gender, age, city 
        FROM "user"
    WHERE id={user_id}
    '''
    cursor.execute(sql_text)
    result = cursor.fetchone()
    logger.info(f'Get info: {result}')
    return {'gender': result[0], 'age': result[1], 'city': result[2]}


@app.post('/user/validate')
def post_user_validate(user_info: User):
    return f'Will add user: {user_info.name} {user_info.surname} with age {user_info.age}'
