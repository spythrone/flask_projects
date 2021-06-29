from flaskblog import create_app
from flaskblog.config import LocalDevConfig, LocalProdConfig, HerokuDevConfig, HerokuProdConfig, DockerDevConfig

configuration = DockerDevConfig

app = create_app(configuration=configuration)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
