# PYBOT-APP Documentation 🤖

## Introduction

Welcome to **PYBOT**!  An advanced Python-based conversational AI chatbot designed to assist you in navigating and extracting insights from PDF documents using cutting-edge Natural Language Processing (NLP) techniques. This application is built with Streamlit and leverages the power of **Retrieval-Augmented Generation (RAG)** to provide accurate, contextually relevant, and insightful answers to your queries.

https://github.com/user-attachments/assets/02ba1f8d-8c80-4a18-8f15-d00b4679b091


## Table of Contents 📑

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Technical Overview](#technical-overview)
- [Concept of RAG](#concept-of-rag)
- [Customization](#customization)
- [Lightning AI Integration](#lightning-ai-integration)
- [License](#license)

## Features

- **PDF Processing**: Seamlessly extract and analyze text from PDF documents. 
- **Text Chunking**: Break down large texts into manageable chunks for efficient processing. 
- **Vectorized Search**: Utilize FAISS for fast and accurate retrieval of text segments. 
- **Conversational Interface**: Engage in a dynamic Q&A session, powered by OpenAI or Hugging Face models. 
- **Memory Management**: Maintains conversation context for coherent multi-turn interactions. 
- **Customizable NLP Models**: Easily switch between different language models for varied use cases. 
- **Python Development Focus**: Pre-trained on Python development documents, making it ideal for assisting with Python code-related queries. 

## Prerequisites

Before running this application, ensure that you have the following installed:

- Python 3.7 or higher 🐍
- pip (Python package installer) 
- Virtual environment tools (optional but recommended) 🛡

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/3pacc/NTT-PYBOT.git
   cd NTT-PYBOT
   ```

2. **Set Up a Virtual Environment (optional but recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Required Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory of the project.
   - Add your OpenAI API key and any other required environment variables:
     ```
     OPENAI_API_KEY=your-openai-api-key
     ```

5. **Prepare Your PDF Documents**:
   - Place your PDF files in the `ressources` folder. 📂

## Usage

1. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

2. **Interact with PYBOT**:
   - Use the web interface to upload PDF documents and ask questions. 
   - Navigate through different sections using the sidebar. 

## File Structure

```plaintext
NTT-PYBOT/
├── ressources/           # Folder containing PDF files to be processed 📂
├── img/                  # Image assets for the Streamlit interface 🖼️
├── app.py                # Main application code 📜
├── requirements.txt      # Python dependencies 📝
├── .env                  # Example environment variables ⚙️
├── README.md             # Project documentation 📄
└── htmlTemplates.py      # HTML/CSS templates for chat UI 🎨
```

## Technical Overview 

### Core Components

- **Streamlit**: Provides the interactive web interface for the chatbot. 
- **Langchain**: Manages text processing, vector embeddings, and language model interactions.
- **FAISS**: Enables fast and efficient similarity search on the text chunks. 
- **PyPDF2**: Handles PDF file reading and text extraction. 

### Workflow

1. **PDF Text Extraction**: Extracts text from PDF files using PyPDF2. 
2. **Text Chunking**: Breaks the text into smaller chunks for better retrieval and processing. 
3. **Vectorization**: Converts chunks into embeddings using Hugging Face models. 
4. **RAG-Based Interaction**: Retrieves relevant text chunks and generates responses using the selected NLP model. 
5. **Conversation Handling**: Maintains context across multiple user queries with memory management. 

## Concept of RAG

**Retrieval-Augmented Generation (RAG)** combines two powerful NLP techniques:

1. **Retrieval**: Searches for the most relevant documents or text segments related to a query. 🔍
2. **Generation**: Uses language models to generate coherent and contextually accurate responses based on the retrieved information. 📝

This hybrid approach ensures that the chatbot can provide precise, well-informed answers even when handling complex queries. 

## Customization

- **Switching NLP Models**: Modify the `get_conversation_chain` function to use different Hugging Face models as per your requirements. 🔄
- **Text Chunking Parameters**: Adjust the `chunk_size` and `chunk_overlap` parameters in the `get_text_chunks` function to fine-tune the text segmentation. 
- **UI Customization**: Update the `htmlTemplates.py` file to change the look and feel of the chatbot interface. 

## Lightning AI Integration

If you do not have the necessary local resources, such as powerful GPUs or are concerned about the compatibility of various modules, you can deploy this application on **Lightning AI**. Lightning AI provides a robust platform that allows you to run and scale AI applications easily, using cloud resources to bypass local hardware limitations. ☁️

### Benefits of Using Lightning AI

- **Access to GPUs**: Leverage high-performance GPUs in the cloud to accelerate your application, especially useful for NLP tasks that require substantial computational power. 
- **Module Compatibility**: Ensure that all necessary dependencies and modules are compatible and up to date, reducing the complexity of local environment setup. 
- **Scalability**: Easily scale your application to handle larger workloads without worrying about local resource constraints. 
- **Ease of Deployment**: Deploy your application with minimal configuration, making it accessible from anywhere. 

### How to Deploy on Lightning AI

1. **Sign Up for Lightning AI**: Create an account at [Lightning AI](https://lightning.ai/). 
2. **Create a New Project**: Start a new project and link it to your GitHub repository containing the PYBOT application. 
3. **Configure Your Environment**: Set up the necessary environment variables and dependencies as you would locally. Lightning AI ensures that the modules are compatible and optimized for performance. 
4. **Deploy**: Launch the application on Lightning AI and access it via the provided URL. 

Using Lightning AI is particularly advantageous if you're working with limited local resources but still want to leverage the full capabilities of the PYBOT application. 💪

## License

This project is licensed under the MIT License. 📄
