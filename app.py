from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint for receiving callback notifications from Pesapal
@app.route('/pesapal/callback', methods=['POST', 'GET'])
def pesapal_callback():
    try:
        # Log request method and headers for debugging
        print(f"Request method: {request.method}")
        print(f"Request headers: {request.headers}")

        # Handle GET requests (Pesapal might use GET for callbacks)
        if request.method == 'GET':
            payment_status = request.args.to_dict()  # Parse query parameters
            print("Payment status received via GET:", payment_status)

        # Handle POST requests
        elif request.method == 'POST':
            # Check the Content-Type of the request
            if request.content_type == 'application/json':
                payment_status = request.json  # Parse JSON body
            else:
                # Fallback for non-JSON content
                payment_status = request.form.to_dict()

            print("Payment status received via POST:", payment_status)

        else:
            return jsonify({"status": "error", "message": "Unsupported HTTP method"}), 405

        # Process payment status
        if 'status' in payment_status:
            status = payment_status['status']
            if status == 'completed':
                print("Payment completed. Updating order status.")
            elif status == 'pending':
                print("Payment is pending.")
            elif status == 'failed':
                print("Payment failed.")
            else:
                print("Unknown payment status received.")
        else:
            print("No status field in payment status.")

        # Return success response to Pesapal
        return jsonify({"status": "Payment successful redirecting..."}), 200

    except Exception as e:
        print(f"Error processing callback: {e}")
        return jsonify({"status": "error", "message": str(e)}), 400

# Home route (you can add more routes as needed)
@app.route('/')
def home():
    return "Welcome to the Callback Payment System!"

if __name__ == '__main__':
    app.run(debug=False)
