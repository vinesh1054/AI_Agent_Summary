# import requests
# from bs4 import BeautifulSoup

# def fetch_webpage(url):
#     """Fetches and extracts clean text from a given URL."""
#     response = requests.get(url)
#     if response.status_code != 200:
#         raise Exception(f"Failed to fetch URL: {url}")

#     soup = BeautifulSoup(response.text, "html.parser")
#     return ' '.join([p.text for p in soup.find_all("p")])  # Extract paragraphs

import requests
from bs4 import BeautifulSoup
import re

def fetch_webpage(url):
    """Fetches and extracts only the main article content from a given URL."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Remove unwanted elements
        unwanted_elements = [
            'script', 'style', 'nav', 'header', 'footer', 'aside', 'iframe',
            'noscript', 'form', 'button', 'input', 'meta', 'link'
        ]
        for tag in unwanted_elements:
            for element in soup.find_all(tag):
                element.decompose()
        
        # Remove elements with classes/ids suggesting non-article content
        unwanted_patterns = [
            'ad', 'popup', 'modal', 'sidebar', 'banner', 'cookie', 'newsletter',
            'subscription', 'promo', 'social', 'share', 'comment', 'related',
            'recommended', 'download', 'app', 'disclaimer', 'copyright', 'footer',
            'header', 'nav', 'menu', 'tag', 'author', 'date', 'time', 'publish'
        ]
        pattern = re.compile('|'.join(unwanted_patterns), re.IGNORECASE)
        
        for element in soup.find_all(attrs={'class': pattern}):
            element.decompose()
        for element in soup.find_all(attrs={'id': pattern}):
            element.decompose()
        
        # Try to find the main article container
        article_container = None
        
        # Look for common article containers
        for container in ['article', 'main', 'div', 'section']:
            # First try with article-related classes
            candidates = soup.find_all(container, class_=re.compile(r'article|content|main|story|post', re.IGNORECASE))
            if candidates:
                # Choose the candidate with the most paragraphs
                article_container = max(candidates, key=lambda x: len(x.find_all('p')))
                break
        
        # If no specific article container found, use the body
        if not article_container:
            article_container = soup.body
        
        # Extract paragraphs from the article container
        paragraphs = article_container.find_all('p')
        
        # Filter out short paragraphs and likely non-article content
        filtered_paragraphs = []
        for p in paragraphs:
            text = p.text.strip()
            # Skip short paragraphs
            if len(text) < 30:
                continue
            # Skip paragraphs with common non-article content keywords
            if re.search(r'disclaimer|copyright|download|app|subscribe|newsletter', text, re.IGNORECASE):
                continue
            filtered_paragraphs.append(text)
        
        # Join the filtered paragraphs
        article_text = ' '.join(filtered_paragraphs)
        
        # Clean up whitespace and special characters
        article_text = re.sub(r'\s+', ' ', article_text).strip()
        
        return article_text
        
    except Exception as e:
        raise Exception(f"Failed to fetch or parse URL: {str(e)}")