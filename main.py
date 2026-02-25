from fastapi import FastAPI , status , HTTPException , Query , Path , Form

app = FastAPI()

users = [
    {"id":0 , "username":"Abbas"},
    {"id":1 , "username":"teimor"},
    {"id":2 , "username":"Ali"},
    {"id":3 , "username":"xz"},
    {"id":4 , "username":"rostam"},
]


@app.get('/',status_code=status.HTTP_200_OK)
def rooot():
    return {"root"}

@app.get('/users/{username}',status_code=status.HTTP_200_OK)
def all_users(username:str , q:str = Query(default=None) ):
    for user in users:
        if user["username"] == username:
            return user
    raise HTTPException(status_code= status.HTTP_404_NOT_FOUND , detail="object not found")


@app.get('/signup')
def signup(username : str = Form()):
    return username
