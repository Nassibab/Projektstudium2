# Hello page: http://localhost:8085/hello - http://127.0.0.1:8000/hello
# Character count: http://localhost:8085/count_chars?text=FastAPI - http://127.0.0.1:8000/counter?text=example
# Swagger docs: http://localhost:8085/docs - http://127.0.0.1:8000/docs#/default/welcome_api_hello_get

from fastapi import FastAPI, Query

app= FastAPI()

@app.get("/hello")
def welcome_api():
    return {"message": "Hello World from Nassib"}



@app.get("/counter")
def counter_api(text: str = Query(..., description="enter text")):
    count = len(text)
    return {"text": text, "character_count": count}
