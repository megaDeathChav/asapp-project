# Conversational Analysis and Information Extraction with LLMs

## Overview
This project implements AI-powered tools to analyze and extract meaningful information from customer-agent conversations. By leveraging advanced Large Language Models (LLMs) such as BERT, LLaMA, and Gemini, this project aims to:
- Convert unstructured conversation data into structured formats (e.g., names, emails, phone numbers).
- Evaluate the accuracy and performance of multiple LLMs for conversational data extraction.
- Provide an API for seamless integration into real-world systems.
- Perform Exploratory Data Analysis (EDA) to uncover key trends in conversational datasets.

This work addresses the challenges businesses face in processing large amounts of unstructured conversational data. Our solution enables data-driven decision-making, improves customer support workflows, and enhances operational efficiency.

## Features
1. **LLM Evaluation**: Testing and comparing ChatGPT, BERT, LLaMA, and Gemini for data extraction tasks.
2. **API Integration**: Built with FastAPI to allow real-time conversation analysis.
3. **Dataset Preprocessing**: Cleaned and reduced large datasets for faster model training and testing.
4. **Performance Metrics**: Accuracy scores and detailed evaluation for structured field extraction.
5. **Exploratory Data Analysis**: Insights into conversation patterns, label distributions, and field-level missing values.

## Table of Contents
1. Project Overview
2. Setup Instructions
3. API Usage
4. Exploratory Data Analysis (EDA)
5. BERT
6. LLaMA
7. Gemini
8. Accuracy Score Calculation
9. Model Evaluation
10. Datasets

## Setup Instructions
### 1. Clone the Repository
    git clone https://github.com/your-username/conversational-llms.git
    cd conversational-llms

### 2. Create and Activate a Virtual Environment
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate

### 3. Install Dependencies
    pip install -r requirements.txt

### 4. Set Up Google API Key (for Gemini)
Update the llmgemini.py file with your Google API key:

    genai.configure(api_key="YOUR_GOOGLE_API_KEY")

## API Usage
### 1. Start the API
    cd api
    uvicorn api:app --reload

### 2. Send Requests

   Endpoint: POST /extract-info/

### Sample Input:
    
    {
      "conversations": [
        {
          "conversations": [
            {"speaker": "User", "text": "Hello, I need help."},
            {"speaker": "Agent", "text": "Sure, how can I assist you?"}
          ]
        }
      ]
    }

### Sample Response:

    {
      "results": [
        {"customer_name": "John Doe", "email": "johndoe@example.com", "phone": "(123) 456-7890"}
      ]
    }

## Exploratory Data Analysis (EDA)
The EDA was performed to understand key dataset insights, including:

- Conversation Metrics: Total utterances, speaker distribution, character lengths.
- Most Common Flows and Subflows: Frequently occurring conversation patterns.
- Label Presence: Distribution of important fields like email, phone, etc.
  
### Steps to Run EDA
- Open the EDA/eda.ipynb notebook.
- Run the cells sequentially to visualize:
    - Total utterances per conversation.
    - Character length distribution.
    - Speaker dominance (customer vs. agent).

## Using the Models

### BERT
- Purpose: Classification and extraction tasks.
- File: bert.ipynb
- How to Use:
    1. Open the notebook and load the dataset.
    2. Fine-tune the model on the dataset.
    3. Evaluate metrics like accuracy and F1 score.

### LLaMA
- Purpose: Inference and JSON-based extraction.
- File: LLAMATesting.ipynb
- How to Use:
    1. Install dependencies:
       
           pip install unsloth transformers torch
    2. Load the LLaMA model and run fine-tuning/inference steps.

### Gemini
- Purpose: Extract structured information.
- File: models/llmgemini.py
- How to Use:
    1. Configure the API key.
    2. Call query_gemini_for_info() to extract data from conversations.

## Calculating Accuracy Score for Models
- Purpose: Calculate accuracy score based on any of our model's output.
- File: LLM_acc_score_sklearn.ipynb
- How to Use:
    1. Update the script with your ground truth JSON dataset and LLM predictions.
    2. Install required dependencies:

           pip install pandas scikit-learn tabulate
    3. Run the script:

           python LLM_acc_score_sklearn.ipynb
    4. Analyze the output, including:
        - Overall conversation-level accuracy.
        - Field-specific accuracy for name, email, and phone.
        - Mismatched results between predictions and ground truth.

 ## Model Evaluation
 ### Models Tested:
1. **BERT**: Best suited for classification tasks, requiring fine-tuning for each metric.
2. **LLaMA**: Performed well with JSON extraction tasks but occasionally hallucinated data.
3. **Gemini**: Offered the highest overall accuracy and ease of use via Google's API.
    
### Accuracy Overview:
|Model|Name Accuracy| Email Accuracy| Phone Accuracy| Overall Accuracy| Notes|
|---|----|----|----|-----|-----|
|BERT| 48.7% | 45.2%| 10.3%| 42.9%|Requires individual fine-tuning|
|LLaMA	|96.25% |88.75%	|81.25% | 88.75%	| Tends to hallucinate non-existent data|
|Gemini	|100%	|90%	|N/A	|86%	|Best performer; cost-effective|

## Datasets
The dataset reduction folder contains datasets for training, testing, and validation.
The Jupyter Notebook smaller_dataset_creator.ipynb was used to create the following datasets:

|File Name| Description|
|---------|------------|
|100-100-100.json| 100 train, 100 test, 100 dev|
|2400-300-300.json| 2400 train, 300 test, 300 dev|
|4000-500-500.json| 4000 train, 500 test, 500 dev|
|800-100-100.json| 800 train, 100 test, 100 dev|
|80-10-10.json| 80 train, 10 test, 10 dev|
|delexed_removed_main.json|Main dataset without delexed key|
   






