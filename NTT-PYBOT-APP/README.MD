# PYBOT Chatbot Documentation

## Introduction

Welcome to **PYBOT**, an advanced chatbot application designed to assist you in navigating and extracting insights from PDF documents using state-of-the-art Natural Language Processing (NLP) techniques. This application is built with Streamlit and leverages the power of **Retrieval-Augmented Generation (RAG)** to provide accurate and contextually relevant answers to your questions.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Technical Overview](#technical-overview)
- [Concept of RAG](#concept-of-rag)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Features

- **PDF Processing**: Seamlessly extract and analyze text from PDF documents.
- **Text Chunking**: Break down large texts into manageable chunks for efficient processing.
- **Vectorized Search**: Utilize FAISS for fast and accurate retrieval of text segments.
- **Conversational Interface**: Engage in a dynamic Q&A session, powered by OpenAI or Hugging Face models.
- **Memory Management**: Maintains conversation context for coherent multi-turn interactions.
- **Customizable NLP Models**: Easily switch between different language models for varied use cases.

## Prerequisites

Before running this application, ensure that you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)
- Virtual environment tools (optional but recommended)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/pybot-chatbot.git
   cd pybot-chatbot
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
   - Place your PDF files in the `ressources` folder.

## Usage

1. **Run the Application**:
   ```bash
   streamlit run main.py
   ```

2. **Interact with PYBOT**:
   - Use the web interface to upload PDF documents and ask questions.
   - Navigate through different sections using the sidebar.

## File Structure

```plaintext
pybot-chatbot/
├── ressources/           # Folder containing PDF files to be processed
├── img/                  # Image assets for the Streamlit interface
├── main.py               # Main application code
├── requirements.txt      # Python dependencies
├── .env.example          # Example environment variables
├── README.md             # Project documentation
└── htmlTemplates.py      # HTML/CSS templates for chat UI
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

1. **Retrieval**: Searches for the most relevant documents or text segments related to a query.
2. **Generation**: Uses language models to generate coherent and contextually accurate responses based on the retrieved information.

This hybrid approach ensures that the chatbot can provide precise, well-informed answers even when handling complex queries.

## Customization

- **Switching NLP Models**: Modify the `get_conversation_chain` function to use different Hugging Face models as per your requirements.
- **Text Chunking Parameters**: Adjust the `chunk_size` and `chunk_overlap` parameters in the `get_text_chunks` function to fine-tune the text segmentation.
- **UI Customization**: Update the `htmlTemplates.py` file to change the look and feel of the chatbot interface.

## Contributing

We welcome contributions from the community! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License.
