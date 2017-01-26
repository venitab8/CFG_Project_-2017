import backend
import time
import util
from flask import Flask
from flask import render_template, request, redirect
from os import environ
import flask_excel as excel

from rq import Queue
from worker import conn

q = Queue(connection=conn)

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
    if len(q)==0:
        #start a new job to conduct the search
        job=q.enqueue_call(func=backend.do_search,
               args=(search_words, condition,),
               timeout=30)
        time.sleep(6)
        return redirect('/results/'+ condition+"/"+ job.id+ "?search=" + search_words)
    else:
        #select the first job that is running
        queued_jobs = q.jobs
        job=queued_jobs[0]
        return redirect('/results/'+ condition+"/"+ job.id +"?search=" + search_words)


@app.route('/results/<condition>/<job_id>')
def wait_and_display_results(condition=None,  job_id=None):
    job = q.fetch_job(job_id)
    search_words = request.args.get('search')
    if job==None:
        try:
            return redirect('/results/'+ condition+"/" + "?search=" + search_words)
        except:
            return "Invalid Address"
    elif job.is_finished:
        is_keyword_matched, message, result=job.result
        median = util.median_price(result)
        return render_template('result_page.html', search_words=search_words,result=result, median=median,message=message, condition=condition)
    else:
        #check every 6 seconds for a result
        time.sleep(6)
        return redirect('/results/'+ condition+"/"+ job.id +"?search=" + search_words)

@app.route('/download/<search_words>/', methods=['GET'])
def download_file(search_words, condition=None):
    #is_keyword_matched, message, result=q.enqueue(backend.do_search, search_words, condition)
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
    app.run(host='127.0.0.1', port=port)
    #app.run()
