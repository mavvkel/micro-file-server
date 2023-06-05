from flask import Blueprint, current_app, redirect, render_template, send_from_directory, url_for
from flask_login import login_required, current_user
import os

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
@login_required
def index():
    files_loc = os.path.join(current_app.root_path, "data")
    file_list = os.listdir(files_loc) 
    return render_template(template_name_or_list='index.html',
                           files=file_list,
                           name=current_user.name)

@main.route('/download/<path:filename>')
@login_required
def download(filename):
    print(current_app.root_path)
    # if 404 then flash msg
    return send_from_directory(directory=current_app.config['UPLOAD_FOLDER'],
                               path=filename,
                               as_attachment=True)
    #return redirect(url_for('main.index'))

#
#@app.route('/files', methods=['GET'])
#def getFiles():
#	return os.listdir('/tmp/d/')
#
#@app.route('/download/<path:name>')
#def downloadFile(name):
#	return send_from_directory('/tmp/d/',name)
#
#@app.route('/upload')
#def uploadFile(name):
#	if loggedIn:
#		f = request.files['file']
#		f.save('/tmp/d'+f.filename);
#		return 'File uploaded'
#	else:
#		return 'Login first'
#
#@app.route('/login/<username>/<password>', methods=['POST'])
#def login(username, password):
#	if(username == 'admin' and password == 'admin'):
#		loggedIn = True
#		return 'Login Success'
#	else:
#		return 'Bad credentials!'
#

# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0")
