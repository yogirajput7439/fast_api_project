from pydantic import BaseModel, ConfigDict

class StudentCreate(BaseModel):
    name : str
    email : str
    age : int
    city : str

class StudentResponse(BaseModel):
    id : int
    name : str
    email : str
    age : int
    city : str


    model_config = ConfigDict(from_attributes = True)
    