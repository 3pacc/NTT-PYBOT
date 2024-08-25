import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub
from sentence_transformers import SentenceTransformer


PDF_FOLDER_PATH = "ressources"

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    # Initialize embeddings model
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
    
    # Create the vectorstore from text chunks
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vectorstore):
    # Initialize the language model from Hugging Face
    llm = HuggingFaceHub(repo_id="google/gemma-7b-it", model_kwargs={"temperature": 0.7, "max_length": 2048 , "return_full_text":False})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def process_files(folder_path):
    pdf_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.pdf')]
    pdf_docs = [open(f, "rb") for f in pdf_files]
    raw_text = get_pdf_text(pdf_docs)
    text_chunks = get_text_chunks(raw_text)
    vectorstore = get_vectorstore(text_chunks)
    return vectorstore

def handle_userinput():
    user_question = st.session_state.user_question
    if user_question and st.session_state.conversation:
        response = st.session_state.conversation({'question': user_question})
        st.session_state.chat_history = response['chat_history']
        st.session_state.user_question = ""  # Clear the input field

def display_chat_history():
    if st.session_state.chat_history:
        for i, message in enumerate(reversed(st.session_state.chat_history)):
            if i % 2 != 0:
                st.write(user_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)
            else:
                st.write(bot_template.replace(
                    "{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with NTT-CHATBOT", page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None
    if "user_question" not in st.session_state:
        st.session_state.user_question = ""

    # Process files and initialize conversation chain
    if st.session_state.conversation is None:
        with st.spinner("Processing files and initializing..."):
            vectorstore = process_files(PDF_FOLDER_PATH)
            st.session_state.conversation = get_conversation_chain(vectorstore)
            st.success("Files processed and conversation initialized successfully.")

    st.header("Chat with NTT-CHATBOT 🤖")

    # Input field at the top
    st.text_input("Ask a question about your documents:", value=st.session_state.user_question, key="user_question", on_change=handle_userinput)

    # Display chat messages
    display_chat_history()

    with st.sidebar:
        st.image("img/ntt-data.png", caption="Chatbot trained on Python development")
        
        
        menu_options = [
            "Introduction",
            "Python Basics",
            "Advanced Python",
            "Python Libraries",
            "Troubleshooting",
            "Best Practices",
            "About Us",
            "FAQ",
            "Location",
            "Contact Support"
        ]
        
        selected_option = st.selectbox("Navigate to", menu_options)

        if selected_option == "Introduction":
            st.subheader("Introduction 🗣️")
            st.write("Welcome to the **NTT-CHATBOT**! I am here to assist you with everything related to **Python development**. Whether you're just starting out or looking to refine your skills, I'm here to help!")

        elif selected_option == "About Us":
            st.subheader("About Us 🌟")
            st.write("We are a team of passionate developers dedicated to helping you master **Python**. Our mission is to provide high-quality resources and support for all your Python development needs.")

        elif selected_option == "Python Basics":
            st.subheader("Python Basics 📚")
            st.write("Get started with the **fundamentals of Python**. Learn about variables, data types, loops, and functions. Perfect for beginners looking to build a solid foundation.")

        elif selected_option == "Advanced Python":
            st.subheader("Advanced Python 🚀")
            st.write("Explore more **complex Python topics** such as decorators, context managers, and metaclasses. Ideal for developers looking to deepen their understanding and improve their coding skills.")

        elif selected_option == "Python Libraries":
            st.subheader("Python Libraries 📦")
            st.write("Discover essential Python libraries like NumPy, pandas, and TensorFlow. Learn how to leverage these tools to enhance your projects and streamline your workflow.")

        elif selected_option == "Troubleshooting":
            st.subheader("Troubleshooting 🔧")
            st.write("Encountering issues with your Python code? Find solutions to common problems and bugs, and get tips on how to debug and resolve them effectively.")

        elif selected_option == "Best Practices":
            st.subheader("Best Practices 🏆")
            st.write("Adopt best practices for writing clean, efficient, and maintainable Python code. Learn about coding standards, design patterns, and strategies to enhance your development process.")

        elif selected_option == "FAQ":
            st.subheader("FAQ ❓")
            st.write("Check out our frequently asked questions to find quick answers to common queries about Python development and how to use the NTT-CHATBOT.")

        elif selected_option == "Location":
            st.subheader("Location 🌍")
            st.write("Retrouvez-nous dans nos bureaux pour une assistance en personne ou pour toute autre demande :")
            st.write("📍 **Adresse:** 123 Rue de Python, VilleTech, 75001, Paris, France")
            st.write("🕒 **Heures d'ouverture:** Lundi - Vendredi : 9h00 - 18h00")
            st.write("📞 **Téléphone:** +33 1 23 45 67 89")

        elif selected_option == "Contact Support":
            st.subheader("Contact Support 📞")
            st.write("Need further assistance? Reach out to our support team for help with any issues or questions you may have. We're here to support you! Feel free to reach out to our team.       \n  "      
                 "   📧 **Email:** antribak@emeal.nttdata.com    \n    "
                 "🐦 **Follow us on LinkedIn:** [Tribak Anas](https://www.linkedin.com/in/anas-tribak-331470242/)     |   [Zineb Doukkali](https://www.linkedin.com/in/anas-tribak-331470242/)    \n"
                 "🔗 **GitHub:** [3pacc](https://github.com/3pacc)")



    st.write("""
        <script>
            var container = window.parent.document.querySelector('section.main');
            if (container) {
                container.scrollTo(0, container.scrollHeight);
            }
        </script>
    """, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
