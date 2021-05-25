from flaskblog import create_app
from flaskblog.config import BaseConfig, DevConfig, ProductionConfig

app = create_app(configuration=DevConfig)

if __name__ == "__main__":
    app.run()
