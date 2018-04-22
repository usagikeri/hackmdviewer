from flask import Flask, render_template, request, send_file, redirect, url_for
import sqlalchemy as sa

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    url = 'mysql://hackmd:hackmdpass@database:3306/hackmd'
    engine = sa.create_engine(url, echo=True)
    rows = engine.execute('select title,shortid from Notes')

    return render_template('index.html',rows=rows)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
