from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint for receiving callback notifications from Pesapal
@app.route('/pesapal/callback', methods=['POST'])
def pesapal_callback():
    try:
        # Get the response from Pesapal
        payment_status = request.json

        # Log the raw request data for debugging
        print("Raw Payment Status Received:", request.data)

        # Log or process the response
        print("Payment status received:", payment_status)
        
        # Example of processing payment status
        if 'status' in payment_status:
            # Implement your order update logic based on the payment status
            if payment_status['status'] == 'completed':
                print("Payment completed. Updating order status.")
            elif payment_status['status'] == 'pending':
                print("Payment is pending.")
            elif payment_status['status'] == 'failed':
                print("Payment failed.")
            else:
                print("Unknown payment status received.")
        else:
            print("No status field in payment status.")
        
        # Return a success response to Pesapal
        return jsonify({"status": "success"}), 200

    except Exception as e:
        print(f"Error processing callback: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

# Home route (you can add more routes as needed)
@app.route('/')
def home():
    return "Welcome to the Callback Payment System!"

if __name__ == '__main__':
    app.run(debug=True)
