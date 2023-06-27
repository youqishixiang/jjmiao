from flask import Flask, render_template
import viewdata.tools as tool
from flask import jsonify, json
from flask_cors import CORS

app = Flask(__name__, static_folder='', static_url_path='')
CORS(app, resources='/*')
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRNT_REGULAR'] = False
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def index():
    return render_template("index2.html")

@app.route("/bigdata/sales_rank")
def task4():
    data = tool.bigdata_sales_rank()
    return jsonify(data)


@app.route("/index2/toplist")
def task18():
    data = tool.index2_toplist()
    return jsonify(data)

@app.route("/index2/chart")
def task19():
    data = tool.index2_chart_data()
    return jsonify(data)

@app.route("/index2/top_title")
def task20():
    data = tool.index2_toptitle()
    return jsonify(data)


if __name__ == '__main__':
    app.debug = True
    app.run()