# NTTRAG-PYBOT-SCRATCH

## Overview

The **NTTRAG-PYBOT-SCRATCH** project is an educational and practical exploration into the development of a chatbot using custom-built NLP pipelines from the ground up. This version of the chatbot is designed to offer a transparent, step-by-step guide to creating a Retrieval-Augmented Generation (RAG) system. Unlike typical implementations that rely heavily on pre-built frameworks, this project manually constructs each component, providing an in-depth understanding of how modern NLP techniques can be implemented and optimized.

![Architecture and Workflow](/img/workflow.png)

### Project Purpose

The primary aim of this project is to demystify the processes involved in building a sophisticated chatbot system by constructing each part of the RAG pipeline manually. This approach offers invaluable insights into the inner workings of NLP applications, serving as both a learning resource and a foundation for further research or custom developments.

## Architecture and Workflow

The NTTRAG-PYBOT-SCRATCH system is designed to run on a local GPU, making use of high-performance computing to handle large-scale document processing and information retrieval. The following steps outline the architecture and workflow of the system:

### 1. Document Preprocessing and Embedding Creation

- **Collection of Documents**: 
  - A large database of Python-related documents, primarily PDFs, is collected as the knowledge base for the chatbot.
  
- **Preprocessing**:
  - These documents are converted into smaller, manageable text chunks, typically grouped into 12-sentence passages. This step is crucial for ensuring that the information is processed in a format suitable for embedding creation and retrieval.

- **Embedding Creation**:
  - The smaller text chunks are transformed into numerical embeddings using an embedding model (e.g., Sentence Transformers). These embeddings are numerical representations of the text, allowing for efficient similarity searches.

### 2. Embedding Storage

- **Vectorial Database**:
  - The embeddings are stored in a vectorial database, optimized for rapid retrieval. In this project, the embeddings are stored using `torch.center`, which is particularly efficient even when dealing with a large number of embeddings (e.g., 100k+ embeddings).

### 3. Search and Answer

- **Query Processing**:
  - When a user inputs a query, it is converted into an embedding similar to the document embeddings. This allows the system to search the vectorial database for the most relevant passages.

- **Response Generation**:
  - The relevant passages retrieved from the vectorial database are used by a language model (LLM) to generate a response that is contextually relevant to the user’s query.

## Modules Overview

### Imported Modules

The following table lists the Python modules used in the NTTRAG-PYBOT-SCRATCH application, along with a brief description of each:

| Module                  | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `os`                    | Provides a way of using operating system-dependent functionality like file paths.|
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

## How to Run

To get started with the NTTRAG-PYBOT-SCRATCH, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/NTTRAG-PYBOT-SCRATCH.git
