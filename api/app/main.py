# Default fastapi
import json
from typing import List, Optional
from fastapi import FastAPI
from .schemas.lecturer import Lecturer, LecturerType
app = FastAPI()

import strawberry
from strawberry.fastapi import GraphQLRouter

from .backend.api.api import api_router
app.include_router(api_router, prefix="/api")

# Two main examples of the GET routes
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# Example how to read in the courses
with open('./data/courses.json', 'r') as f:
  courses = json.load(f)

# Example how to read in the lecturers
with open('./data/lecturers.json', 'r') as f:
  lecturers = json.load(f)
  lecturers = list(map(lambda lecturer: Lecturer(**lecturer), lecturers))


@app.get('/mct/courses')
def getAllCourses():
    # pass # Remove the pass part now
    return courses

@app.get('/mct/courses/name/{name}')
def getCourseByName(name: str): # Define that you want to get a parameter 'name' from the url, which will be a string-value

    # Use a Lambda method, which is just a shorthand Python function. This function takes one JSON input and checks it.
    # It returns 'true' if the statement is correct. This filter method only returns the elements for which the result of the statement is 'true'
    return list(filter(lambda course: course['title'] == name, courses)) # Use the Python filter function to filter on only one Course. This will still return a list of items. We will fix that later.

@app.get('/mct/courses/track/{track}')
def getAllCoursesByTrack(track: str): # Define that you want to get a parameter 'track' from the url, which will be a string-value
    return list(filter(lambda course: course['tracks'] == None or ( course['tracks'] != None and track in course['tracks'] ), courses)) # What if this track isn't in the list of Courses? Shouldn't we show something nicer? Let's do that later!


lecturers[0].sayHello()

@strawberry.type
class Query:
    @strawberry.field
    def lecturers(self) -> List[LecturerType]:
        return lecturers

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app.include_router(graphql_app, prefix="/graphql")
