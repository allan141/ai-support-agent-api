from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.schemas import MessageRequest, TicketCreate, TicketResponse
from app.ai_agent import analyze_message
from app.database import Base, engine, SessionLocal
from app.models import Ticket
from app.mongo import save_message_log


Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Support Agent API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "AI Support Agent API funcionando"}

@app.post("/agent/analyze")
def analyze(request: MessageRequest):
    result = analyze_message(request.message)
    return result

@app.post("/tickets", response_model=TicketResponse)
def create_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):

    analysis = analyze_message(ticket.message)

    new_ticket = Ticket(
        customer_id=ticket.customer_id,
        message=ticket.message,
        category=analysis["category"],
        urgency=analysis["urgency"]
    )

    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)

    save_message_log({
        "ticket_id": new_ticket.id,
        "customer_id": ticket.customer_id,
        "message": ticket.message,
        "category": analysis["category"],
        "urgency": analysis["urgency"],
        "response": analysis["response"],
        "source": "POST /tickets"
    })

    return new_ticket

@app.get("/tickets", response_model=list[TicketResponse])
def list_tickets(db: Session = Depends(get_db)):
    tickets = db.query(Ticket).all()
    return tickets

@app.get("/metrics")
def get_metrics(db: Session = Depends(get_db)):
    total_tickets = db.query(Ticket).count()

    urgent_tickets = db.query(Ticket).filter(
        Ticket.urgency == "alta"
    ).count()

    categories = db.query(
        Ticket.category,
        func.count(Ticket.id)
    ).group_by(Ticket.category).all()

    categories_count = {
        category: count for category, count in categories
    }

    return {
        "total_tickets": total_tickets,
        "urgent_tickets": urgent_tickets,
        "categories": categories_count
    }