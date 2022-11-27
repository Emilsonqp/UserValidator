from server import create_app
from .modelos import db
from flask_restful import Api
from .vistas import VistaLogIn, VistaSignIn, VistaValidaAgenda, VistaCrearConsulta
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = create_app('default')
app_context = app.app_context()
app_context.push()
app.debug = True
db.init_app(app)
db.create_all()

cors = CORS(app)
api = Api(app)
api.add_resource(VistaSignIn, '/api/auth/signup')
api.add_resource(VistaLogIn, '/api/auth/login')
api.add_resource(VistaValidaAgenda, '/api/agenda')
api.add_resource(VistaCrearConsulta, '/api/consulta/<int:id_consulta>')

jwt = JWTManager(app)
