def main(raw_keywords_paste: str) -> dict:
    # Split into lines and clean
    lines = [line.strip() for line in raw_keywords_paste.splitlines() if line.strip()]
    
    # Extract keywords and minimum frequency using regex
    import re
    keyword_freq = []
    
    for line in lines:
        # Pattern to match: text, followed by 0, followed by numbers-numbers
        pattern = r'^(.*?)\s+0\s*/\s*(\d+)-\d+'
        match = re.match(pattern, line)
        
        if match:
            keyword = match.group(1).strip()
            min_freq = int(match.group(2))
            
            keyword_freq.append({
                "keyword": keyword,
                "frequency": min_freq
            })
    
    # Create JSON structure
    output_dict = {
        "keyword_frequencies": keyword_freq
    }
            
    # Convert to JSON string and wrap in markdown code block
    import json
    json_str = json.dumps(output_dict, ensure_ascii=False)
    markdown_json = f"```json\n{json_str}\n```"
    
    return {
        'result': markdown_json
    }