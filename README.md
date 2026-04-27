📚 Teacher CrewAI  Multi-Agent AI Teaching Assistant (Local Qwen Model)
A fully local AI-powered teaching assistant built with CrewAI, Python, and Ollama.
This project uses a team of specialized AI agents to transform lesson notes into professional classroom materials such as lesson plans, quizzes, and teaching strategies.
It runs entirely on your machine using local language models like Qwen2.5 or Llama, with no API keys, no cloud dependency, and full privacy.
Perfect for:


Teachers


Tutors


Trainers


Homeschool educators


Students creating study material


Anyone exploring AI multi-agent systems



🚀 Features
✅ 100% Local AI
Runs offline using Ollama with models such as:


Qwen2.5 (recommended)


Llama 3


Other Ollama-supported models


✅ No API Keys Required
No OpenAI key, no subscriptions, no hidden costs.
✅ Multi-Agent Collaboration
Three expert AI agents work together:
AgentRole📘 Curriculum DesignerBuilds a professional lesson plan📝 Quiz CreatorGenerates quizzes with answer keys🎓 Pedagogy AdvisorGives expert teaching strategies
✅ Flexible Input Options
Choose how to provide lesson notes:


Paste notes directly into terminal


Load notes from .txt file


Use built-in example lessons


✅ Supports Any Subject
Use it for:


Mathematics


English


Science


Music


History


Languages


Business


Coding


University subjects


Corporate training



🧠 Tech Stack


Python 3.10 – 3.12


CrewAI 1.9.x


crewai-tools


Ollama


Qwen2.5 / Llama



📦 Installation
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/teacher-crewai-assistant.gitcd teacher-crewai-assistant

2️⃣ Create Virtual Environment
Windows
python -m venv venvvenv\Scripts\activate
macOS / Linux
python3 -m venv venvsource venv/bin/activate

3️⃣ Install Requirements
pip install -r requirements.txt

🤖 Install Ollama
Download Ollama:
👉 https://ollama.com/download

📥 Download Local Model
Recommended:
ollama pull qwen2.5
Alternative:
ollama pull llama3

▶️ Start Ollama
ollama serve

⚙️ Configure Model
Inside teacher_crew.py
LLM_MODEL = "ollama/qwen2.5:3b"
To see installed models:
ollama list

▶️ Run Project
python teacher_crew.py

💬 How It Works
When the program starts, choose:
1. Paste lesson notes directly2. Load notes from .txt file3. Use built-in example
Then enter:


Subject


Grade / Level


Notes content


The AI crew will begin working.

📄 What The Crew Generates
📘 1. Complete Lesson Plan
Includes:


Lesson title


Learning objectives


Materials needed


Class timeline


Activities


Summary


Homework ideas



📝 2. Student Quizzes
Creates two quiz types:
Formative Quiz
Short in-class assessment.
Summative Quiz
Longer final assessment with:


Multiple Choice


True / False


Fill in the Blank


Short Answer


Includes full answer keys.

🎓 3. Teaching Advice
Practical teaching guidance:


Common misconceptions


Best teaching methods


Differentiation strategies


Student engagement ideas


Mistakes to avoid


Real-time assessment ideas



📌 Example Use Cases
Mathematics
Input notes on:


Quadratic Equations


Algebra


Geometry


Calculus


English
Input notes on:


Poetry


Grammar


Writing Skills


Figurative Language


Science
Input notes on:


Biology


Chemistry


Physics


Music
Input notes on:


Rhythm


Chords


Theory


Instruments



📁 Project Structure
teacher-crewai-assistant/│── teacher_crew.py│── requirements.txt│── README.md│── teacher_output.txt

📝 Notes


Fully offline after model installation


No internet needed during use


Easy to customize agents


Great for educators and students


Supports all education levels



🔮 Future Enhancements
Planned upgrades:


PDF worksheet export


PowerPoint lesson slides


Gradio / Streamlit UI


Voice teaching assistant


Homework generator


Auto grading system


Multi-language support



🤝 Contributing
Contributions are welcome.


Fork repository


Create feature branch


Improve project


Submit pull request



💛 Author
Narjes
AI Enthusiast • SEO Analyst • Multi-Agent Systems Learner

⭐ Support
If this project helped you:
⭐ Star the repository
🔁 Share it
🚀 Build your own version

📜 License
MIT License
