from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/pesapal/callback', methods=['POST'])
def pesapal_callback():
    # Get the response from PesaPal
    payment_status = request.json
    
    # Log or process the response
    print("Payment status received:", payment_status)
    
    # Do something with the payment status (update order, etc.)
    # Example: process_payment_status(payment_status)
    
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
