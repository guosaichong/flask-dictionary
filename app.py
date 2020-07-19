from flask import Flask, render_template, url_for, redirect, flash, request
from sqlalchemy.sql.expression import func, select
from utils import youdao
import requests
from config import engine
from models import Dictionary, User
from forms import QueryForm, LoginForm
from flask_login import LoginManager,login_user,login_required
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
app.secret_key = "tianjin"
Session = sessionmaker(bind=engine)

login_manager = LoginManager(app)

login_manager.login_view = '/'
login_manager.login_message_category = 'info'
login_manager.login_message = 'Access denied.'


@login_manager.user_loader
def get_user(user_id):
    session=Session()
    return session.query(User).filter_by(id=user_id).first()
@app.route("/delete_word/<delete_word>")
@login_required
def delete_word(delete_word):

    # 查询
    session = Session()
    word = session.query(Dictionary).filter_by(word=delete_word).first()
    # 有就删除
    if word:
        try:

            session.delete(word)
            session.commit()
            session.close()
            flash("已删除")
        except Exception as e:
            print(e)
            flash("删除单词出错")
            session.rollback()
            session.close()
            return render_template("500.html")
    else:
        flash("单词找不到")
    return redirect(url_for("index"))


@app.route("/index", methods=["POST", "GET"])
@login_required
def index():
    query_form = QueryForm()
    # 调用WTF的函数实现验证
    if query_form.validate_on_submit():
        # 验证通过 获取数据

        input_word = query_form.word.data
        # 判断单词是否存在 查询数据库
        session = Session()
        word = session.query(Dictionary).filter_by(word=input_word).first()
        if word:
            # try:

            words = session.query(Dictionary).filter_by(word=input_word)
            # print(words)
            session.close()
            return render_template("index.html", form=query_form, words=words)

        else:

            try:
                paraph = youdao.get_data(input_word)
                new_word = Dictionary(
                    word=paraph[0], IPA=paraph[1], paraphrase=paraph[2], example_sentence=paraph[3]+paraph[4], other=paraph[5])
                session.add(new_word)
                session.commit()
                
                flash("添加成功")
                words = session.query(Dictionary).filter_by(word=input_word)

                session.close()
                return render_template("index.html", form=query_form, words=words)
            except Exception as e:
                print(e)
                flash("添加失败")
                session.rollback()
                words = session.query(Dictionary).order_by(
                    func.rand()).limit(5)
                session.close()
                return render_template("index.html", form=query_form, words=words)
    session = Session()
    words = session.query(Dictionary).order_by(func.rand()).limit(5)
    session.close()
    return render_template("index.html", form=query_form, words=words)


@app.route('/', methods=['GET', 'POST'])
def login():
    forms = LoginForm()       # 实例化forms
    if forms.validate_on_submit():  # 提交的时候进行验证,如果数据能被所有验证函数接受，则返回true，否则返回false
        data = forms.data  # 获取form数据信息（包含输入的用户名（account）和密码（pwd）等信息）,这里的account和pwd是在forms.py里定义的
        session = Session()
        user = session.query(User).filter_by(
            username=data["username"]).first()  # 查询表信息user表里的用户名信息
        print(user)  # 查询表信息user表里的用户名信息

        if user == None:
            flash("账号不存在")  # 操作提示信息，会在前端显示
            return redirect(url_for('login'))
        # 这里的check_pwd函数在models 下user模型下定义
        elif user != None and not user.verify_password(data["password"]):
            flash("密码错误")
            return redirect(url_for('login'))
        # 匹配成功，添加session
        # session['user'] = data['account']
        # 重定向到首页
        session.close()
        login_user(user)
        
        return redirect(request.args.get('next') or url_for('index'))
    return render_template('login.html', form=forms)


if __name__ == "__main__":

    app.run(debug=True)
