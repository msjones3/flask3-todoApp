from flask import *
app = Flask(__name__)


todos = ['make bed','do homework','brush teeth']

app.run(debug=True)