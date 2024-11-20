def main(header_sentences: str, additional_header_sentences: str) -> dict:
    import json
    
    # Remove the ```json and ``` markers and clean up whitespace
    def clean_json(text):
        return text.replace('```json', '').replace('```', '').strip()
    
    # Clean and parse both JSON strings
    data1 = json.loads(clean_json(header_sentences))
    data2 = json.loads(clean_json(additional_header_sentences))
    
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