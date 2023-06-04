from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db
import os

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
@login_required
def index():
    file_list = os.listdir('data') 
    return render_template(template_name_or_list='index.html',
                           files=file_list,
                           name=current_user.name)

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
