def send_sms():
    # Twilio credentials
    account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    auth_token = "SK1234567890abcdef1234567890abcdef"

    # Twilio phone numbers
    from_phone = "+1234567890"
    to_phone = "+0987654321"

    # Message body
    message_body = "Hello, this is a test message."

    print(f"Sending SMS from {from_phone} to {to_phone}: {message_body}")

if __name__ == "__main__":
    send_sms()
