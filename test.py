from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('main_equipment_page.html',name=name)

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
