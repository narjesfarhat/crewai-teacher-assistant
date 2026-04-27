# 📚 Teacher CrewAI — Multi-Agent AI Teaching Assistant (Local Qwen Model)

An intelligent multi-agent teaching assistant built with **CrewAI**, **Python**, and **Ollama** that helps educators turn raw notes into professional classroom materials.

This project runs **100% locally** using Ollama models like **Qwen2.5** or **Llama**, meaning no API keys, no cloud costs, and complete privacy.

Simply provide lesson notes (paste directly or load from a `.txt` file), and the AI crew will generate:

✅ Structured Lesson Plan  
✅ Student Quizzes with Answer Keys  
✅ Teaching Strategies & Pedagogical Advice

---

# 🚀 Features

## ✅ 100% Local AI

Runs entirely on your computer using:

- Qwen2.5 (recommended)
- Llama 3
- Any Ollama-supported model

## ✅ No API Keys Required

No OpenAI key. No subscriptions. No cloud dependency.

## ✅ Multi-Agent Collaboration

Three expert agents work together:

| Agent | Role |
|------|------|
| 📘 Curriculum Designer | Builds a structured lesson plan |
| 📝 Quiz Creator | Creates quizzes + answer keys |
| 🎓 Pedagogy Advisor | Gives teaching strategies and classroom tips |

## ✅ Supports Any Subject

Use it for:

- Mathematics
- English
- Science
- Music
- History
- Languages
- Business
- University Topics
- Training Programs

## ✅ Flexible Input Options

Choose how to provide notes:

1. Paste directly in terminal  
2. Load from `.txt` file  
3. Use built-in examples

---

# 🧠 Tech Stack

- Python 3.10 – 3.12
- CrewAI 1.9.x
- crewai-tools
- Ollama
- Qwen2.5 / Llama 3

---

# 📦 Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/teacher-crewai-assistant.git
cd teacher-crewai-assistant
2️⃣ Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Mac/Linux
python3 -m venv venv
source venv/bin/activate
3️⃣ Install Requirements
pip install -r requirements.txt
🤖 Install Ollama

Download from:

https://ollama.com/download

📥 Pull Model

Recommended:

ollama pull qwen2.5

Or:

ollama pull llama3
▶️ Start Ollama
ollama serve
⚙️ Configure Model

Inside teacher_crew.py

LLM_MODEL = "ollama/qwen2.5:3b"

Use exact installed model name:

ollama list
▶️ Run Project
python teacher_crew.py
💬 Input Options

When starting, choose:

1. Paste notes directly
2. Load from txt file
3. Use built-in example
📌 Example Use Cases
Math

Input notes about:

Quadratic Equations
Algebra
Geometry
Calculus

Output:

Lesson Plan
Practice Quiz
Teaching Methods
English

Input notes about:

Poetry
Grammar
Figurative Language
Writing Skills
Music

Input notes about:

Chords
Rhythm
Music Theory
Instruments
📄 Example Output

The crew generates:

📘 Lesson Plan
Objectives
Materials
Timeline
Activities
Homework
📝 Quizzes
Multiple Choice
True/False
Fill in the Blank
Short Answer
🎓 Teaching Advice
Common misconceptions
Engagement tips
Differentiation ideas
Teaching mistakes to avoid
Formative assessment methods
📁 Project Structure
teacher-crewai-assistant/
│── teacher_crew.py
│── requirements.txt
│── README.md
│── teacher_output.txt
📝 Notes
Runs fully offline
No internet needed after model install
Great for teachers and tutors
Easy to customize
Supports all education levels
🔮 Future Enhancements
PDF worksheet export
PowerPoint lesson slides
Web UI with Gradio
Voice teaching assistant
Student report cards
Auto homework generator
Multi-language support
🤝 Contributing

Pull requests are welcome.

Fork project
Create branch
Improve features
Submit PR
💛 Author

Built by Narjes
AI Enthusiast • SEO Analyst • Multi-Agent Systems Learner

⭐ Support

If you like this project:

⭐ Star the repository
🔁 Share it
🚀 Build your own version

📜 License

MIT License
