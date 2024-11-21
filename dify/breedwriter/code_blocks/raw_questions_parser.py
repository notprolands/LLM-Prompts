def main(arg1: str) -> dict:
    # Split into lines and clean
    lines = [line.strip() for line in arg1.splitlines() if line.strip()]
    
    # Extract text parts using regex to remove trailing number
    import re
    fragments = []
    for line in lines:
        # Remove trailing number pattern (digit at end of line)
        text = re.sub(r'\s*\d+\s*$', '', line).strip()
        if text:
            fragments.append(text)
    
    # Create JSON structure
    output_dict = {
        "question_fragments": fragments
    }
            
    # Convert to JSON string and wrap in markdown code block
    import json
    json_str = json.dumps(output_dict, ensure_ascii=False)
    markdown_json = f"```json\n{json_str}\n```"
    
    return {
        'result': markdown_json
    }