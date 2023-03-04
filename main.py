import ast
import json

from flask import Flask, redirect, render_template, request, send_file, url_for

from acro_handle import Acro_Handle

app = Flask(__name__)
acro = Acro_Handle()


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        # grab our shit
        input_acronym = request.form.get("acro-name", "").upper()
        output_acronym = acro.get_acro(input_acronym)
        output_acronym = {"name": output_acronym[0], "description": output_acronym[1]}

        return render_template("index.html", acronym=output_acronym)

    # for random
    output_acronym = request.args.get("acronym", "")
    if output_acronym:
        output_acronym = ast.literal_eval(output_acronym)

    return render_template("index.html", acronym=output_acronym)


@app.route("/random")
def random_acronym():

    output_acronym = acro.get_random_acronym()
    output_acronym = {"name": output_acronym[0], "description": output_acronym[1]}

    return redirect(url_for("home", acronym=output_acronym))


@app.route("/download")
def download_acronyms():
    path = "./acronyms.txt"
    return send_file(path, as_attachment=True)


if __name__ == "__main__":
    app.run()
