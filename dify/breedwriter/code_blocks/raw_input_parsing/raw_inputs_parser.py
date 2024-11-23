def main(arg1: str, arg2: str, arg3: str) -> dict:
    """
    Processes three text inputs and converts them into structured JSON format wrapped in markdown code blocks.
    
    Args:
        arg1 (str): Text containing keywords with frequencies in format "keyword 0 / min-max"
        arg2 (str): Text containing header fragments
        arg3 (str): Text containing question fragments
    
    Returns:
        dict: Dictionary containing four markdown-wrapped JSON strings:
            - keywords_and_frequencies: Keywords mapped to their minimum frequencies
            - keywords: List of keywords without frequencies
            - headers: List of header fragments
            - questions: List of question fragments
    """
    import re
    import json

    def process_keywords(text):
        """
        Extracts keywords and their minimum frequencies from text.
        Example input line: "pekińczyk 0 / 2-5" -> {"pekińczyk": 2}
        """
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        keyword_freq_dict = {}
        
        # Skip first line by starting from index 1
        for line in lines[1:]:
            pattern = r'^(.*?)\s+0\s*/\s*(\d+)-\d+'  # Matches "keyword 0 / min-max"
            match = re.match(pattern, line)
            
            if match:
                keyword = match.group(1).strip()
                min_freq = int(match.group(2))
                keyword_freq_dict[keyword] = min_freq
                
        return {"keywords_and_frequencies": keyword_freq_dict}

    def process_keywords_only(text):
        """
        Extracts just the keywords without frequencies.
        Example input line: "pekińczyk 0 / 2-5" -> "pekińczyk"
        """
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        keywords = []
        
        # Skip first line by starting from index 1
        for line in lines[1:]:
            # Extract everything before the "0 /" pattern
            pattern = r'^(.*?)\s+0\s*/'
            match = re.match(pattern, line)
            
            if match:
                keyword = match.group(1).strip()
                keywords.append(keyword)
                
        return {"keywords": keywords}

    def process_fragments(text, key_name):
        """
        Processes text fragments by removing trailing numbers.
        Example: "Some text 123" -> "Some text"
        """
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        fragments = []
        
        for line in lines:
            # Remove trailing numbers and whitespace
            text = re.sub(r'\s*\d+\s*$', '', line).strip()
            if text:
                fragments.append(text)
                
        return fragments

    # Process all inputs into their respective formats
    keywords_dict = process_keywords(arg1)
    keywords_only_dict = process_keywords_only(arg1)

    # Convert processed data to JSON strings
    keywords_json = json.dumps(keywords_dict["keywords_and_frequencies"], ensure_ascii=False)
    keywords_only_json = json.dumps(keywords_only_dict["keywords"], ensure_ascii=False)
    headers_json = json.dumps({"header_fragments": process_fragments(arg2, "header_fragments")}, ensure_ascii=False)
    questions_json = json.dumps({"question_fragments": process_fragments(arg3, "question_fragments")}, ensure_ascii=False)

    # Wrap each JSON string in markdown code block
    keywords_markdown = f"```json\n{keywords_json}\n```"
    keywords_only_markdown = f"```json\n{keywords_only_json}\n```"
    headers_markdown = f"```json\n{headers_json}\n```"
    questions_markdown = f"```json\n{questions_json}\n```"

    # Return all processed data in a dictionary
    return {
        'keywords_and_frequencies': keywords_markdown,
        'keywords': keywords_only_markdown,
        'headers': headers_markdown,
        'questions': questions_markdown
    }