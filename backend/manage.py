from core import create_app
from dapr.conf import settings

app = create_app()

if __name__== '__main__':
    app.run(port=settings.HTTP_APP_PORT)