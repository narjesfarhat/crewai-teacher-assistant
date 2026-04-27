📚 Teacher CrewAI — Multi-Agent AI Teaching Assistant
A professional AI-powered teaching assistant built with CrewAI, Python, and Ollama.
This project uses multiple specialized AI agents to transform raw lesson notes into complete classroom-ready teaching materials.
Provide your notes manually or from a .txt file, and the system will automatically generate:


📘 Structured lesson plans


📝 Student quizzes with answer keys


🎓 Teaching strategies and pedagogy guidance


Built to run 100% locally using Ollama models such as Qwen2.5 or Llama, with no API keys, no cloud dependency, and full privacy.

🚀 Why This Project?
Teachers spend hours preparing lessons, assessments, and teaching strategies.
This project automates that workflow using coordinated AI agents, helping educators save time while improving lesson quality.
Ideal for:


Teachers


Tutors


Trainers


Homeschool educators


Students creating study resources


Developers learning multi-agent AI systems



✨ Key Features
✅ Multi-Agent AI Workflow
Three expert agents collaborate sequentially:
AgentResponsibility📘 Curriculum DesignerConverts notes into structured lesson plans📝 Quiz CreatorBuilds formative and summative assessments🎓 Pedagogy AdvisorRecommends teaching methods and engagement strategies

✅ Flexible Input Methods
Choose one of the following:


Paste lesson notes directly into terminal


Load lesson notes from a .txt file


Use built-in demo lessons



✅ Works Across Subjects
Supports virtually any topic:


Mathematics


English Literature


Science


History


Geography


Music


Languages


Business


Programming


University courses



✅ Runs Fully Local
Powered by Ollama.
Benefits:


No API fees


No rate limits


No external data sharing


Fast local inference


Full ownership of workflow



🧠 Tech Stack
TechnologyPurposePython 3.10+Core programming languageCrewAI 1.9.xMulti-agent orchestrationOllamaLocal LLM runtimeQwen2.5 / LlamaLanguage modelspathlib / CLIFile loading & user interaction

📦 Installation
1. Clone Repository
git clone https://github.com/YOUR_USERNAME/teacher-crewai-assistant.gitcd teacher-crewai-assistant

2. Create Virtual Environment
Windows
python -m venv venvvenv\Scripts\activate
macOS / Linux
python3 -m venv venvsource venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

🤖 Install Ollama
Download Ollama:
👉 https://ollama.com/download

📥 Download a Model
Recommended:
ollama pull qwen2.5
Alternative:
ollama pull llama3

▶️ Start Ollama
ollama serve

⚙️ Configure Model
Inside teacher_crew.py
LLM_MODEL = "ollama/qwen2.5:3b"
To list installed models:
ollama list

▶️ Run the Application
python teacher_crew.py

💬 User Workflow
When launched, choose:
1. Paste notes directly2. Load notes from .txt file3. Use built-in example
Then enter:


Subject


Grade / Education level


Lesson notes


The AI crew processes everything automatically.

📄 Output Generated
📘 Lesson Plan
Includes:


Lesson title


Learning objectives


Materials needed


Time breakdown


Activities


Summary


Homework suggestions



📝 Assessments
Formative Quiz
Short in-class check for understanding.
Summative Quiz
Comprehensive end-of-lesson quiz containing:


Multiple choice


True / False


Fill in the blank


Short answer


Includes answer keys and explanations.

🎓 Teaching Guidance
Includes:


Common student misconceptions


Best methods to teach the topic


Differentiation strategies


Classroom engagement ideas


Mistakes to avoid


Real-time assessment methods



📌 Example Use Cases
Mathematics


Algebra


Geometry


Quadratic Equations


Calculus


English


Poetry


Grammar


Essay Writing


Figurative Language


Science


Biology


Chemistry


Physics


Music


Rhythm


Theory


Instruments


Harmony



📁 Project Structure
teacher-crewai-assistant/│── teacher_crew.py│── requirements.txt│── README.md│── teacher_output.txt

🔮 Roadmap
Future improvements:


Web UI (Gradio / Streamlit)


PDF lesson exports


PowerPoint slide generation


Homework generator


Auto grading assistant


Voice teacher assistant


Multi-language support



🤝 Contributing
Contributions are welcome.
1. Fork repository2. Create feature branch3. Commit improvements4. Open pull request

💛 Author
Narjes
AI Enthusiast • SEO Analyst • Multi-Agent Systems Learner

⭐ Support
If you found this useful:


Star the repository ⭐


Share with educators


Build your own version



📜 License
Released under the MIT License.
