def main(arg1: str, arg2: str) -> dict:
    import json
    
    # Remove backticks and "json" word from the input strings
    def clean_json_string(s: str) -> str:
        return s.replace('```json', '').replace('```', '').strip()
    
    # Clean and parse both JSON strings
    data1 = json.loads(clean_json_string(arg1))
    data2 = json.loads(clean_json_string(arg2))
    
    # Create new merged list
    result = []
    
    # Iterate through both lists simultaneously
    for d1, d2 in zip(data1, data2):
        # Merge keywords from both objects
        combined_keywords = {
            "keywords": list(set(d1["keywords"] + d2["keywords"]))
        }
        result.append(combined_keywords)
    
    # Convert the result to a JSON-formatted string with proper indentation
    json_string = f"```json\n{json.dumps(result, indent=4, ensure_ascii=False)}\n```"
    
    return {
        'result': json_string
    }