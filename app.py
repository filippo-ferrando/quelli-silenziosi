from flask import Flask, request, render_template
import os

app = Flask(__name__)

default_filename = "default.png"

UPLOAD_FOLDER = 'static/img/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["TEMPLATES_AUTO_RELOAD"] = True

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        file = request.files['image']
        if(file.filename == ''):
            with open("entries.txt", "a") as f:
                f.write(f"{name} - {comment} - {default_filename}\n")
            return render_template('index.html', name=name, comment=comment, image_file=default_filename)
        else:
            if file and allowed_file(file.filename):
                filename = file.filename
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                with open("entries.txt", "a") as f:
                    f.write(f"{name} - {comment} - {filename}\n")
                return render_template('index.html', name=name, comment=comment, image_file=filename)
    with open("entries.txt", "r") as f:
        entries = f.readlines()
    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)