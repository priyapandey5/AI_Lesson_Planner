# 📚 Lesson Plan Generator 

## 🚀 Overview

The **Lesson Plan Generator** is a Streamlit-based web application that helps educators create structured and comprehensive lesson plans using Google's **Gemini AI model**.

This tool simplifies lesson planning by automatically generating detailed plans based on user inputs like subject, grade, and duration.

---

## ✨ Features

* Interactive web interface for entering lesson details
* Generates structured lesson plans including:

  * Learning Outcomes
  * Learning Experiences
  * Assessment
  * Reflection
* Powered by **Google Gemini AI** for intelligent content generation
* Option to download generated lesson plans in JSON format
* Fast and lightweight deployment-ready app

---

## 🧰 Prerequisites

Before you begin, ensure you have:

* Python **3.8 or higher**
* A **Google Gemini API Key** (from Google AI Studio)

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/priyapandey5/AI_Lesson_Planner.git
cd AI_Lesson_Planner
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setting Up the API Key

You need to set your **Gemini API Key**.

### ✅ Option 1: Environment Variable (Recommended)

#### On Windows:

```bash
set GEMINI_API_KEY=your-api-key-here
```

#### On macOS/Linux:

```bash
export GEMINI_API_KEY=your-api-key-here
```

---

### ✅ Option 2: `.env` File

Create a `.env` file in your project root:

```env
GEMINI_API_KEY=your-api-key-here
```

---

## ▶️ Usage

Run the Streamlit app:

```bash
streamlit run app.py
```

Open your browser and go to:

```
http://localhost:8501
```

---

## 📝 How to Use

Fill in the form fields:

* Lesson Title
* Subject
* Grade
* Duration
* Key Vocabulary
* Supporting Materials & Resources

👉 Click **"Generate Lesson Plan"**

---

## 📊 Output

The app will generate a structured lesson plan including:

* **Learning Outcomes**

  * Knowledge
  * Skills
  * Understanding

* **Learning Experiences**

  * Prepare
  * Plan
  * Investigate
  * Apply
  * Connect
  * Evaluate

* **Assessment**

* **Reflection**

---

## 💾 Download Option

You can download the generated lesson plan as a **JSON file** for future use.

---

## 🛠️ Customization

You can modify the AI behavior by editing:

```bash
app.py
```

* Change prompt structure
* Adjust output format
* Improve response quality

---

## 🐞 Troubleshooting

### ❌ API Errors

* Check if your `GEMINI_API_KEY` is correct
* Ensure your API quota is available

### ❌ App Not Running

* Verify all dependencies are installed
* Check terminal logs for errors

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 🙏 Acknowledgments

* Google Gemini AI for content generation
* Streamlit for the web app framework

---

## 🌍 Deployment

This app can be easily deployed on platforms like **Render** using:

```bash
streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

---

## 🎉 Final Note

This project is beginner-friendly and perfect for:

* Students
* Educators
* Developers learning AI integration

---

💡 *Build, Learn, and Deploy with AI!*




- OpenAI for providing the GPT model
- Streamlit for the web application framework
