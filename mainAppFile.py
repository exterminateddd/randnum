from flask import render_template, redirect, request, Flask, make_response
import random
import werkzeug.exceptions

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        minNum = str(request.form["min"])
        maxNum = str(request.form["max"])
        if not minNum.isdigit() or not maxNum.isdigit():
            return render_template("index.html")
        if not minNum or not maxNum:
            return render_template("index.html")
        if int(minNum) > int(maxNum):
            return render_template("index.html")
        result = random.randint(int(minNum), int(maxNum))
        if len(str(result)) > 10:
            result = str(result)[:7]+'...'
        return render_template("index.html", result=result)
    return render_template("index.html")


@app.errorhandler(werkzeug.exceptions.NotFound)
def not_found(e):
    return redirect('/')


if __name__ == '__main__':
    app.run()
