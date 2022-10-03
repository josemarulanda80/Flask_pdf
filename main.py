
from flask import Flask,render_template,make_response
import pdfkit
app =Flask(__name__)

@app.route('/<name>/<location>')
def home(name,location):
    
    path_wkthmltopdf = b'C:\Program Files\wkhtmltopdf\\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkthmltopdf)



    res = render_template("index.html",name=name,location=location)
    responsestring=pdfkit.from_string(res,False,configuration=config)
    response=make_response(responsestring)
    response.headers['Content-Type']='application/pdf'
    response.headers['Content-Disposition']='inline;filename=output.pdf'
    return response

if __name__=="__main__":
    app.run(debug=True)