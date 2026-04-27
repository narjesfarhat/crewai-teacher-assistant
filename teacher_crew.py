"""
Exercise 2: Teacher Assistant CrewAI Crew
==========================================
Reads lesson notes (from a .txt file OR typed directly in the prompt).
Agents:
  1. Curriculum Designer  – generates a structured lesson plan
  2. Quiz Creator         – generates quizzes with answer keys
  3. Pedagogy Advisor     – gives the teacher tips on HOW to teach it

Run:
  python teacher_crew.py
  → You'll be asked to either paste notes OR provide a .txt file path.

Example notes are included at the bottom of this file for testing.
"""

import os
import sys
from pathlib import Path
from crewai import Agent, Task, Crew, Process

# ─── LLM Config ───────────────────────────────────────────────────────────────

LLM_MODEL = "ollama/qwen2.5:3b"     # Change to your preferred model (e.g., "gpt-4", "ollama/qwen2.5:3b", etc.)

# ─── AGENTS ───────────────────────────────────────────────────────────────────

def create_agents():
    curriculum_designer = Agent(
        role="Curriculum Designer",
        goal=(
            "Transform raw lesson notes into a clear, structured, and engaging lesson plan "
            "suitable for the target audience."
        ),
        backstory=(
            "You are a senior curriculum designer with 20 years of experience building "
            "educational programs from K-12 to university level. You specialize in breaking "
            "complex topics into digestible, logically ordered lessons. You know how to set "
            "clear learning objectives and scaffold knowledge effectively."
        ),
        llm=LLM_MODEL,
        llm_config={"base_url": "http://localhost:11434"},
        verbose=True,
        allow_delegation=False,
    )

    quiz_creator = Agent(
        role="Assessment & Quiz Specialist",
        goal=(
            "Design comprehensive, fair, and pedagogically sound quizzes that test "
            "understanding at multiple cognitive levels."
        ),
        backstory=(
            "You are an expert in educational assessment with a PhD in psychometrics. "
            "You design quizzes that go beyond memorization — testing comprehension, "
            "application, and critical thinking. You always provide answer keys with "
            "explanations so teachers can use them effectively. You create a mix of "
            "multiple choice, true/false, fill-in-the-blank, and open-ended questions."
        ),
        llm=LLM_MODEL,
        llm_config={"base_url": "http://localhost:11434"},
        verbose=True,
        allow_delegation=False,
    )

    pedagogy_advisor = Agent(
        role="Pedagogy & Teaching Strategy Advisor",
        goal=(
            "Give the teacher practical, evidence-based advice on HOW to teach "
            "this specific topic most effectively."
        ),
        backstory=(
            "You are a master teacher trainer and educational psychologist who has trained "
            "over 5,000 teachers worldwide. You are fluent in modern pedagogy including "
            "Bloom's Taxonomy, spaced repetition, active learning, differentiated instruction, "
            "project-based learning, and formative assessment. Your advice is always concrete, "
            "practical, and tied to the specific content being taught."
        ),
        llm=LLM_MODEL,
        llm_config={"base_url": "http://localhost:11434"},
        verbose=True,
        allow_delegation=False,
    )

    return curriculum_designer, quiz_creator, pedagogy_advisor


# ─── TASKS ────────────────────────────────────────────────────────────────────

