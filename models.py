from pydantic import BaseModel

class TicketAction(BaseModel):
    action: str
    reasoning: str