from flask import Blueprint, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

main = Blueprint('main', __name__)

load_dotenv()
UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "app/uploads")
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(save_path)
            flash(f"Soubor '{filename}' byl úspěšně nahrán.")
            return redirect(url_for("main.index"))

        flash("Nepodporovaný typ souboru. Povoleny: PDF, DOCX, TXT")
        return redirect(request.url)

    return render_template("index.html")