def create_tasks(agents, notes: str, subject: str, level: str):
    curriculum_designer, quiz_creator, pedagogy_advisor = agents

    task_lesson_plan = Task(
        description=(
            f"You have received the following lesson notes for a {level}-level {subject} class:\n\n"
            f"---\n{notes}\n---\n\n"
            "Using these notes, create a complete, structured lesson plan. Include:\n"
            "1. Lesson Title\n"
            "2. Target Audience & Level\n"
            "3. Estimated Duration\n"
            "4. Learning Objectives (3–5 clear, measurable objectives using Bloom's verbs)\n"
            "5. Materials Needed\n"
            "6. Lesson Structure:\n"
            "   - Introduction / Hook (5–10 min)\n"
            "   - Main Content sections with timing\n"
            "   - Activities / Practice\n"
            "   - Summary & Wrap-up\n"
            "7. Homework or Further Reading suggestions"
        ),
        expected_output=(
            "A complete, teacher-ready lesson plan formatted clearly with all 7 sections. "
            "It should be detailed enough that any teacher could pick it up and use it immediately."
        ),
        agent=curriculum_designer,
    )

    task_quizzes = Task(
        description=(
            f"Based on the following {subject} lesson notes for {level} students:\n\n"
            f"---\n{notes}\n---\n\n"
            "Create TWO separate quizzes:\n\n"
            "QUIZ 1 — Formative Quiz (during the lesson, 5 questions):\n"
            "  - Mix of multiple choice and true/false\n"
            "  - Tests basic understanding and recall\n"
            "  - Include the answer key\n\n"
            "QUIZ 2 — Summative Quiz (end of lesson / homework, 10 questions):\n"
            "  - Include: 4 multiple choice, 2 true/false, 2 fill-in-the-blank, 2 short answer\n"
            "  - Tests deeper understanding and application\n"
            "  - Include the full answer key with brief explanations for each answer"
        ),
        expected_output=(
            "Two clearly labeled quizzes (Formative and Summative) with all questions, "
            "answer choices where applicable, and a complete answer key with explanations."
        ),
        agent=quiz_creator,
        context=[task_lesson_plan],  # Quiz creator sees the lesson plan too
    )

    task_advice = Task(
        description=(
            f"A teacher is about to teach the following {subject} content to {level} students:\n\n"
            f"---\n{notes}\n---\n\n"
            "Provide a comprehensive teaching strategy guide. Include:\n"
            "1. Common Misconceptions — what do students typically get wrong about this topic? "
            "   How should the teacher address them proactively?\n"
            "2. Teaching Techniques — what specific methods work best for THIS topic? "
            "   (e.g., visual aids, manipulatives, think-pair-share, worked examples, etc.)\n"
            "3. Differentiation — how to adjust for students who are struggling vs. advanced?\n"
            "4. Engagement Tips — how to make this topic interesting and relevant to students' lives?\n"
            "5. Common Mistakes to Avoid — what teaching pitfalls should the teacher watch out for?\n"
            "6. Formative Assessment Ideas — quick checks the teacher can use during the lesson "
            "   (beyond the quiz) to gauge understanding in real-time."
        ),
        expected_output=(
            "A practical, detailed teaching advice guide covering all 6 areas. "
            "Advice must be specific to the content, not generic. "
            "Use bullet points and clear headers for easy reading."
        ),
        agent=pedagogy_advisor,
        context=[task_lesson_plan],  # Advisor sees the lesson plan
    )

    return [task_lesson_plan, task_quizzes, task_advice]


# ─── CREW ─────────────────────────────────────────────────────────────────────

def run_teacher_crew(notes: str, subject: str, level: str):
    print("\n" + "="*60)
    print("📚  TEACHER ASSISTANT CREW — Starting...")
    print("="*60 + "\n")

    agents = create_agents()
    tasks = create_tasks(agents, notes, subject, level)

    crew = Crew(
        agents=list(agents),
        tasks=tasks,
        process=Process.sequential,  # Lesson Plan → Quiz → Teaching Advice
        verbose=True,
    )

    result = crew.kickoff()
    return result


# ─── NOTES LOADING ────────────────────────────────────────────────────────────

