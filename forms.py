from flask_wtf import FlaskForm
# 导入表单的字段
from wtforms import StringField, PasswordField, SubmitField
# 导入验证器
from wtforms.validators import Length, DataRequired

# 自定义表单类
class QueryForm(FlaskForm):
    word=StringField("请输入要查询的单词：",validators=[DataRequired()])
    
    submit=SubmitField("提交",render_kw={
            "class": "control",
        })
class LoginForm(FlaskForm):
    username = StringField(
        # 标签
        label="用户名",
        # 验证器
        validators=[
            DataRequired('请输入用户名')
        ],
        description="账号",
        # 附加选项,会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入用户名!",
            "required": 'required'  # 表示输入框不能为空，并有提示信息
        }
    )

    password = PasswordField(
        # 标签
        label="密码",
        # 验证器
        validators=[
            DataRequired('请输入密码!')
        ],
        description="密码",

        # 附加选项(主要是前端样式),会自动在前端判别
        render_kw={
            "class": "form-control",
            "placeholder": "请输入密码!",
            "required": 'required'    # 表示输入框不能为空
        }
    )

    submit = SubmitField(
        label="登录",
        render_kw={
            "class": "form-control",
        }
    )
