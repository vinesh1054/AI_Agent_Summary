
# **AI Agent for summary - Zocket Assignment 🚀**  
An AI-powered agent that extracts and summarizes key information from any given webpage.  

## **🔹 Overview**  
This project is part of an **AI/ML intern assignment**, demonstrating expertise in **web scraping, NLP, embeddings, vector storage, and LLM-powered summarization**. The AI agent:  
✅ Accepts a **URL as input**  
✅ Scrapes and **cleans webpage content**  
✅ Converts text into **vector embeddings (FAISS)**  
✅ Retrieves **key information** using **semantic search**  
✅ Generates a **concise summary** using an LLM (Hugging Face API)  
✅ Provides a **user-friendly Streamlit UI**  

## **🔹 Tech Stack & Libraries**  
| **Category** | **Tools & Libraries** |
|-------------|----------------------|
| **Web Scraping** | `requests`, `BeautifulSoup` |
| **Text Processing** | `langchain.text_splitter` |
| **Vector Storage & Retrieval** | `FAISS`, `sentence-transformers` |
| **Summarization (LLM)** | `transformers` (Mistral-7B via Hugging Face API) |
| **UI** | `streamlit` |
| **Environment Management** | `dotenv` (for API keys) |

---

## **🔹 Project Structure**  

```plaintext
Zocket_Assgn01_Modified/
│── app.py                # Streamlit UI for user interaction
│── web_scraper.py        # Fetches and cleans webpage content
│── vector_store.py       # Stores text in FAISS and retrieves key info
│── summarizer.py         # Calls Hugging Face API for summarization
│── .env                  # Stores API keys securely
│── requirements.txt      # Lists all dependencies
│── README.md             # Documentation for the project
```

---

## **🔹 Setup & Installation**  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/yourusername/Zocket_Assgn01_Modified.git
cd Zocket_Assgn01_Modified
```

### **2️⃣ Install Dependencies**  
Ensure you have **Python 3.8+** installed. Then, install required packages:  
```bash
pip install -r requirements.txt
```

### **3️⃣ Add Hugging Face API Key**  
Create a `.env` file and add your **Hugging Face API Key**:  
```plaintext
HUGGINGFACE_API_KEY=your_api_key_here
```

### **4️⃣ Run the Streamlit App**  
```bash
streamlit run app.py
```

---

## **🔹 How It Works**  

1️⃣ **Web Scraping (`web_scraper.py`)**  
- Fetches webpage content using `requests` and `BeautifulSoup`.  
- Cleans and extracts **main article content** while removing irrelevant text.  

2️⃣ **Vector Storage (`vector_store.py`)**  
- Splits text into **overlapping chunks** for better retention.  
- Converts text into **vector embeddings** using `sentence-transformers`.  
- Stores embeddings in **FAISS** for fast retrieval.  

3️⃣ **Summarization (`summarizer.py`)**  
- Retrieves the **most relevant text chunks** from FAISS.  
- Calls **Mistral-7B (Hugging Face API)** to generate a **concise summary**.  

4️⃣ **User Interface (`app.py`)**  
- Accepts a **URL** input from the user.  
- Displays extracted **key information** and **generated summary**.  

---
<!-- 
## **🔹 Example Run**  

### **Input URL**  
🔗 [Mint-News on Gold Price](https://www.livemint.com/market/stock-market-news/gold-price-surges-to-90-000-per-10-grams-how-to-trade-amid-rising-prices-11742370589779.html)   -->

<!-- ### **Extracted Key Information**  
📌 *"Organizers of Leeds Festival of Gothica (LFOG) amend application process due to complaints about AI-generated art at their Alternative Market..."*   -->

<!-- ### **Generated Summary**  
📝 *"Leeds Festival of Gothica revised its vendor application process after receiving community complaints about AI-generated artwork. The event now requires vendors to disclose AI usage in their submissions."*  

--- -->

## **🔹 Why This Project Stands Out?**  
✔️ **Modular & Scalable** – Each component (scraper, vector storage, summarization) is independent.  
✔️ **Efficient Retrieval** – Uses **semantic search** via FAISS instead of naive keyword matching.  
✔️ **Latest AI Models** – Uses **Mistral-7B**, a powerful LLM for summarization.  
✔️ **Streamlit UI** – Interactive and user-friendly interface for testing.  

---

## **🔹 Future Improvements**  
🔹 Improve **LLM more customised for Summary**  
🔹 Add **memory retention** (e.g., storing past summaries).  
 
