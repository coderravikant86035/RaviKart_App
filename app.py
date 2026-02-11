# RaviCard App - Basic Backend with AI logic
from flask import Flask, jsonify, request

app = Flask(__name__)

# दुकानदारों का डेटा (उदाहरण के लिए)
products = [
    {"id": 1, "name": "Sofa", "price": 5000, "category": "Furniture"},
    {"id": 2, "name": "Laptop", "price": 45000, "category": "Electronics"}
]

@app.route('/')
def home():
    return "<h1>Welcome to RaviCard AI Store</h1>"

# AI फीचर: ग्राहक की पसंद के हिसाब से सामान दिखाना
@app.route('/recommend', methods=['GET'])
def recommend_products():
    # यहाँ भविष्य में AI मॉडल लगेगा जो कस्टमर की पसंद बताएगा
    return jsonify({"message": "AI recommends these top products", "data": products})

if __name__ == '__main__':
    app.run(debug=True)
