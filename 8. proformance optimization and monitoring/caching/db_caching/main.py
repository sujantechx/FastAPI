import sqlite3
import redis
import json
import hashlib
from fastapi import FastAPI
from pydantic import BaseModel


app =FastAPI()
redis_clinte= redis.Redis(host='localhost',port= 6379,db=0)

# estabklish database conections
def get_db_conection():
    conn=sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn
#set up database

def init_db():
    conn =get_db_conection()
    cursor=conn.cursor()
    cursor.execute("""
         CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTGER 
                )
         """)
    
    cursor.execute("INSERT OR IGNORE INTO users (id,name,age) VALUES (1,'sujd',74)")
    cursor.execute("INSERT OR IGNORE INTO users (id,name,age) VALUES (2,'dsfg',46)") 
    cursor.execute("INSERT OR IGNORE INTO users (id,name,age) VALUES (3,'sudsjd',64)")
    conn.commit()
    conn.close()
    
init_db()

class UserQuery(BaseModel):
    user_id:int
    

def make_cache_key(user_id:int):
    raw =f"user:{user_id}"
    return hashlib.sha256(raw.encode()).hexdigest()


@app.post('/get_user')
def get_user(query:UserQuery):
    cache_key = make_cache_key(query.user_id)
    
    cache_data = redis_clinte.get(cache_key)
    if cache_data:
        print('Serving from Redis Cache!')
        return json.loads(cache_data)
    
    
    conn = get_db_conection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE id = ?', (query.user_id,))
    row = cursor.fetchone()
    conn.close()
    
    
    if row is None:
        return {'message':'User not found'}
    
    
    result= {'id':row['id'], 'name':row['name'],'age':row['age']}
    redis_clinte.setex(cache_key, 3600, json.dumps(result))
    print("Fetched from DB and Cached!")
    
    return result