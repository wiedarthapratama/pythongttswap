import os
import shutil
import flask 
import flask_restful
from gtts import gTTS

app = flask.Flask(__name__, static_url_path='/static')
api = flask_restful.Api(app)

class HelloWorld(flask_restful.Resource):

    def post(self):
        json_data = flask.request.form
        id = json_data['id']
        judul = json_data['judul']
        deskripsi = json_data['deskripsi']

        mytext = judul+" "+deskripsi

        language = 'id'
        myobj = gTTS(text=mytext, lang=language, slow=False)
        filename = "file-"+id+".mp3"
        try:
            os.remove("static/"+filename)
        except OSError:
            pass
        myobj.save(filename)

        shutil.move(filename, "static/"+filename)

        file = os.path.join("/static", filename)
        return flask.jsonify(id=id, judul=judul, deskripsi=deskripsi, file=file)

api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    app.run(debug=True)
