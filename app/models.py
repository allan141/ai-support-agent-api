from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, nullable=False)
    message = Column(Text, nullable=False)
    category = Column(String(100))
    urgency = Column(String(50))
