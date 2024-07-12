from flask import Flask
from api.ddb_log import bp as ddb_log_bp
from api.pt_region import bp as pt_region_bp


app = Flask(__name__)

app.register_blueprint(ddb_log_bp, url_prefix='/')
app.register_blueprint(pt_region_bp, url_prefix='/')


@app.route('/', methods=['GET', 'POST'])
def health_check():
    return 'Server is running'

if __name__ == "__main__":
    app.run(debug=True)
