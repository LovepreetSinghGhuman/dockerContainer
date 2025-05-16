# lecturer.py
from pydantic import BaseModel
import strawberry

# Make the Lecturer Class inherit from the base-class `object`
class Lecturer(BaseModel):
    name: str
    language: str
    track: str
    programmingLanguage: str
    favouriteCourse: str
        
    def sayHello(self):
        print(f"Hello, my name is {self.name} and I love {self.favouriteCourse}")

@strawberry.experimental.pydantic.type(model=Lecturer, all_fields=True)
class LecturerType:
    pass