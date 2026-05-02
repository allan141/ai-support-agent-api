from pydantic import BaseModel

class MessageRequest(BaseModel):

    customer_id: int
    message: str

class TicketCreate(BaseModel):
    customer_id: int
    message: str
    category: str | None = None
    urgency: str | None =None


class TicketResponse(BaseModel):
    id: int
    customer_id: int
    message: str
    category: str | None
    urgency: str | None


    class Config:
        form_attributes = True