from flask import Blueprint, current_app, redirect, render_template, send_from_directory, url_for
from flask_login import login_required, current_user
from pathlib import Path
from glob import glob
import os

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
@login_required
def index():
    files_loc = os.path.join(current_app.root_path, "data")

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
