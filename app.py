from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/pesapal/callback', methods=['POST'])
def pesapal_callback():
    try:
        # Get the response from PesaPal
        payment_status = request.json
        
        # Log or process the response
        print("Payment status received:", payment_status)
        
        # Example of processing payment status
        # You might want to extract relevant information here
        if 'status' in payment_status:
            # Update your order based on payment status
            # For example, if payment_status['status'] == 'completed':
            #     update_order_status(payment_status)
            pass  # Replace with actual processing logic
        
        # Return a success response to PesaPal
        return jsonify({"status": "success"}), 200

    except Exception as e:
        print(f"Error processing callback: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
