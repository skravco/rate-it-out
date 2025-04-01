
# Rate It Out

## Overview

The **Feedback System** is a Flask-based web application designed to collect and manage feedback on my various projects. It allows users to submit ratings and comments, stores the feedback in a database, and notifies via email using Mailtrap integration.

This project showcases a clean, scalable, and secure web application, displays both front-end and back-end development capabilities. Additionally, it highlights proficiency in modern deployment techniques, environment management, and cloud hosting using **Render.com**.

---

## Features

- **User Feedback Submission**: Users can provide feedback on different projects by submitting their name, project, rating, and additional comments.
- **Data Persistence**: Feedback data is stored in a **SQLite** database, ensuring long-term data retention.
- **Email Notifications**: Once feedback is submitted, a notification email is sent to relevant stakeholders (using **Mailtrap** integration for testing purposes).
- **Duplicate Feedback Prevention**: Prevents duplicate feedback from the same customer, ensuring the integrity of the feedback data.
- **Responsive UI**: The app features a clean and responsive design that works across various devices and screen sizes.
- **Automated Deployment**: The app is hosted on **Render.com**, ensuring seamless and automatic deployment with each update from the GitHub repository.

---

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Email Service**: Mailtrap (SMTP for email notifications)
- **Environment Management**: Python-dotenv (for local development)
- **Deployment**: Render.com (Cloud hosting platform)

---

## Installation & Setup

To run this project locally, follow the instructions below:

### 1. Clone the repository:
```bash
git clone https://github.com/skravco/rate-it-out.git
cd rate-it-out
```

### 2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables:
For local development, create a `.env` file in the root of the project and include the following variables:

```env
SMTP_SERVER=your-smtp-server
SMTP_PORT=your-smtp-port
MAILTRAP_USERNAME=your-mailtrap-username
MAILTRAP_PASSWORD=your-mailtrap-password
SENDER_EMAIL=your-email@example.com
RECEIVER_EMAIL=receiver-email@example.com
```

### 5. Run the Flask application:
```bash
python app.py
```

### 6. Visit `http://127.0.0.1:5000` in your browser to view the app.

---

## Deployment to Render.com

This application is deployed on **Render.com**, ensuring automated scaling and continuous integration with every commit pushed to GitHub.

For production, follow these steps:

1. Create a **Render.com** account.
2. Link the project repository to Render and configure the deployment settings (Python 3 environment).
3. Set the environment variables directly in the Render dashboard (no need for `.env` file in production).
4. Once deployed, Render will provide a public URL for your live application.

---

## Future Enhancements

- **Feedback Analytics**: Add a dashboard to visualize and analyze customer feedback (e.g., average ratings, most common comments).
- **Database Migration**: Migrate from SQLite to a more scalable database solution, like PostgreSQL, for handling larger datasets.
- **Enhanced Email Notifications**: Integrate a more robust email service, such as SendGrid, for production-grade email delivery.

---

## **Contact & Links**
 **Portfolio**: [skravco.github.io](https://skravco.github.io/)
 **LinkedIn**: [skravco](https://www.linkedin.com/in/skravco)

---

### **If you find this project insightful, please give it a star on GitHub!**

