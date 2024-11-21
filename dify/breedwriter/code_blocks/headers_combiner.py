def main(arg1: str, arg2: str) -> dict:
    import json
    
    # Remove the ```json and ``` markers and clean up whitespace
    def clean_json(text):
        return text.replace('```json', '').replace('```', '').strip()
    
    # Clean and parse both JSON strings
    data1 = json.loads(clean_json(arg1))
    data2 = json.loads(clean_json(arg2))
    
    # Combine the header_sentences arrays
    combined = {
        "header_sentences": data1["header_sentences"] + data2["header_sentences"]
    }
    
    # Convert to JSON string and add markers
    json_str = json.dumps(combined, ensure_ascii=False, indent=4)
    formatted_output = f"```json\n{json_str}\n```"
    
    return {
        'result': formatted_output
    }