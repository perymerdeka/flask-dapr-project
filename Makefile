dapr-run:
	dapr run --app-id api --app-port 5000 --dapr-http-port 5000 python backend/manage.py

dapr-dashboard:
	dapr dashboard