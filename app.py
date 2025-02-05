from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Enable Prometheus metrics
metrics = PrometheusMetrics(app)

@app.route("/wish")
def pleaseWish():
    return "Hello, Jenkins"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port="5000")

# 0.0.0.0 ==> all Traffic
# The default port no is always 5000

