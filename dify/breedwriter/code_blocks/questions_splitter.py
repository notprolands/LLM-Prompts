def main(arg1: str) -> dict:
    """
    Splits a JSON string of question sentences into three roughly equal parts.
    Works with input both with and without markdown code block formatting.
    
    Args:
        arg1 (str): JSON string containing a list of question sentences,
        optionally wrapped in ```json ``` markers
    """
    import json
    from json_repair import repair_json
    
    # Remove markdown code block formatting if present
    cleaned_input = arg1.strip()
    if cleaned_input.startswith('```json'):
        cleaned_input = cleaned_input[7:]  # Remove ```json
    if cleaned_input.endswith('```'):
        cleaned_input = cleaned_input[:-3]  # Remove trailing ```
    cleaned_input = cleaned_input.strip()
    
    # Try to parse JSON, use repair if needed
    try:
        json_dict = json.loads(cleaned_input)
    except json.JSONDecodeError:
        repaired = repair_json(cleaned_input)
        json_dict = json.loads(repaired)
    
    # Get the list of questions
    questions = json_dict.get('question_sentences', [])
    
    # Calculate split points
    length = len(questions)
    first_split = length // 3
    second_split = 2 * length // 3
    
    # Split questions into three parts
    first_part = questions[:first_split]
    second_part = questions[first_split:second_split]
    third_part = questions[second_split:]
    
    # Wrap each part in a new dictionary and convert to JSON string
    json_p1 = json.dumps({'question_sentences': first_part}, ensure_ascii=False)
    json_p2 = json.dumps({'question_sentences': second_part}, ensure_ascii=False)
    json_p3 = json.dumps({'question_sentences': third_part}, ensure_ascii=False)
    
    # Wrap in markdown code blocks
    markdown_p1 = f"```json\n{json_p1}\n```"
    markdown_p2 = f"```json\n{json_p2}\n```"
    markdown_p3 = f"```json\n{json_p3}\n```"
    
    return {
        'questions_p1': markdown_p1,
        'questions_p2': markdown_p2,
        'questions_p3': markdown_p3
    } 