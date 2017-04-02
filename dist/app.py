from flask import Flask, render_template
app = Flask(__name__)
app.config.update(
    DEBUG=True,
    TEMPLATES_AUTO_RELOAD=True
)

item = "AI1133"

app.jinja_env.globals.update(item=item)

@app.route("/")
def index():
    if (False):
        # return "Hello World"
        return render_template("index.html")
    else:
        return render_template("second.html")

if __name__ == "__main__":
    app.run()
