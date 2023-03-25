"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""


import os

from sqlalchemy import Column, String, Text, Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, declared_attr, sessionmaker

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine


# Main URL for connection to DB
PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI")

# Secondary URL for connection
# PG_CONN_URI = "postgresql+asyncpg://postgres:password@localhost/postgres"

# URL for testing locally
# PG_CONN_URI = "postgresql+asyncpg://superuser:secretpassword@localhost:5432/postgres"

DB_ECHO = False


engine = create_async_engine(PG_CONN_URI, echo = DB_ECHO)


# Base model
class Base:
    @declared_attr
    def __tablename__(cls):
        """
        User ->blog_users
        Post -> blog_posts
        """
        return f"blog_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=Base)


Session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


# user table model
class User(Base):
    username = Column(
        String(32),
        unique=True,
        nullable=False,
    )
    name = Column(
        String(32),
        unique=False,
        nullable=False,
    )
    email = Column(
        String(32),
        unique=True,
        nullable=False,
    )

    posts = relationship("Post", back_populates="user")


# posts table model
class Post(Base):
    user_id = Column(
        Integer,
        ForeignKey("blog_users.id"),
        nullable=False,
        unique=False,
    )
    title = Column(
        String(100),
        nullable=False,
        default="",
        server_default="",
    )
    body = Column(
        Text,
        nullable=False,
        default="",
        server_default="",
    )

    user = relationship("User", back_populates="posts")
