from flask import Flask, request, render_template, send_file
import subprocess
import os
import tempfile
import uuid
import shutil  

app = Flask(__name__)


def compile_latex(latex_code):
    random_filename = str(uuid.uuid4())
    
    temp_dir = tempfile.mkdtemp()
    
    tex_file_path = os.path.join(temp_dir, f'{random_filename}.tex')
    with open(tex_file_path, 'w') as tex_file:
        tex_file.write(latex_code)
    
    process = subprocess.Popen(['pdflatex', '-interaction=nonstopmode', f'{random_filename}.tex'], cwd=temp_dir, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    
    pdf_file_path = os.path.join(temp_dir, f'{random_filename}.pdf')
    if os.path.exists(pdf_file_path):
        return pdf_file_path
    else:
        print("PDF file not found:", pdf_file_path)
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        latex_code = request.form['latex_code']
        pdf_file_path = compile_latex(latex_code)
        if pdf_file_path:
            try:
                return send_file(pdf_file_path, as_attachment=True)
            finally:
                # cleanup
                temp_dir = os.path.dirname(pdf_file_path)
                if temp_dir.startswith(tempfile.gettempdir()) and os.path.exists(temp_dir):
                    shutil.rmtree(temp_dir)
        else:
            return "Failed to compile LaTeX code."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
