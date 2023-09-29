import os
from flask import Flask, request, render_template, send_file
from PIL import Image
from PyPDF2 import PdfFileWriter, PdfFileReader

app = Flask(__name)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    uploaded_file = request.files['image']

    if uploaded_file.filename != '':
        img = Image.open(uploaded_file)
        pdf = PdfFileWriter()
        pdf.addPage(img.convert('RGB'))

        pdf_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'output.pdf')

        with open(pdf_filename, 'wb') as pdf_file:
            pdf.write(pdf_file)

        return send_file(pdf_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
