# Morning Greetings Automation
## Introduction
Morning Greetings Automation is a Python project designed to automate the process of sending personalized “Good Morning” messages to a list of friends. The project organizes the task into distinct modules that handle managing contacts, generating personalized messages, simulating the sending of those messages, and logging the events. It’s a practical exercise in using Python for scripting and automation, suitable for students and developers looking to enhance their skills with file I/O, packages, and error handling.

## How the Problem is Solved
### The problem is approached by building a Python package that handles the entire greeting process, broken down into the following components: 
* Managing Contacts: A contact manager is used to maintain a list of friends, including their names, emails, and preferred greeting times. This data is stored in a CSV file, which the program reads to dynamically manage the contact list.
*	Message Generation: A message generator module is responsible for creating personalized “Good Morning” messages based on the contact’s name.
*	Simulating Message Sending: A message sender module simulates sending the message by printing the result to the console, including validation for missing email addresses.
* Logging: The logger module logs every message sent, along with a timestamp, to a log file.
### The project emphasizes modular design, where each component is decoupled and reusable, following Python best practices for file I/O and error handling.

## Real-World Application
While the project simulates sending messages and logging events, it could easily be adapted to a real-world application with minimal changes. For example: 
* Real-World Example: By integrating with an actual email service (like smtplib or external APIs like SendGrid or Mailgun), this project could send real emails to contacts based on the generated greetings. The framework is already in place; the core functionality only requires modifying the message sending logic.

For now, this is a simulation designed for educational purposes, demonstrating Python scripting, file handling, and automation.
## Project Structure
    Morning_greetings_project
    │
    ├── /morning_greetings      # Package directory containing modules
    │   ├── __init__.py         # Package initializer
    │   ├── Contact.py          # Manages contacts
    │   ├── message_generator.py# Generates personalized messages
    │   ├── message_sender.py   # Simulates sending the messages
    │   └── logger.py           # Logs the sent messages
    │
    ├── contacts.csv            # Stores contact information (name, email, preferred time)
    ├── main.py                 # Main script to run the automation
    ├── README.md               # Documentation file
    └── setup.py                # Setup script for package installation

## How to Run the Project
### Step 1: Set up the Project 
* Clone or download the project files to your local system.
* Navigate to the project directory where setup.py is located.
###  Step 2: Install the Package
 Ensure you have Python and pip installed. Run the following command from the project root directory to install the package: 
 # 
     pip install .
Alternatively, if pip is not available, you can use: 
# 
    python3 -m pip install .
###  Step 3: Prepare the Contacts List
 Ensure that you have a contacts.csv file in the project directory. It should contain the names, emails, and preferred greeting times in the following format:

# 
    name,email,preferred_time
    Alice,alice@example.com,08:00 AM
    Bob,bob@example.com,09:00 AM
    Charlie,charlie@example.com,07:30 AM    
### Step 4: Run the Script

You can now run the main script to execute the entire process of generating, sending, and logging messages.

# 
     python main.py