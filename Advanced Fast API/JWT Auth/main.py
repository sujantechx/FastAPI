from fastapi import FastAPI ,Depends , HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer,OAuth2PasswordBearer

from auth import create_access_token, verify_token
from models import UserInDB
from utils import get_user,verify_password

app = FastAPI()

oauth2_schema=OAuth2AuthorizationCodeBearer(tokenUrl='token')


@app.post('/token')
def login(form_data: OAuth2PasswordRequestForm= Depends()):
    user_dict= get_user(form_data.username)
    if not user_dict:
        raise HTTPException(400,detail= 'Invalid Usersname')
    if not verify_password(form_data.password,user_dict['hased_password']):
        raise HTTPException(400,detail='Invalid Passwored')
    
    acess_token=create_access_token(data={'sub':form_data.username})
    return {'access_token':acess_token,'token_type':'bearer'}


@app.get('/users')
def read_users(token:str=Depends(oauth2_schema)):
    username=verify_token(token)
    return {'username':username}