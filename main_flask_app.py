from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('main_equipment_page.html')

@app.route('/search/<condition>')
def enter_values(condition=None):
    return "search page"


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