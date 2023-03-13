
import os
from pathlib import Path

from flask import Flask
from flask import Response
from flask import send_file
from flask_restx import Api
from flask_restx import Resource
from flask_cors import CORS

from werkzeug.datastructures import FileStorage
from service.imagesService import ImagesService

app = Flask(__name__)
api = Api(app)
CORS(app)

tickets_namespace = api.namespace('')
articles_namespace = api.namespace('articles')

attachement_request = api.parser()
attachement_request.add_argument(
    'file', location='files', type=FileStorage, required=True
)

@tickets_namespace.route('/<string:iso_date_prefix>/<string:image_name>')
class TicketsNameSpace(Resource):

    def get(self, iso_date_prefix, image_name):
        print(f"{iso_date_prefix=}, {image_name=}")
        location = Path("D:\\minio\\ticket") / 'ticket' / iso_date_prefix / image_name
        if os.path.exists(location):
            return send_file(location, mimetype='image/png')
        return Response(image_name, 404)

@articles_namespace.route('/<string:image_name>')
class ArticlesNameSpace(Resource):

    def get(self, image_name):
        print(f"{image_name=}")
        location = Path("D:\\minio\\ticket") / 'article' / 'articles' / image_name
        if os.path.exists(location):
            return send_file(location, mimetype='image/png')
        return Response(image_name, 404)


if __name__ == '__main__':
    app.run(debug=True, port=9001)
