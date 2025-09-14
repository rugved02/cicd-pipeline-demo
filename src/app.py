from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <h1>🚀 CI/CD Pipeline Demo</h1>
    <p>Hello from our Dockerized Flask App!</p>
    <p>This app was built and deployed using GitHub Actions!</p>
    <p>Environment: Production</p>
    <p>Version: 1.0.0</p>
    """

@app.route('/health')
def health():
    return {'status': 'healthy', 'message': 'Application is running successfully!'}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
