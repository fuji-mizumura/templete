import os
import json
from flask import Flask, render_template
from flask_cors import CORS
import psycopg2
import psycopg2.extras



app = Flask(__name__)
CORS(app)




# 接続テスト用のAPI
@app.route('/')
def index_api():
    return json.dumps({
        'message':'Hello World',
    })




# DBに接続して従業員リストをテンプレートを用いて表示
@app.route('/db')
def db_view():
    try:
        # PostgreSQL Serverとの接続を定義し、接続を作成
        conn = psycopg2.connect(
            host='db',
            port=5432,
            database=os.environ['POSTGRES_DB'],
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD'],
        )
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # SQLを投入して情報取得
        cur.execute('select * from employee order by employee_id')
        employee_list = cur.fetchall()

        # データをhtmlに渡して表示
        return render_template(
            'app_template.html',
            title='Flask PostgreSQL',
            dataset=employee_list
        )
    except psycopg2.errors:
        return json.dumps({
            'message':'error',
        })
        pass

    # 接続終了
    conn.close()




# DBに接続してパスに指定した従業員IDの情報を取得するAPI
@app.route('/db/<int:employee_id>')
def db_get_api(employee_id):
    try:
        # PostgreSQL Serverとの接続を定義し、接続を作成
        conn = psycopg2.connect(
            host='db',
            port=5432,
            database=os.environ['POSTGRES_DB'],
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD'],
        )
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # SQLを投入して情報取得
        cur.execute('select * from employee where employee_id = %s', (employee_id,))
        employee_list = cur.fetchall()

        return json.dumps({
            'data':employee_list[0],
        })

    except psycopg2.errors:
        return json.dumps({
            'message':'error',
        })
        pass

    # 接続終了
    conn.close()





# DBに接続して従業員リストを作成するAPI
@app.route('/db/reset')
def db_reset_api():
    try:
        # PostgreSQL Serverとの接続を定義し、接続を作成
        conn = psycopg2.connect(
            host='db',
            port=5432,
            database=os.environ['POSTGRES_DB'],
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD'],
        )
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        # テーブルが存在するか確認し、存在しない場合は作成
        cur.execute("SELECT EXISTS(SELECT relname FROM pg_class WHERE relname='employee')")
        table_exists = cur.fetchone()[0]
        if not(table_exists):
            cur.execute('create table employee (employee_id int, employee_name varchar(255), employee_age int)')
            conn.commit()
            employee_list = []

        # テーブルにデータが存在する場合は削除
        cur.execute('select * from employee')
        employee_list = cur.fetchall()
        if len(employee_list) > 0:
            cur.execute('delete from employee')
            conn.commit()

        # 10件分のダミーデータを作成
        cur.execute("insert into employee values (1, 'Taro Yamada', 20)")
        cur.execute("insert into employee values (2, 'Hanako Yamada', 22)")
        cur.execute("insert into employee values (3, 'Jiro Yamada', 25)")
        cur.execute("insert into employee values (4, 'Sachiko Yamada', 27)")
        cur.execute("insert into employee values (5, 'Saburo Yamada', 30)")
        cur.execute("insert into employee values (6, 'Shizuka Yamada', 33)")
        cur.execute("insert into employee values (7, 'Goro Yamada', 35)")
        cur.execute("insert into employee values (8, 'Miki Yamada', 37)")
        cur.execute("insert into employee values (9, 'Ichiro Yamada', 40)")
        cur.execute("insert into employee values (10, 'Junko Yamada', 42)")

        # コミット
        conn.commit()

        return json.dumps({
            'message':'ダミーデータを作成しました',
        })

    except psycopg2.errors:
        return json.dumps({
            'message':'error',
        })
        pass

    # 接続終了
    conn.close()




app.run()