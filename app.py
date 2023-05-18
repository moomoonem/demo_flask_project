from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)


@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == "GET":
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="123456",
            database="world"
        )

        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        sql = "select * from test;"
        cursor.execute(sql)
        datalist = cursor.fetchall()
        conn.commit()
        conn.close()
        print(datalist)
        return render_template('add_user.html', datalist=datalist)

    else:
        u_name = request.form.get("user")
        u_pwd = request.form.get("pwd")
        u_mobile = request.form.get("mobile")
        print(u_name, u_pwd, u_mobile)

        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="123456",
            database="world"
        )

        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        conn.select_db("world")
        sql = "insert into test(name,password,mobile) values (%s,%s,%s);"
        cursor.execute(sql, [u_name, u_pwd, u_mobile, ])
        conn.commit()
        conn.close()
        return "xxx"

# @app.route('/add_user')
# def show_users():
#     conn = Connection(
#         host="localhost",
#         port=3306,
#         user="root",
#         password="123456",
#         autocommit=False
#     )
#
#     cursor = conn.cursor()
#     conn.select_db("world")
#     sql = "select * from test;"
#     cursor.execute(sql)
#     datalist = cursor.fetchall()
#     conn.commit()
#     conn.close()
#     print(datalist)
#     return render_template('add_user.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        data = request.form
        print(data, type(data))
        print(dict(data))
        if dict(data)["user"] and dict(data)["psd"]:
            return "注册成功"
        else:
            return "注册失败"


if __name__ == '__main__':
    app.run()
