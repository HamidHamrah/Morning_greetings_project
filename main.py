import csv
from ContactsManager import ContactsManager  # Now using ContactsManager
from message_generator import generate_message
from message_sender import send_message
from logger import log_message

# Function to read contacts from a CSV file
def read_contacts_from_csv(filename):
    contacts_manager = ContactsManager()  # Initialize ContactsManager
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                name = row.get('name')
                email = row.get('email')
                preferred_time = row.get('preferred_time', "08:00 AM")
                if name and email:
                    contacts_manager.add_contact(name, email, preferred_time)
                else:
                    print(f"Skipping invalid entry in CSV: {row}")
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except Exception as e:
        print(f"Error while reading contacts from CSV: {e}")
    
    return contacts_manager

# Main function
def main():
    # Read contacts from a CSV file
    contacts_manager = read_contacts_from_csv('contacts.csv')
    
    # Check if the contact list is empty
    if not contacts_manager.get_contacts():
        print("No contacts available to send messages.")
        return

    # Loop through the contacts and handle errors during the process
    for contact in contacts_manager.get_contacts():
        try:
            # Generate personalized message
            message = generate_message(contact['name'])
            
            # Simulate sending the message
            send_message(contact['email'], message)
            
            # Log the message
            log_message(contact, message)
        
        except ValueError as ve:
            print(f"Error with contact {contact['name']}: {ve}")
        except Exception as e:
            print(f"Unexpected error when processing {contact['name']}: {e}")

if __name__ == "__main__":
    main()