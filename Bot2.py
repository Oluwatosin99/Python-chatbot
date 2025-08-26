from docx import Document

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

def chatbot(qa_data):
    print("ChatBot: Hello! Ask me something. Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip().lower()
        if user_input == "exit":
            print("ChatBot: Goodbye!")
            break
        found = False
        for question, answer in qa_data.items():
            # Split question into keywords and check if any keyword is in user input
            keywords = question.split()
            if any(keyword in user_input for keyword in keywords):
                print("ChatBot:", answer)
                found = True
                break
        if not found:
            print("ChatBot: Sorry, I don't have an answer for that.")

kb_file = "knowledge_base.docx"
qa_data = load_knowledge_base(kb_file)
chatbot(qa_data)


#How it works:

# It loads Q&A pairs from a Word document.
# When you ask a question, it checks if any keyword from the stored questions appears in your input.
# If a match is found, it returns the answer. Otherwise, it says it doesn't know.