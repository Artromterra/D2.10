import os
import sentry_sdk

from bottle import Bottle, run, response
from sentry_sdk.integrations.bottle import BottleIntegration

sentry_sdk.init(
    dsn="https://185dff922e3342778a26a4dcd26bfaff@sentry.io/1849735",
    integrations=[BottleIntegration()]
)

app = Bottle()

@app.route("/success")
def success_response():
	return response.status

@app.route("/fail")
def fail_response():
	raise RuntimeError("Just an Error!!!")
	return

if os.environ.get("APP_LOCATION") == "heroku":
	app.run(
		host="0.0.0.0",
		port=int(os.environ.get("PORT", 5000)),
		server="gunicorn",
		workers=3,
		)
else:
	app.run(host="localhost", port=8080, debug=True)