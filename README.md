# AIPPTBuilder API

**AIPPTBuilder API** is an AI-powered backend service designed for creating slide presentations. This API enables users to input various types of data and content and generate structured, visually coherent PowerPoint slides. It leverages advanced **Large Language Models (LLMs)** and a **Retrieval-Augmented Generation (RAG)** pipeline to ensure relevant, context-aware, and accurate slide creation. The API supports a wide range of file types, making it a multimodal solution for content creation.

Developed by **Wilfredo Aaron Sosa Ramos**, this API is built with cutting-edge technologies like **Python**, **FastAPI**, **LangChain**, **Google Generative AI**, and **ChromaDB** to deliver real-time, few-shot AI responses formatted in JSON.

## Table of Contents

- [1. Features](#1-features)
- [2. Slide Creation Service](#2-slide-creation-service)
- [3. RAG Pipeline](#3-rag-pipeline)
- [4. Multimodal Capabilities](#4-multimodal-capabilities)
- [5. Technologies Used](#5-technologies-used)
- [6. Installation Guide](#6-installation-guide)
- [7. How to Use](#7-how-to-use)

---

## 1. Features

The **AIPPTBuilder API** offers the following key features:

- **AI-Driven Slide Creation**: Automatically generates slides based on input content, topics, and presentation structures.
- **RAG Pipeline**: Combines retrieval-augmented generation (RAG) to pull relevant data from a vector database and generate slides with contextually accurate content.
- **Few-Shot Learning**: Uses a few-shot approach to ensure that each slide is tailored to the specific input, even with limited examples.
- **Multimodal Support**: Handles over 16 different file types (PDF, TXT, WORD, EXCEL, images, YouTube videos, etc.), enabling diverse content integration for slide creation.
- **JSON Output**: Provides structured responses in JSON format, ensuring compatibility with various client applications and seamless integration.

These features allow users to automate the slide creation process, whether for educational, professional, or creative purposes.

---

## 2. Slide Creation Service

The **Slide Creation Service** is the core functionality of the **AIPPTBuilder API**. It allows users to generate slide presentations by providing inputs such as:

- **Prompt or Topic**: Users input a topic or prompt related to the content of the presentation. The API processes this prompt to generate slides that are relevant to the subject matter.
- **Multimodal Data**: Supports multiple file types like PDFs, text documents, images, or even video links to enrich the content of the slides.
- **Few-Shot AI**: Using few-shot learning, the API can create slides that are precise, relevant, and highly specific to the user’s input with minimal examples.

The service generates well-structured slides, including titles, bullet points, and other relevant content, formatted to be compatible with PowerPoint or other presentation software.

---

## 3. RAG Pipeline

The **AIPPTBuilder API** relies on a **Retrieval-Augmented Generation (RAG)** pipeline to provide high-quality, context-aware slide content. Here’s how it works:

1. **Prompt**: The user provides a prompt, such as a topic or subject for the slide presentation.
2. **Vector DB (ChromaDB)**: The system retrieves relevant information from a vectorized database, **ChromaDB**, which stores various pieces of knowledge in vector form for quick retrieval.
3. **Retriever**: The retriever narrows down the most relevant pieces of content, ensuring the generated slides are contextually accurate.
4. **LLM (Large Language Model)**: The retrieved content is passed into the LLM (powered by **Google Generative AI**) to generate slide content based on the input.
5. **Parser**: The content is parsed and formatted into structured JSON, making it ready for further processing or direct conversion into slides.

This pipeline ensures that the slides generated are not only based on AI-generated knowledge but also relevant to the specific context of the prompt.

---

## 4. Multimodal Capabilities

One of the key strengths of the **AIPPTBuilder API** is its support for over 16 different file types, making it a powerful multimodal tool for slide creation. Supported file types include:

- **Documents**: PDF, TXT, WORD, EXCEL
- **Images**: PNG, JPG, GIF
- **Videos**: YouTube links, MP4
- **Data Files**: CSV, JSON
- **Other**: Markdown, LaTeX

This multimodal capability allows the system to pull data from various content types and integrate them into the slides, ensuring a diverse and rich presentation experience.

---

## 5. Technologies Used

The **AIPPTBuilder API** is built using a modern tech stack that ensures fast, scalable, and reliable performance:

- **Python**: The primary programming language used to build the backend.
- **FastAPI**: A fast and modern web framework for building APIs with Python.
- **LangChain**: A framework that facilitates the building of LLM-powered applications, integrating various AI services.
- **Google Generative AI**: Powers the language model that generates content for the slides.
- **ChromaDB**: A vector database that stores content in a vectorized format, enabling fast and accurate retrieval.
- **RAG Pipeline**: Combines retrieval and generation to deliver context-aware content in a few-shot manner.

---

## 6. Installation Guide

To set up and run the **AIPPTBuilder API** locally, follow these steps:

1. **Clone the repository**:
   - Use the following command to clone the repository to your local machine:
     ```
     git clone https://github.com/yourusername/AIPPTBuilderAPI.git
     ```

2. **Navigate to the project directory**:
   - Move into the project folder:
     ```
     cd AIPPTBuilderAPI
     ```

3. **Set up a virtual environment** (optional but recommended):
   - Create and activate a virtual environment:
     ```
     python -m venv venv
     source venv/bin/activate
     ```

4. **Install dependencies**:
   - Install the required Python libraries using pip:
     ```
     pip install -r requirements.txt
     ```

5. **Run the development server**:
   - Start the FastAPI server locally:
     ```
     uvicorn app.main:app --host 0.0.0.0 --port 8000
     ```

6. **Test the API**:
   - Access the interactive API documentation via Swagger UI at `http://localhost:8000/docs`.

---

## 7. How to Use

Once the **AIPPTBuilder API** is running, you can use it to create slide presentations by sending requests to the available endpoints. Below is an overview of the typical workflow:

1. **Provide Input**:
   - Submit a request with a **prompt** or **topic** for the slides. You can also include multimodal data such as documents, images, or videos to enrich the presentation.

2. **RAG Pipeline Activation**:
   - The API will retrieve relevant content from **ChromaDB**, process it using the **Google Generative AI**, and format the response into structured slides.

3. **JSON Response**:
   - The output will be provided in JSON format, with structured data including titles, bullet points, and slide content ready to be imported into a presentation tool.

4. **Integration**:
   - Use the generated JSON to create PowerPoint presentations or other slide formats.

---

With **AIPPTBuilder API**, users can generate professional and well-structured presentations effortlessly by leveraging advanced AI and multimodal capabilities.
