import re
import unicodedata


def normalize_text(text: str) -> str:
    """
    Normalize text by converting to lowercase, normalizing unicode characters,
    removing punctuation, and cleaning up whitespace.
    
    Args:
        text: The text to normalize
        
    Returns:
        The normalized text string
    """
    # Lowercase
    text = text.lower()
    
    # Normalize unicode (e.g., é → e)
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Optionally: Combine single-letter initials (e.g., "j k rowling" → "jk rowling")
    text = re.sub(r'\b(\w)\s+(?=\w\b)', r'\1', text)

    return text 