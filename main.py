from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/requirements_gathering")
def requirements_gathering():
    return render_template("requirements_gathering.html")

@app.route("/conceptual_design")
def conceptual_design():
    return render_template("conceptual_design.html")

@app.route("/detailed_design")
def detailed_design():
    return render_template("detailed_design.html")

@app.route("/prototype_development")
def prototype_development():
    return render_template("prototype_development.html")

@app.route("/testing_and_validation")
def testing_and_validation():
    return render_template("testing_and_validation.html")

@app.route("/documentation")
def documentation():
    return render_template("documentation.html")

@app.route("/manufacturing")
def manufacturing():
    return render_template("manufacturing.html")

@app.route("/continuous_improvement")
def continuous_improvement():
    return render_template("continuous_improvement.html")

if __name__ == "__main__":
    app.run()
