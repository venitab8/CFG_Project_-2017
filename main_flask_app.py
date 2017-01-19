from flask import Flask
from flask import render_template, request, redirect
app = Flask(__name__)


search_words = []
search_condition=None

@app.route('/')
def main_page():
    return render_template('main_equipment_page.html')

@app.route('/search/<condition>')
def display_search_page(condition=None):
    if condition != "new" and condition != "used":
        return "Invalid address"
    search_condition=condition
    search_words = request.args.get('search')
    return render_template('search_page.html',condition=condition)

@app.route('/search',methods=['GET','POST'])
def enter_values():
    search_words = request.args.get('search')
    return search_words
    #return redirect('results/'+search_condition+"/"+search_words)

@app.route('/results/<condition>/')
def results(search_words=None):
	return render_template('result_page', search_words=search_words)
    
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
