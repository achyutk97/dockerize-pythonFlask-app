from flask import Flask,  jsonify,  render_template
import socket
app = Flask(__name__)

def fetchHostAndIp():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return host_name, host_ip

@app.route("/")
def root():
    return "Hello World!"

@app.route("/health")
def health():
    return jsonify(
        status = "Up"
    )

@app.route("/details")
def details():
    host_name, host_ip = fetchHostAndIp()
    return render_template('index.html', HOSTNAME=host_name, IP=host_ip)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= "8080")
