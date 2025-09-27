from fpdf import FPDF # type: ignore

# Define the weekly study plan content
title = "English Self-Study Plan (Beginner to Pro)"
intro = ("This is a weekly study plan designed to help you learn English on your own, "
         "from beginner to advanced level. Follow this guide daily to improve your grammar, "
         "speaking, listening, reading, and writing skills.")

daily_plan = [
    ("Monday", "Grammar + Listening", 
     "🧠 Khan Academy (Grammar)\n🎧 BBC Learning English (6-Minute English) — 1 hour"),
    ("Tuesday", "Vocabulary + Reading", 
     "📘 Duolingo (20 min)\n📚 LingQ or British Council stories — 1 to 1.5 hours"),
    ("Wednesday", "Speaking + Listening", 
     "🎤 EngVid video + Repeat aloud\n🎧 Shadow BBC clips — 1 hour"),
    ("Thursday", "Grammar + Writing", 
     "✍️ British Council (Grammar and Writing practice) — 1 hour"),
    ("Friday", "Free Learning (Your Choice)", 
     "🔁 YouTube (e.g., Speak English with Emma)\n📓 Review vocabulary — 1 hour"),
    ("Saturday", "Real English Practice", 
     "📰 Read news on LingQ or BBC Learning\n📝 Write a summary — 1 to 1.5 hours"),
    ("Sunday", "Review + Test Yourself", 
     "🧪 Take quizzes (British Council, EngVid)\n🗣️ Record yourself speaking or write a journal — 1 hour")
]

tools = [
    "📒 Notebook or Google Docs – for writing and notes",
    "🃏 Anki or Quizlet – flashcards for vocabulary",
    "🎙️ Voice Recorder App – to practice and check your pronunciation",
    "📝 Grammarly – helps correct grammar and improve writing"
]

goals = [
    "Week 1–2: Learn basic grammar (present tense, articles), 300 new words, start speaking daily",
    "Week 3–4: Practice simple conversations, learn past tense, read short articles, write short stories",
    "Month 2: Intermediate grammar (future tense, modals), podcasts, writing prompts",
    "Month 3: Advanced grammar, participate in debates, write essays, fluent speaking on topics"
]

# Create PDF
pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, title, ln=True, align='C')

pdf.set_font("Arial", '', 12)
pdf.ln(10)
pdf.multi_cell(0, 10, intro)

pdf.ln(5)
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "📅 Weekly Study Schedule", ln=True)

pdf.set_font("Arial", '', 12)
for day, focus, detail in daily_plan:
    pdf.ln(2)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, f"{day} – {focus}", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 8, detail)

pdf.ln(5)
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "🧰 Recommended Tools", ln=True)
pdf.set_font("Arial", '', 12)
for tool in tools:
    pdf.multi_cell(0, 8, f"- {tool}")

pdf.ln(5)
pdf.set_font("Arial", 'B', 14)
pdf.cell(0, 10, "🎯 Monthly Goals Example", ln=True)
pdf.set_font("Arial", '', 12)
for goal in goals:
    pdf.multi_cell(0, 8, f"- {goal}")

# Save the PDF
pdf.output("English_Self_Study_Plan.pdf")
