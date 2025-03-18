import streamlit as st
from web_scraper import fetch_webpage
from vector_store import store_text_in_faiss, load_faiss_db
from summarizer import summarize_text

st.title("AI Web Summarizer")
url = st.text_input("Enter a webpage URL:")

if st.button("Summarize"):
    if url:
        with st.spinner("Fetching and processing..."):
            # Step 1: Scrape webpage
            content = fetch_webpage(url)
            
            # Step 2: Store extracted text in FAISS
            store_text_in_faiss(content)
            db = load_faiss_db()

            # Step 3: Retrieve relevant info
            query = "Summarize the main points"
            docs = db.similarity_search(query, k=5)
            key_info = " ".join([doc.page_content for doc in docs])

            # Step 4: Generate summary using LLM
            summary = summarize_text(key_info)

            # Display results
            st.subheader("Extracted Key Information")
            st.write(key_info)

            st.subheader("Generated Summary")
            st.write(summary)
