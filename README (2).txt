# Hotel Marloo Guest Chat Assistant

---

## a) Project Title
Hotel Marloo Guest Chat Assistant

## b) Task Option Chosen
This project is an example of a simple chatbot that could be part of a larger hotel management system or a standalone guest service. It aligns with the idea of improving customer interaction for a hotel.

## c) Technologies Used
* Backend: Python (Flask framework)
* Frontend: HTML, CSS, JavaScript

## d) Features Implemented
* Interactive Chat Interface: A user-friendly web interface for guests to ask questions.
* Multilingual FAQ Responses: Provides pre-defined answers to common hotel guest questions in both English and Sinhala.
* Dynamic Chat Display: Messages are dynamically added to the chatbox as users interact.
* New Chat Functionality: Allows users to clear the conversation and start a new chat.
* Navigation: Provides options to navigate between the login page and the chatroom.

## e) Instructions to Run the Project

1.  Prerequisites:
    * Ensure you have Python installed (Python 3.x is recommended).
    * Install Flask:
        ```bash
        pip install Flask
        ```

2.  Project Structure:
    
    geust_chatbot/
    ├── app.py
    └── templates/
        ├── index.html
        └── login.html
    ```

3.  File Content:
    * `app.py`: Save the Python code  into this file.
    * `templates/index.html`**: Save the main chat interface HTML/CSS/JS code into this file.
    * `templates/login.html`**: For the `/` route to work,  need a `login.html` file.
4.  Run the Flask Application:
    * Open your terminal or command prompt.
    * Navigate to your `hotel_chatbot` directory:
        ```bash
        cd hotel_chatbot
        ```
    * Run the Flask application:
        ```bash
        python app.py
        ```

5.  Access the Chatbot:
    * Once the server starts,  can see a message like `* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`.
    * Open your web browser and go to `http://127.0.0.1:5000/`. This will display the `login.html` page.
    * Click on the "Go to Chat Assistant" link (or directly go to `http://127.0.0.1:5000/index`) to access the chatbot.