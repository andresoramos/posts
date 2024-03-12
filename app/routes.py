from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json


router = APIRouter()

class Id(BaseModel):
    id: str

@router.get('/posts/{page_number}')
def get_tasks(page_number: int):
    data_location = 'data/data.json'
    quantity = 5
    lower_range = (quantity * page_number) - quantity
    upper_range = quantity * page_number
    return_list = []
    stop_running = False
    

    with open(data_location, 'r') as file:
        data = json.load(file)
    
    for i in range(lower_range, upper_range):
        if i < len(data):
            return_list.append(data[i])
        else: 
            return_list = []
            stop_running = True
            break
    
    return {'list': return_list, 'stop_running': stop_running}

@router.post('/posts')
def get_post_by_id(id: Id):
    data_location = 'data/data.json'
    
    with open(data_location, 'r') as file:
        data = json.load(file)
    for post in data:
        if post["post_url"] == id.id:
            post["num_hugs"] = post.get("num_hugs", 0) + 1
            
            with open(data_location, 'w') as file:
                json.dump(data, file, indent=4)
            
            return post
    
    raise HTTPException(status_code=404, detail="Post not found")
