import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def get_hello_world(a: int, b: int):
    return a + b


@app.get('/sum_date')
def get_sum_date(current_date: datetime.date, offset: int):
    diff_days = datetime.timedelta(days=offset)
    return current_date + diff_days
