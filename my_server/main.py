from flask import Blueprint, current_app, redirect, render_template, \
        request, send_from_directory, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
# from pathlib import Path
from glob import glob
import os

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    files_loc = os.path.join(current_app.root_path, "data")

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part in the request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(files_loc, filename))

    #file_list = [os.path.join(dp, f) for dp, dn, filenames in os.walk(PATH) for f in filenames if os.path.splitext(f)[1] == '.txt']

    #file_list = list(Path(files_loc).rglob("*"))

    rel_file_list = glob(pathname="./**",
                         root_dir=files_loc,
                         recursive=True)
    abs_file_list = glob(pathname="./my_server/data/**",
                         recursive=True)
    files = []

    for i in range(len(abs_file_list)):
        if not os.path.isdir(abs_file_list[i]):
            files.append(rel_file_list[i][1::])

    return render_template(template_name_or_list='index.html',
                           files=files,
                           name=current_user.name)


@main.route('/download/<path:filename>')
@login_required
def download(filename):
    # print(current_app.root_path)
    # if 404 then flash msg
    print(filename)
    filename = filename.replace('\\', '/')

    #path = filename.rep
    return send_from_directory(directory=current_app.config['UPLOAD_FOLDER'],
                               path=filename[1::],
                               as_attachment=True)
