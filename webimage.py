from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
import pandas as pd

# file을 submit하는 페이지
# /upload 의 페이지로 들어와서, upload.html의 파일을 렌더링하여 보여줌
# 여기서, upload.html은 프로젝트 폴더 내의 templates 폴더에 존재해야 함(default)
app = Flask(__name__)
@app.route('/upload')
def render_file():
    return render_template('upload.html')

# file이 submit되면 전달되는 페이지
# upload.html에서 form이 제출되면 /file_uploaded로 옮겨지게 되어 있음.
@app.route('/file_uploaded', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST': # POST 방식으로 전달된 경우
        f = request.files['file1']
        # 파일 객체 혹은 파일 스트림을 가져오고, html 파일에서 넘겨지는 값의 이름을 file1으로 했기 때문에 file1임.
        f.save(f'uploads/{secure_filename(f.filename)}') # 업로드된 파일을 특정 폴더에저장하고,
        df_to_html = pd.read_csv(f'uploads/{secure_filename(f.filename)}').to_html() # html로 변환하여 보여줌
        return df_to_html

if __name__ == '__main__':
    # debug를 True로 세팅하면, 해당 서버 세팅 후에 코드가 바뀌어도 문제없이 실행됨.
    app.run(host='0.0.0.0', port=5000, debug = True)
