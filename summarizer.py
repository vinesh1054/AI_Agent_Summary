import os
from dotenv import load_dotenv
from langchain.llms import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate

# Step 1: Load environment variables
load_dotenv()
HF_TOKEN = os.getenv("HF_TOKEN")  # Load API token from .env
HUGGINGFACE_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"

print("HF_TOKEN successfully loaded.")  # Debugging step

# Step 2: Setup LLM (Mistral 7B) for Summarization
def load_llm(huggingface_repo_id):
    """Initialize Hugging Face API-based LLM for summarization."""
    llm = HuggingFaceEndpoint(
        repo_id=huggingface_repo_id,
        huggingfacehub_api_token=HF_TOKEN,
        task="text-generation",
        temperature=0.3  # Lower temp for more deterministic summaries
    )
    return llm

# Step 3: Custom Prompt for Summarization
SUMMARIZATION_PROMPT_TEMPLATE = """
You are an AI assistant that specializes in summarizing text clearly and concisely.

### **Guidelines:**
- **Extract key points** without changing the meaning.
- **Avoid unnecessary details** and keep it to the main ideas.
- **Ensure readability** and coherence.

---

### **Text to Summarize:**
{text}

---

### **Summary:**  
(Provide a well-structured, concise summary.)
"""

def set_summarization_prompt(custom_prompt_template):
    """Create a structured prompt template for summarization."""
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=["text"])
    return prompt

# Step 4: Function to Summarize Text
def summarize_text(text):
    """Generates a summary using Mistral 7B API with a structured prompt."""
    llm = load_llm(HUGGINGFACE_REPO_ID)  # Load LLM
    prompt = set_summarization_prompt(SUMMARIZATION_PROMPT_TEMPLATE)  # Load prompt

    # Format the final input prompt
    formatted_prompt = prompt.format(text=text)
    response = llm(formatted_prompt)  # Call the LLM
    return response.strip()

# Example Usage
if __name__ == "__main__":
    sample_text = """
    Artificial intelligence is revolutionizing industries by automating tasks 
    and enabling data-driven decision-making. Advances in deep learning and 
    natural language processing have significantly improved AI capabilities, 
    leading to applications in healthcare, finance, and many other sectors. 
    However, ethical concerns such as bias, transparency, and job displacement 
    remain important considerations.
    """
    
    summary = summarize_text(sample_text)
    print("\n### Generated Summary:\n", summary)
