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
# RaviCard AI Assistant Logic
def ravicard_ai_response(user_query):
    query = user_query.lower()
    
    # ग्राहकों के लिए AI का जवाब
    if "सस्ता" in query or "cheap" in query:
        return "RaviCard AI: हमारे पास सबसे सस्ता सामान 'किराना' सेक्शन में उपलब्ध है। क्या मैं लिस्ट दिखाऊं?"
    
    elif "दुकान" in query or "shop" in query:
        return "RaviCard AI: आपके आस-पास 5 दुकानें खुली हैं। आप 'Visit' बटन दबाकर टाइम कन्फर्म कर सकते हैं।"

    # दुकानदारों के लिए AI का जवाब
    elif "बिक्री" in query or "sales" in query:
        return "RaviCard AI: आज आपके पास 10 नए ग्राहक आए। सबसे ज्यादा मांग 'जूतों' की है।"

    else:
        return "RaviCard AI: मैं आपकी कैसे मदद कर सकता हूँ? आप सामान या दुकान के बारे में पूछ सकते हैं।"

# उदाहरण के लिए टेस्ट
print(ravicard_ai_response("सबसे सस्ता सामान दिखाओ"))