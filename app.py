from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/index')
def chatroom():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    from flask import request, jsonify

    faq_responses = {
        # English FAQs
        "check-in time": "Check-in starts at 2:00 PM.",
        "check in time": "Check-in starts at 2:00 PM.",
        "what time is check-in": "Check-in is available from 2:00 PM.",
        "checkout time": "Checkout is at 11:00 AM.",
        "check-out time": "Checkout is at 11:00 AM.",
        "restaurant hours": "Our restaurant is open daily from 7:00 AM to 10:00 PM.",
        "breakfast time": "Breakfast is served from 7:00 AM to 10:00 AM.",
        "wifi password": "The Wi-Fi password is: marloo123.",
        "do you have wifi": "Yes, free Wi-Fi is available throughout the hotel. Password: marloo123.",
        "pool hours": "The pool is open from 8:00 AM to 8:00 PM.",
        "spa hours": "Our spa is open from 10:00 AM to 6:00 PM.",
        "parking": "Yes, we offer free parking for all guests.",
        "airport shuttle": "Yes, we offer airport shuttle service. Please contact reception to schedule.",

        # Sinhala FAQs
        "check-in වෙලාව": "Check-in වෙලාව 2:00 PM ට ආරම්භ වේ.",
        "check out වෙලාව": "Check-out වෙලාව 11:00 AM.",
        "අදාල වෙලාව": "Check-in 2:00 PM සිටයි. Check-out 11:00 AM.",
        "අපේ wifi": "ඔව්, අපේ Wi-Fi එකේ password එක: marloo123.",
        "wifi password එක": "Wi-Fi password එක: marloo123.",
        "ආපනශාලාවේ වෙලාවන්": "අපේ ආපනශාලාව සෑම දිනකම 7:00 AM - 10:00 PM විවෘත වේ.",
        "නැවුම් ආහාර වේලාව": "නැවුම් ආහාර 7:00 AM - 10:00 AM.",
        "පාකීය වේලාවන්": "Swimming pool එක විවෘතයි 8:00 AM - 8:00 PM.",
        "spa එක": "Spa එක විවෘතයි 10:00 AM - 6:00 PM.",
        "පාර්ක්": "ඔව්, අපේ අමුත්තන්ට නොමිලේ පාර්ක් කිරීම් ඇත.",
        "ගුවන්තොටුපළ වාහනය": "ඔව්, shuttle සේවාවක් ඇත. කරුණාකර reception අමතන්න."
    }

    def get_response(user_input):
        user_input = user_input.lower().strip()
        for key in faq_responses:
            if key in user_input:
                return faq_responses[key]
        return "I'm sorry, I didn't understand. Try asking about check-in, Wi-Fi, or restaurant hours. ඔබට උදව්වක් අවශ්‍යද? Check-in, Wi-Fi, නැවතුම් ගන්න පුළුවන්."

    user_message = request.json.get('message', '')
    bot_response = get_response(user_message)
    return jsonify(response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)
