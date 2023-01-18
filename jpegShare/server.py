
from flask import Flask
from flask import Response
from flask import send_file
from flask_restx import Api
from flask_restx import Resource
from flask_cors import CORS

from werkzeug.datastructures import FileStorage
from service.imagesService   import ImagesService

app = Flask(__name__)
api = Api(app)
CORS(app)

image_namespace = api.namespace('attachement')

attachement_request = api.parser()
attachement_request.add_argument('file', location='files', type=FileStorage, required=True)

class AttachementEndpoints(Resource):

    def __getImagePath(categorie : str, imageName : str) -> str:
        if categorie == 'ticket':
            return ImagesService.getTicketImageLink(f"{imageName}.0")
        elif categorie == 'icon':
            return ImagesService.getIconsImageLink(imageName)
        elif categorie == 'article':
            return ImagesService.getArticlesImageLink(imageName)
        return None

    def get(self, categorie, imageName):

        filename = AttachementEndpoints.__getImagePath(categorie, imageName)

        if filename is None:
            return Response('', 404)

        if not ImagesService.locationExist(filename):
            return Response(imageName, 404)

        return send_file(filename, mimetype='image/png')

    def post(self, categorie, imageName):

        filename = AttachementEndpoints.__getImagePath(categorie, imageName)

        if filename is None:
            return Response('', 400)

        if ImagesService.locationExist(filename):
            return Response(imageName, 409)

        args = attachement_request.parse_args()
        uploaded_file = args['file']
        uploaded_file.save(filename)

        if ImagesService.locationExist(filename):
            return Response(imageName, 201)
        
        return Response(None, 500)

@image_namespace.route('/ticket/<string:imageName>')
class AttachementTicketEndpoints(AttachementEndpoints):

    def get(self, imageName):
        return super().get('ticket', imageName)

    @api.expect(attachement_request)
    def post(self, imageName):
        return super().post('ticket', imageName)
        
@image_namespace.route('/icon/<string:imageName>')
class AttachementIconEndpoints(AttachementEndpoints):

    def get(self, imageName):
        return super().get('icon', imageName)

    @api.expect(attachement_request)
    def post(self, imageName):
        return super().post('icon', imageName)
        
@image_namespace.route('/article/<string:imageName>')
class AttachementArticleEndpoints(AttachementEndpoints):

    def get(self, imageName):
        return super().get('article', imageName)

    @api.expect(attachement_request)
    def post(self, imageName):
        return super().post('article', imageName)

if __name__ == '__main__':
    app.run(debug=True)