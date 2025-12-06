from sqlalchemy import Column, Integer, String
from database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    status = Column(String, default="Pending")

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', status='{self.status}')>"
