def main(arg1: str, arg2: str, arg3: str) -> dict:
    import json
    
    # Parse the three JSON strings into Python objects
    try:
        data1 = json.loads(arg1)
        data2 = json.loads(arg2)
        data3 = json.loads(arg3)
    except json.JSONDecodeError:
        # If JSON parsing fails, try to repair it using json_repair
        from json_repair import repair_json
        data1 = json.loads(repair_json(arg1))
        data2 = json.loads(repair_json(arg2))
        data3 = json.loads(repair_json(arg3))
    
    # Combine all keywords into a single list
    all_keywords = []
    all_keywords.extend(data1.get("pretty_keywords", []))
    all_keywords.extend(data2.get("pretty_keywords", []))
    all_keywords.extend(data3.get("pretty_keywords", []))
    
    # Remove duplicates while preserving order
    seen = set()
    unique_keywords = [x for x in all_keywords if not (x in seen or seen.add(x))]
    
    # Create the output structure and convert to JSON string
    result = {
        "pretty_keywords": unique_keywords
    }
    json_str = json.dumps(result, ensure_ascii=False, indent=2)
    
    # Wrap in markdown code block
    markdown_json = f"```json\n{json_str}\n```"
    
    return {
        'pretty_keywords_complete': markdown_json
    }
