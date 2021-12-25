# import modules
from area import area_to_acre
from fastapi import FastAPI, Request
import uvicorn
from enum import Enum

# instantiate FastAPI object
app = FastAPI()

# endpoint


@app.post("/")
async def get_area(request: Request):
    '''
    A FastAPI app to take input and invoke area module to process input parameters to return the area in acres.
    '''
    packet = await request.json()
    length = packet['length']
    width = packet['width']

    # instantiate area object to evaluate input
    area = area_to_acre(length, width)
    return {"area_in_acre": area, "input": packet}

# main driver function
if __name__ == '__main__':
    uvicorn.run("app:app", reload=True)
