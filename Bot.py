from docx import Document

# Step 1: Load the Word document
def load_knowledge_base(knowledge_base):
    doc = Document(knowledge_base)
    qa_pairs = {}
    question = None

    for para in doc.paragraphs:
        text = para.text.strip()
        if text.startswith("Q:"):
            question = text[2:].strip().lower()
        elif text.startswith("A:") and question:
            answer = text[2:].strip()
            qa_pairs[question] = answer
            question = None
    return qa_pairs

# Step 2: Simple chatbot logic
def chatbot(qa_data):
    print("ChatBot: Hello! Ask me something. Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            print("ChatBot: Goodbye!")
            break
        found = False
        for question, answer in qa_data.items():
            if user_input in question:
                print("ChatBot:", answer)
                found = True
                break
        if not found:
            print("ChatBot: Sorry, I don't have an answer for that.")

# Step 3: Run the bot
kb_file = "knowledge_base.docx"
qa_data = load_knowledge_base(kb_file)
chatbot(qa_data)
