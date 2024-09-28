from __init__ import app
from flask import render_template
import untils


@app.route("/")
def home():
    cates = untils.load_categorys()
    return render_template("controller.html", categorys=cates)

if __name__ == "__main__":
    app.run(debug=True)