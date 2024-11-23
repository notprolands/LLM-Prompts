def main(arg1: str) -> dict:
    """
    Processes text input containing keywords with frequencies and returns both
    frequency-mapped keywords and a plain keyword list.
    
    Args:
        arg1 (str): Text containing keywords with frequencies in format "keyword 0 / min-max"
    
    Returns:
        dict: Dictionary containing two markdown-wrapped JSON strings:
            - keywords_and_frequencies: Keywords mapped to their minimum frequencies
            - keywords: List of keywords without frequencies
    """
    import re
    import json

    def process_keywords(text):
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        keyword_freq_dict = {}
        
        for line in lines[1:]:
            pattern = r'^(.*?)\s+0\s*/\s*(\d+)-\d+'
            match = re.match(pattern, line)
            
            if match:
                keyword = match.group(1).strip()
                min_freq = int(match.group(2))
                keyword_freq_dict[keyword] = min_freq
                
        return {"keywords_and_frequencies": keyword_freq_dict}

    def process_keywords_only(text):
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        keywords = []
        
        for line in lines[1:]:
            pattern = r'^(.*?)\s+0\s*/'
            match = re.match(pattern, line)
            
            if match:
                keyword = match.group(1).strip()
                keywords.append(keyword)
                
        return {"keywords": keywords}

    # Process keywords
    keywords_dict = process_keywords(arg1)
    keywords_only_dict = process_keywords_only(arg1)

    # Convert to JSON strings
    keywords_json = json.dumps(keywords_dict["keywords_and_frequencies"], ensure_ascii=False)
    keywords_only_json = json.dumps(keywords_only_dict["keywords"], ensure_ascii=False)

    # Wrap in markdown code blocks
    keywords_markdown = f"```json\n{keywords_json}\n```"
    keywords_only_markdown = f"```json\n{keywords_only_json}\n```"

    return {
        'keywords_and_frequencies': keywords_markdown,
        'keywords': keywords_only_markdown
    }