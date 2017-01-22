import backend
from flask import Flask
from flask import render_template, request, redirect
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
    #print(str(do_search(search_words))
    #return render_template('result_page.html', search_words=search_words)
    result= str(backend.do_search(search_words,condition))
    return render_template('result_page.html', search_words=search_words,result=result)

    
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
