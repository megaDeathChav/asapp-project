# Conversational Analysis and Information Extraction with LLMs

This project provides tools for processing and analyzing customer-agent conversations using advanced Large Language Models (LLMs) such as BERT, LLaMA, and Gemini. The project includes a FastAPI-based API for real-time information extraction, exploratory data analysis (EDA) for dataset insights, and evaluation metrics to validate model performance.

## Table of Contents
1. Project Overview
2. Setup Instructions
3. API Usage
4. Exploratory Data Analysis (EDA)
5. Using the Models
6. BERT
7. LLaMA
8. Gemini
9. ChatGPT
10. Datasets
11. Contributing
12. License

## Project Overview
The goal of this project is to:
- Extract structured information (name, email, phone, etc.) from conversation datasets.
- Evaluate the performance of multiple LLMs.
- Provide a user-friendly API for integrating these models.
- Perform exploratory data analysis (EDA) to understand conversation trends.

## Setup Instructions
### 1. Clone the Repository
    git clone https://github.com/your-username/conversational-llms.git
    cd conversational-llms

### 2. Create and Activate a Virtual Environment
    python -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate

### 3. Install Dependencies
    pip install -r requirements.txt

### 4. Set Up Google API Key for Gemini
Update the llmgemini.py file with your Google API key:

    genai.configure(api_key="YOUR_GOOGLE_API_KEY")

## API Usage
### 1. Start the API
Navigate to the api/ folder and run the following command:

    uvicorn api:app --reload

### 2. API Endpoint

    POST /extract-info/

### Input:
    
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

### Response:

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

### ChatGPT
- Purpose: Evaluate ChatGPT (or other LLMs) for extracting customer information (name, email, phone) from conversations.
- File: LLM_acc_score_sklearn.ipynb
- How to Use:
    1. Update the script with your ground truth JSON dataset (e.g., abcd_sample.json) and LLM predictions.
    2. Install required dependencies:

           pip install pandas scikit-learn tabulate
    3. Run the script:

           python LLM_acc_score_sklearn.ipynb
    4. Analyze the output, including:
        - Overall accuracy of ChatGPT's predictions.
        - Field-specific accuracy for name, email, and phone.
        - Mismatched results between predictions and ground truth.

 Example Output:

     LLM Prediction Accuracy: 66.67%
    
    Keywise Accuracy:
    {
        'Customer Name Accuracy': 100.0,
        'Email Accuracy': 66.67,
        'Phone Accuracy': 100.0
    }
    
    Mismatched Results:
    [
      {
        "Index": 2,
        "True Customer Name": "alessandro phoenix",
        "Predicted Customer Name": "alessandro phoenix",
        "True Email": "aphoenix939@email.com",
        "Predicted Email": "incorrectemail@gmail.com",
        "True Phone": "(727) 760-7806",
        "Predicted Phone": "(727) 760-7806",
        "Match": false
      }
    ]
    
      

## Datasets
The dataset reduction folder contains datasets for training, testing, and validation.

|File Name| Description|
|---------|------------|
|100-100-100.json| 100 train, 100 test, 100 dev|
|4000-500-500.json| 4000 train, 500 test, 500 dev|
|delexed_removed_main.json|Main dataset without delexed keys|

## Contributing
1. Fork the repository.
2. Create a feature branch:
   
       git checkout -b feature-name
3. Commit changes:

        git commit -m "Added new feature"
4. Push to your branch:

       git push origin feature-name
5. Open a pull request.


## License
This project is licensed under the MIT License. See the LICENSE file for details.


   






