from flask import Flask,render_template,url_for,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Text,DateTime,UniqueConstraint,Index
from sqlalchemy.orm import sessionmaker
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
import pymysql
import datetime
from sqlalchemy.sql.expression import func, select
from youdao import get_data
import requests


app=Flask(__name__)

# 数据库配置
engine = create_engine("mysql+pymysql://test:123456@47.105.166.136/dictionary?charset=utf8mb4",
    max_overflow=0, #超过连接池大小外最多创建的连接
    pool_size=50, # 连接池大小
    pool_timeout=30, # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1 # 多久之后对线程池中的线程进行一次连接的回收（重置）
)
Session = sessionmaker(bind=engine)

app.secret_key="tianjin"
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

# Base.metadata.create_all(engine)
# 自定义表单类
class QueryForm(FlaskForm):
    word=StringField("请输入要查询的单词：",validators=[DataRequired()])
    
    submit=SubmitField("提交")

@app.route("/delete_word/<delete_word>")
def delete_word(delete_word):
    
    # 查询
    session = Session()
    word=session.query(Dictionary).filter_by(word = delete_word).first()
    # 有就删除
    if word:
        try:
            
            session.delete(word)
            session.commit()
            flash("已删除")
        except Exception as e:
            print(e)
            flash("删除单词出错")
            session.rollback()
            return render_template("500.html")
    else:
        flash("单词找不到")
    return redirect(url_for("index"))
@app.route("/",methods=["POST","GET"])
def index():
    query_form=QueryForm()
    # 调用WTF的函数实现验证
    if query_form.validate_on_submit():
        # 验证通过 获取数据
        input_word=query_form.word.data
        # 判断单词是否存在 查询数据库
        # 每次执行数据库操作时，都需要创建一个session
        session = Session()
        word = session.query(Dictionary).filter_by(word=input_word).first()
        if word:
            # try:
                
            words=session.query(Dictionary).filter_by(word=input_word)
            # print(words)
            # session.close()
            return render_template("index.html",form=query_form,words=words)
            
        else:
            
            try:
                paraph = get_data(input_word)
                new_word=Dictionary(word=paraph[0],IPA=paraph[1],paraphrase=paraph[2],example_sentence=paraph[3]+paraph[4],other=paraph[5])
                session.add(new_word)
                session.commit()
                flash("添加成功")
                words=session.query(Dictionary).filter_by(word=input_word)
            
                # session.close()
                return render_template("index.html",form=query_form,words=words)
            except Exception as e:
                print(e)
                flash("添加失败")
                session.rollback()
                words=session.query(Dictionary).order_by(func.rand()).limit(5)
                # session.close()
                return render_template("index.html",form=query_form,words=words)
    session=Session()
    words=session.query(Dictionary).order_by(func.rand()).limit(5)
    return render_template("index.html",form=query_form,words=words)    
if __name__=="__main__":
    
    app.run(debug=True)