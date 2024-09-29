def send_message(email, message):
    if not email:
        raise ValueError("Email address is missing")
    
    # Simulate sending the message (for now, just print to console)
    print(f"Sending message to {email}: {message}")

    ''''
    This modul were simulates sending message to an e-mail and with the genrated messages. 
    It also handles the if the e-mail is missing or somthing. 
    '''