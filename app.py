import json
from flask import Flask, request
from apis.notify import notify_bp
from apis.user import user_bp
from extensions import db
from flask_cors import CORS
import config
from flask_migrate import Migrate
from apis.weather_assistance import weather_bp
from apis.ai_search import searchAI_bp
from apis.ai_draw import drawAI_bp
from apis.ai_chat import chatAI_bp

# from models.chat import Chat
# from models.dialog_list import DialogList
# from models.draw_content import DrawContent
# from models.interaction import Interaction
# from models.users import User


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(chatAI_bp)
app.register_blueprint(user_bp)
app.register_blueprint(notify_bp)
app.register_blueprint(weather_bp)
app.register_blueprint(searchAI_bp)
app.register_blueprint(drawAI_bp)

CORS(app, resources={r"/*": {"origins": "*"}})
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
