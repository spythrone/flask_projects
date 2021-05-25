from flaskblog import create_app
from flaskblog.config import LocalDevConfig, LocalProdConfig, HerokuDevConfig, HerokuProdConfig

app = create_app(configuration=LocalDevConfig)

if __name__ == "__main__":
    app.run()
