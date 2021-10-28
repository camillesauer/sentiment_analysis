from pydantic import BaseModel

# Defining a custom object using Pydantic
class Item(BaseModel):
    item_id: str
    description: str
