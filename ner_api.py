from flask import Flask,jsonify,request,render_template
import string
from custom_logger.logger import logger
from flask_cors import CORS
from processor.recognizer import entity_recogntion
from utility.utils import prepare_html
app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
@app.route("/string_matching", methods=['GET','POST'])
def string_matching():
    if request.method == 'POST':
        string_1=request.form["string_1"]
        htm,file=entity_recogntion(string_1)
        prepare_html(htm)
        return render_template('ner.html',encoding='utf-8')
    else:
        return render_template('new_ner.html')


if __name__ == '__main__':
    app.run(debug=True)