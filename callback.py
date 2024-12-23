from flask import Flask, request

app = Flask(__name__)

@app.route('/payment_callback', methods=['POST'])
def payment_callback():
    """Handle Pesapal payment status updates."""
    data = request.json  # Pesapal sends payment info as JSON
    print("Callback received:", data)  # For debugging, print the received data

    # Extract relevant details (these fields are examples, check Pesapal's documentation)
    order_tracking_id = data.get('order_tracking_id')
    payment_status = data.get('payment_status')
    ammount = data.get('ammount')

    # Log or process the payment confirmation
    if payment_status == "COMPLETED":
        print(f"Payment successful for order {order_tracking_id}. Amount: {ammount}")
        # Update your database to mark the payment as completed
        # e.g., update_payment_status(order_tracking_id, "COMPLETED")
    else:
        print(f"Payment failed or pending for order {order_tracking_id}. Status: {payment_status}")

    return "OK", 200  # Pesapal expects a 200 response to confirm receipt of the callback

