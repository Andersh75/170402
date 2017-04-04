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
    return render_template("index.html")
    

if __name__ == "__main__":
    app.run()
