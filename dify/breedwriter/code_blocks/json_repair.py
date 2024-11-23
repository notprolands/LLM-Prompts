def main(arg1: str) -> dict:
    from json_repair import repair_json
    import json
    
    # Clean the input string (remove markdown code blocks if present)
    def clean_input(s: str) -> str:
        return s.replace('```json', '').replace('```', '').strip()
    
    try:
        # Clean and repair the JSON
        cleaned_input = clean_input(arg1)
        fixed_json = repair_json(cleaned_input, ensure_ascii=False)
        
        # Create pretty version with 2-space indentation
        fixed_json_obj = json.loads(fixed_json)
        pretty_json = json.dumps(fixed_json_obj, indent=2, ensure_ascii=False)
        
        # Wrap both results in markdown code blocks
        markdown_json = f"```json\n{fixed_json}\n```"
        markdown_pretty = f"```json\n{pretty_json}\n```"
        
        return {
            'compact_json': markdown_json,
            'pretty_json': markdown_pretty
        }
    except Exception as e:
        return {
            'compact_json': f"Error fixing JSON: {str(e)}",
            'pretty_json': f"Error fixing JSON: {str(e)}"
        }