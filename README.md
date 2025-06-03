# Personalized Health Coach

This is the repository for our final project for the subject Intelligent Systems.<br>

The **Personalized-Health-Coach** is a modern Flask web application that leverages Google Gemini AI to deliver tailored lifestyle, diet, and exercise plans. Designed for ease of use and accessibility, this project empowers users to achieve their health goals with AI-driven recommendations, all presented in a clean, responsive interface.

---

## 🚀 Overview

Personalized Health Coach enables users to input their age, weight, height, and health goals, and optionally upload an image. The application then generates a comprehensive, personalized plan including:

- **Dietary advice**
- **Workout routines**
- **Supplement recommendations**

All results are delivered instantly and organized for clarity.

---

## ✨ Features

- **Intuitive Web Form:** Simple, user-friendly interface for entering personal data and goals.
- **AI-Powered Recommendations:** Utilizes Google Gemini AI for generating personalized plans.
- **Diet, Exercise, and Supplement Plans:** Clear, actionable advice in each category.
- **Image Upload Support:** Users can upload an image for a more personalized experience.
- **Responsive Design:** Built with Tailwind CSS for seamless use on desktop and mobile.
- **Instant Results:** Plans are generated and displayed immediately after form submission.
- **Secure File Handling:** Uploaded images are safely stored in a dedicated folder.

---

## 🛠️ Tech Stack

- **Backend:** Python 3.8+, Flask, google-generativeai, python-dotenv
- **Frontend:** HTML5, Tailwind CSS (via CDN), Jinja2 templates
- **AI Integration:** Google Gemini API

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/Personalized-Health-Coach.git
   cd Personalized-Health-Coach
   ```
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add your Gemini API key: `GEMINI_API_KEY=your_api_key`
4. **Add logo images:**
   - Place your logo images in the `static` folder.
5. **Run the application:**
   ```sh
   python app.py
   ```
6. **Access the app:**
   - Open your browser and go to `http://localhost:5000`.

---

## 👥 Team Members

- Matthew Valencia - Project manager 
- John Paul Sapasap - Lead Developer 
- Margaux Oriana Gasis - Designer 
- Joven Carl Rex Biaca - Developer 
- Jed Andrew Del Rosario - Developer

#Video Demo
- Youtube Link : https://www.youtube.com/watch?v=-SDNLav393I
