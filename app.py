import json

from flask import Flask, request
from extensions import db
from flask_cors import CORS
import config
from flask_migrate import Migrate
from apis.ai_chat import chatAI_bp
from apis.ai_draw import drawAI_bp
# from models.chat import Chat
# from models.dialog_list import DialogList
# from models.draw_content import DrawContent
# from models.interaction import Interaction
# from models.users import User


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app, db)
CORS(app, resources=r'/*')
app.register_blueprint(chatAI_bp)
app.register_blueprint(drawAI_bp)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
