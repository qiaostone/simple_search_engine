from flask import Flask
from flask import Flask, url_for, redirect, render_template,request
from search_engine import *


app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        print("1")
        keywords = request.form['keywords_input']
        results = search_kws(keywords)
        if len(results) > 0:
            return render_template('news_list.html', results=results)
        else:
            error_dict = {}
            error_dict['title'] = ""
            error_dict['Lcontent'] = "No result"
            error_dict['page_number'] = ""
            error = [error_dict]
            return render_template('news_list.html', results=error)


    return render_template('index.html')

@app.route('/web/<page_number>')
def get_new(page_number):
    print(page_number)
    return render_template('./web/{}'.format(page_number))

@app.route('/test')
def test():
    results = search_kws("wavelength")
    return render_template('news_list.html',results=results)



if __name__ == '__main__':
    app.run()
