from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html", num = 4, num2 = 4)

@app.route('/<int:num2>')
def build_checkerboard(num2):
    return render_template("index.html", num2 = num2 // 2, num = 4)

@app.route('/<int:num>/<int:num2>')
def build_custom_checkerboard(num, num2):
    return render_template("index.html", num2 = num2 // 2, num = num // 2)

@app.route('/<int:num>/<int:num2>/<str1>/<str2>')
def build_color_checkerboard(num, num2, str1, str2):
    return render_template("index.html", num2 = num2 // 2, num = num // 2, str1 = str1, str2 = str2)

if __name__=="__main__":
    app.run(debug=True)