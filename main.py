from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Charger la clé API depuis la variable d'environnement
API_KEY = os.getenv('NEWS_API_KEY')

# Route pour obtenir les actualités
@app.route('/api/news', methods=['GET'])
def get_news():
    # Paramètre de la requête avec une valeur par défaut
    source = request.args.get('source', 'bbc-news')
    url = f'https://newsapi.org/v2/top-headlines?sources={source}&apiKey={API_KEY}'
    
    try:
        # Effectuer la requête à l'API externe
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return jsonify(data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
