import backend
from flask import Flask
from flask import render_template, request, redirect
import flask_excel as excel
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main_equipment_page.html')

@app.route('/search/<condition>')
def display_search_page(condition=None):
    if condition != "new" and condition != "used":
        return "Invalid address"
    return render_template('search_page.html',condition=condition)

@app.route('/results/<condition>/')
def results(condition=None):
    search_words = request.args.get('search')
    is_keyword_matched, message, result= backend.do_search(search_words,condition)
    return render_template('result_page.html', search_words=search_words,result=result, message=message, condition=condition)

@app.route('/download/<search_words>/', methods=['GET'])
def download_file(search_words, condition=None):
    is_keyword_matched, message, result= backend.do_search(search_words,condition)
    exported_list=[['Title','Price', 'Image', 'URL']]
    for r in result:
        exported_list.append([r.title, r.price, r.image_src, r.url])
    return excel.make_response_from_array(exported_list, "xls")

def finish(self):
         if not self.wfile.closed:
            self.wfile.flush()
            try:
                self.wfile.flush()
            except socket.error:
                # An final socket error may have occurred here, such as
                # the local error ECONNABORTED.
                pass
         self.wfile.close()
         self.rfile.close()
        
if __name__== "__main__":
    port = int(environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    #app.run()
