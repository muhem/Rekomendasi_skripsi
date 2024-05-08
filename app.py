from flask import Flask, request, jsonify
from flask_cors import CORS
import Rekomendasi as recommendation

app = Flask(__name__)
CORS(app)

@app.route('/rekomendasi', methods=['GET'])
def recommend_movies():
    res = recommendation.hasil(recommendation.results(request.args.get('userId')))
    return jsonify(res)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
