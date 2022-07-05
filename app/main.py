from fastapi import Body, FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from app.models import Post, User
from random import randrange


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


my_post = [{
    "id": 1,
    "title": "Post 1",
    "content": "Here is the first post test"
},
{
    "id": 2,
    "title": "Post 2",
    "content": "Here is the second post test"
}]

@app.get("/")
def root():
    return {"Hello": "This is the root massage"}


@app.get("/posts")
def get_posts():
    cursor.execute("""SELECT * FROM posts """)
    posts = cursor.fetchall()
    print(posts)
    print(my_post)
    return {"Data": my_post}


@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_post.append(post_dict)
    return {"Message": "Successfully created raw post!", "Body": post}

'''
@app.get("/users")
def getUsers():
    return User
'''
@app.post("/users")
def users(user: User):
    return {"User details": user}