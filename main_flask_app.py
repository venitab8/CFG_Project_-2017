import backend
import util
from flask import Flask
from flask import render_template, request, redirect
from os import environ
import flask_excel as excel
import json

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
def run_search(condition=None):
    search_words = request.args.get('search')
    #split websites we scrape into groups to prevent timeouts. currently func_group only used for used equipment
    func_group = request.args.get('func_group') 
    is_keyword_matched, message, results= backend.do_search(search_words,condition, func_group)
    if len(results)>3 or func_group=='2' or condition=='new':
        #we have enough results or we searched all our functions
        median = util.price_prettify(util.median_price(results))
        for item in results:
            item.price = util.price_prettify(util.str_to_float(item.price))
        return render_template('result_page.html', search_words=search_words,result=results, median=median,message=message, condition=condition)
    else:
        #try the next group
        return redirect('/results/'+ condition + "/?search=" + search_words + "&func_group=" + '2')

@app.route('/download/<search_words>/', methods=['GET'])
def download_file(search_words, condition=None):
    is_keyword_matched, message, result= backend.do_search(search_words,condition)
    exported_list=[['Title','Price', 'Image', 'URL']]
    for r in result:
        exported_list.append([r.title, r.price, r.image_src, r.url])
    print exported_list
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
    app.run(host='127.0.0.1', port=port)
    #app.run()
