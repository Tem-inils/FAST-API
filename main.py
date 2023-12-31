from fastapi import FastAPI, Body
from api.test_process_api.process_api import test_process_router
from api.user_api.api_user import user_router
# создать db
from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(test_process_router)


@app.get('/hello')
async def hello():
    return {'message': 'hello world'}


# Параметры для запроса
@app.get('/param-example')
async def param_example(user_id: int, user_answer: str):
    return {'message': f'У{user_id} 10 ответов {user_answer}'}

# Post

@app.post('/hello')
async def first_post(name: str, phone_number: int):
    return {name: phone_number}


@app.put('/test-body')
async def test_body(header: str = Body(...), main_text: str = Body(default='Пример текста')):
    return {header, main_text}


#Запуск проекта на fastapi
# uvicorn main:app --reload