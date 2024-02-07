# here's an app runs a simple web server

app = Flask(__name__)

# define product route
@app.route('/product', methods=['GET'])
def get_product():
    return 'Product'

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host='', port=5000)

@app.route('/person', methods=['POST'])
