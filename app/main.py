from fastapi import Body, FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from app.models import Post, User


# FastAPI instance
app = FastAPI()



# Database Connection settings
while True:

    try:
        conn = psycopg2.connect(host='localhost', database='sculapi', user='postgres', password='Anthonimoray#', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Database connected successfully!!!')
        break
    except Exception as error:
        print('Database connection failed!!!')
        print("Error ", error)
        time.sleep(2)
 # ..............................................


@app.get("/")
def root():
    return {"Hello": "This is the root massage"}


@app.get("/posts")
def get_posts():
    return {"Data": "This is a post content"}


@app.post("/posts")
def create_posts(new_post: Post):
    print(new_post)
    return {"Message": "Successfully created raw post!", "Body": new_post}
'''
@app.get("/users")
def getUsers():
    return User
'''
@app.post("/users")
def users(user: User):
    return {"User details": user}