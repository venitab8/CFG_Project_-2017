from flask import Flask
from flask import render_template, request, redirect
app = Flask(__name__)


search_words = []

@app.route('/')
def main_page():
    return render_template('main_equipment_page.html')

@app.route('/search/<condition>')
def display_search_page(condition=None):
    return render_template('search_page.html')

'''Currently request.form is empty :('''
@app.route('/search',methods=['GET','POST'])
def enter_values():
    #search_words = request.args('search')
    #search_words = request.form['text']
    return search_words

@app.route('/results/<condition>')
def results(condition=None):
	return "result page"
    
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
    app.run()