EXAMPLE_NOTES = {
    "math": """
Topic: Introduction to Quadratic Equations
Level: High School (Grade 10)

Key concepts:
- A quadratic equation has the form ax² + bx + c = 0, where a ≠ 0
- The degree of a quadratic is 2 (highest power of x is 2)
- Solutions are called "roots" or "zeros" of the equation

Methods to solve quadratic equations:
1. Factoring: Rewrite ax² + bx + c as (px + q)(rx + s) = 0, then solve each factor = 0
   Example: x² - 5x + 6 = 0 → (x-2)(x-3) = 0 → x = 2 or x = 3

2. Quadratic Formula: x = (-b ± √(b²-4ac)) / 2a
   Works for ALL quadratic equations, even when factoring is difficult.
   Example: 2x² + 3x - 2 = 0 → a=2, b=3, c=-2 → x = (-3 ± √(9+16)) / 4 = (-3 ± 5) / 4
   → x = 0.5 or x = -2

3. Completing the Square: Rewrite equation so left side is a perfect square trinomial
   Example: x² + 6x + 5 = 0 → x² + 6x + 9 = 4 → (x+3)² = 4 → x+3 = ±2 → x = -1 or x = -5

The Discriminant: D = b² - 4ac
- D > 0: two distinct real roots
- D = 0: one repeated real root
- D < 0: no real roots (complex roots)

Real-world applications:
- Projectile motion (height of a ball thrown in the air)
- Area problems (finding dimensions of a rectangle given its area)
- Profit/revenue optimization in business
""",

    "english": """
Topic: Figurative Language in Poetry
Level: Middle School (Grade 7)

Key Types of Figurative Language:
1. Simile: comparing two things using "like" or "as"
   Example: "Her voice was like music"
   
2. Metaphor: direct comparison WITHOUT "like" or "as"
   Example: "Life is a rollercoaster"
   
3. Personification: giving human traits to non-human things
   Example: "The wind whispered through the trees"
   
4. Hyperbole: extreme exaggeration for effect
   Example: "I've told you a million times!"
   
5. Onomatopoeia: words that sound like what they describe
   Example: "buzz," "crash," "sizzle"
   
6. Alliteration: repetition of the same consonant sound at the start of words
   Example: "Peter Piper picked a peck of pickled peppers"

Why do poets use figurative language?
- To create vivid images in the reader's mind
- To evoke emotions more powerfully than literal language
- To make abstract ideas concrete
- To add rhythm and musicality

Exercise: Read Robert Frost's "The Road Not Taken" and identify examples of metaphor.
The entire poem is an extended metaphor — the road represents life choices.
""",
}


def load_notes() -> tuple[str, str, str]:
    """Load notes from user input or file."""
    print("\n📝 How would you like to provide the lesson notes?")
    print("  1. Type/paste them directly")
    print("  2. Load from a .txt file")
    print("  3. Use a built-in example (math or english)")
    choice = input("\nEnter 1, 2, or 3: ").strip()

    if choice == "2":
        filepath = input("Enter the path to your .txt file: ").strip()
        try:
            notes = Path(filepath).read_text(encoding="utf-8")
            print(f"✅ Loaded {len(notes)} characters from {filepath}")
        except FileNotFoundError:
            print(f"❌ File not found: {filepath}. Using math example instead.")
            notes = EXAMPLE_NOTES["math"]
        subject = input("What subject is this? (e.g. Math, English, Science): ").strip() or "Math"
        level = input("What level? (e.g. Grade 7, High School, University): ").strip() or "High School"

    elif choice == "3":
        example = input("Which example? (math / english): ").strip().lower()
        notes = EXAMPLE_NOTES.get(example, EXAMPLE_NOTES["math"])
        subject = "Mathematics" if example == "math" else "English / Poetry"
        level = "High School (Grade 10)" if example == "math" else "Middle School (Grade 7)"
        print(f"✅ Using built-in {example} example notes.")

    else:
        print("Paste your notes below. When done, type END on a new line and press Enter:")
        lines = []
        while True:
            line = input()
            if line.strip().upper() == "END":
                break
            lines.append(line)
        notes = "\n".join(lines)
        subject = input("What subject is this? (e.g. Math, English, Music): ").strip() or "General"
        level = input("What level? (e.g. Grade 5, High School, Adult): ").strip() or "High School"

    return notes, subject, level


# ─── MAIN ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("\n📚 Welcome to the AI Teacher Assistant!")
    print("This crew will generate a lesson plan, quizzes, and teaching advice.\n")

    notes, subject, level = load_notes()

    if not notes.strip():
        print("❌ No notes provided. Exiting.")
        sys.exit(1)

    result = run_teacher_crew(notes, subject, level)

    # Save output to a file
    output_path = Path("teacher_output.txt")
    output_path.write_text(str(result), encoding="utf-8")

    print("\n" + "="*60)
    print("✅  TEACHER ASSISTANT COMPLETE")
    print(f"📄  Full output saved to: {output_path.absolute()}")
    print("="*60)
    print(result)
