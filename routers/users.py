from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def profile_users():
    return{"profile_users"}



@router.post('/signin')
async def signin():
    return {"signin"}



@router.post('/login')
async def login():
    return{"login"}



@router.put('/')
async def update_profile():
    return{"update_profile"}



