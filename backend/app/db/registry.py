# imports all models for alembic
from db.base import Base
from features.conversations.models import Conversation, Message
from features.students.models import Student
from features.teachers.models import Teacher
from features.users.models import User
