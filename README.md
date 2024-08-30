# NTT-PYBOT 

## Overview

The NTTRAG-PYBOT project is designed to bridge the gap between theoretical learning and practical application in the field of Natural Language Processing (NLP) and chatbot development. By creating two distinct applications—one leveraging pre-trained models and frameworks, and the other built from scratch—this project aims to demonstrate the strengths, weaknesses, and practical applications of modern NLP techniques in educational contexts, specifically for teaching Python programming.
This project includes two key components:

1. **NTT-PYBOT-APP**: A chatbot application built using pre-trained models and popular frameworks like LangChain and FAISS, which are integral to creating a Retrieval-Augmented Generation (RAG) architecture. The application is designed to assist users in learning Python by responding to queries based on a rich repository of Python educational documents.

2. **NTT-PYBOT-SCRATCH**: A version of the chatbot developed from scratch using custom pipelines, intended to demystify the processes behind popular frameworks. This notebook-based application replicates the functionality of the pre-trained version but allows for deeper insight into how the frameworks operate at a granular level.

## Workflow Description

The workflow of both the pre-trained and scratch versions of the chatbot involves several key steps, which ensure efficient processing, retrieval, and response generation based on the user's queries:

1. **Collection of Documents**: 
   - Gather a large database of Python-related documents, such as PDFs, to serve as the knowledge base for the chatbot.

2. **Preprocessing**: 
   - Convert these documents into smaller, manageable text chunks. This step ensures that the information is processed in a format suitable for embedding creation and retrieval.

3. **Embedding Creation**: 
   - Transform the preprocessed text chunks into numerical embeddings. These embeddings are vectors that represent the semantic content of the text, enabling efficient and accurate retrieval.

4. **Embedding Storage**: 
   - Store the embeddings in a vector database (e.g., FAISS) to allow for quick retrieval of relevant document passages when a user query is processed.

5. **Query Processing**: 
   - Transform user queries into embeddings, similar to the document embeddings, and use these to search the stored embeddings for the most relevant passages.

6. **Response Generation**: 
   - Once relevant document passages are retrieved, a language model generates contextually appropriate responses, using the retrieved passages to inform the response content.

7. **User Interaction**: 
   - Provide an interface through which users can interact with the system. This interface allows users to input their queries and receive generated responses in a conversational format.

## Objectives

### NTT-PYBOT-APP
- **Leverage Pre-Trained Models**: Utilize existing pre-trained models and frameworks to create a functional and efficient chatbot that can assist users with Python-related queries.
- **Simplify Learning**: Provide an easy-to-use interface where users can interact with the chatbot to get answers related to Python programming, enhancing their learning experience.
- **Demonstrate RAG Architecture**: Showcase how frameworks like LangChain and FAISS can be integrated to create a robust RAG architecture, which improves the chatbot's ability to retrieve relevant information and generate accurate responses.

### NTT-PYBOT-SCRATCH
- **Transparency in NLP Processes**: To provide a clear, step-by-step breakdown of the processes involved in building a chatbot from scratch.
- **Understand Framework Processes**: Develop the chatbot from scratch to provide a detailed understanding of the processes and pipelines involved in frameworks like LangChain and FAISS.
- **Educate and Illustrate**: Serve as an educational tool that illustrates the underlying mechanisms of RAG architecture by breaking down complex processes into comprehensible steps.
- **Custom Implementation**: Highlight the flexibility and depth of understanding that comes with building such a system from scratch, allowing for potential customization and optimization that may not be possible with pre-built frameworks.

## Modules Overview

### Imported Modules in Each Application

The following tables list the Python modules used in both the pre-trained model application (`app.py`) and the custom, scratch-built application (`NTTRAG-PYBOT.ipynb`).

#### NTT-PYBOT-APP (`app.py`)

| Module           | Description                                                                      |
|------------------|----------------------------------------------------------------------------------|
| `os`             | Provides a way of using operating system-dependent functionality like file paths.|
| `dotenv`         | Loads environment variables from a `.env` file.                                  |
| `streamlit`      | A framework for creating web apps easily in Python.                              |
| `openai`         | OpenAI's API for interacting with GPT and other models.                          |
| `langchain`      | Framework for building applications with LLMs, especially for RAG.               |
| `PyPDF2`         | Library for working with PDF files, such as reading and extracting text.         |

#### NTT-PYBOT-SCRATCH (`NTT-PYBOT.ipynb`)

| Module                  | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `numpy`                 | Library for numerical computing with arrays and matrices.                   |
| `pandas`                | Data analysis and manipulation tool.                                        |
| `matplotlib`            | Plotting library for creating static, animated, and interactive visualizations. |
| `random`                | Module for generating pseudo-random numbers.                                |
| `time`                  | Time-related functions.                                                     |
| `re`                    | Regular expression operations for string matching and manipulation.         |
| `textwrap`              | Text wrapping and filling utility.                                          |
| `fitz`                  | PyMuPDF, a library for PDF manipulation.                                    |
| `spacy`                 | NLP library for text processing and analysis.                               |
| `tqdm`                  | Provides a fast, extensible progress bar for loops.                         |
| `sentence_transformers` | Framework for fine-tuning and using Transformer models for generating sentence and token embeddings. |
| `torch`                 | Tensor library like NumPy, with strong GPU support, typically used with PyTorch. |
| `requests`              | Simple HTTP library for making network requests.                            |

These tables provide a quick reference to understand the different libraries and frameworks utilized in each application, highlighting the differences in approach and tooling between the pre-built and scratch-built versions.
 
# Lightning AI Overview

## Introduction

**Lightning AI** is a powerful framework designed to streamline the development of machine learning and artificial intelligence applications. Originally known as PyTorch Lightning, Lightning AI has broadened its scope to support a wider range of AI development tasks while minimizing boilerplate code and simplifying the scaling process.

## Key Features

### Simplicity and Flexibility
Lightning AI is built to abstract away the complexities of machine learning operations while allowing developers to retain full control over their processes. This balance makes it suitable for both beginners and experienced developers.

### Scalability
The framework excels in scalability, enabling developers to seamlessly scale their models from local development environments to training on multiple GPUs and clusters in the cloud without modifying the core code.

### Reproducibility
Lightning AI promotes reproducible science by standardizing the experimental setup, which is vital for ensuring consistency across experiments in both academic research and industry applications.

### Integration with Major AI Tools
It integrates well with popular AI and data science tools such as PyTorch, TensorFlow, and scikit-learn, making it a versatile addition to a developer’s toolkit.

### Performance Optimization
Lightning AI supports advanced techniques like mixed precision training and gradient accumulation, optimizing performance without sacrificing precision.

### Comprehensive Ecosystem
The ecosystem includes tools for every stage of the AI development pipeline, from data preprocessing and model building to training, fine-tuning, and deployment. It also supports plugins for advanced computing environments, enhancing its adaptability.

## Use Cases

- **Research**: Enables rapid prototyping and testing of new ideas in academic and research settings.
- **Industry Applications**: Used across various industries for developing AI models that require robust computing, such as in autonomous vehicles, healthcare imaging, and natural language processing.
- **Education**: Provides an accessible platform for teaching complex machine learning concepts.

   Lightning AI is a comprehensive framework that supports the entire lifecycle of AI model development. Its focus on reducing complexity, combined with robustness and flexibility, makes it an indispensable tool for anyone involved in machine learning and AI    development.

   For more information, tutorials, and community resources, visit the [Lightning AI website](https://lightning.ai/).

## How to Run

1. **Clone the Repository**: 
   ```bash
   git clone https://github.com/3pacc/NTT-PYBOT.git
   ```


