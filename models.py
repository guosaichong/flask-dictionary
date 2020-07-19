from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, UniqueConstraint, Index
import datetime
# from config import engine
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
# from sqlalchemy.orm import sessionmaker
Base = declarative_base()
class Dictionary(Base):
    # 表名
    __tablename__="english"
    # 字段
    
    id=Column(Integer,primary_key=True,nullable=False)
    word=Column(String(30),nullable=False,unique=True,index=True)
    IPA= Column(String(60))
    paraphrase = Column(Text)
    example_sentence = Column(Text)
    other = Column(Text)
    create_time = Column(DateTime,default=datetime.datetime.now,nullable=False)

class User(Base,UserMixin):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)  # unique代表不能重复，唯一的
    pwd_hash = Column(String(128), nullable=False)
    create_time = Column(DateTime, index=True, default=datetime.datetime.now, nullable=False)

    def __repr__(self):  # 定义返回的类型
        return '<user %r>' % self.username

    def hash_password(self, password):
        self.pwd_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pwd_hash,password)
# user=User(username="guosaichong",pwd_hash=generate_password_hash("123456"))
# Session = sessionmaker(bind=engine)
# session=Session()
# session.add(user)
# session.commit()
# Base.metadata.create_all(engine)