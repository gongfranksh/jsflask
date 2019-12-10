
import os

from api import create_app
from config import configuration

from tools.exts import logger
from utils.log_helper import init_log

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

init_log()
# api.init_app(app)
# logger.init_app(app)

if __name__ == '__main__':
    host, port, debug = configuration.get_start_config()
    app.run(host=host, port=port, debug=eval(debug))