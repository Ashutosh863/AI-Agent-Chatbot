from db import SessionLocal
from models import ChatMessage

def save_messages(session_id,role,content):
    db = SessionLocal()
    msg = ChatMessage(session_id = session_id,role = role,content = content)
    db.add(msg)
    db.commit()
    db.close()

def load_messages(session_id):
    db = SessionLocal()
    msgs = db.query(ChatMessage).filter(
        ChatMessage.session_id == session_id
    ).all()

    db.close()

    return [
        {"role": m.role, "content": m.content}
        for m in msgs
    ]
