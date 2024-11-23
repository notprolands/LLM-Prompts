# Dify Python Function Considerations

Dify application is a low-code node programming software, where information flows from node to node. One of those nodes is "code" node which allows user to input custom Python function.

## Considerations

- Input is usually arg1, arg2, arg3, etc.
- Output variables must be declared as 'result' in the output variables.
- Output variables must be correct type, e.g. string, number, array[number], array [string], array[object], object.

## Example Functions

This section contains functions that work in Dify application correctly.

### Example Function 1

Function to extract extract subtitles and outlines.

```python
def main(arg1: str) -> dict:
    import json
    data = json.loads(arg1)
    
    # Create an array of objects
    result = [{'section': item["section"], 'bullets': item["bullets"]} for item in data]
    
    return {
        'result': result
    }
```
### Example Function 2

Function to calculate the variance of an array.

```python
def main(x: list) -> float:
    return {
        # Note to declare 'result' in the output variables
        'variance': sum([(i - sum(x) / len(x)) ** 2 for i in x]) / len(x)
    }
```

### Example Function 3

Function that merges data from two knowledge bases.

```python
 def main(knowledge1: list, knowledge2: list) -> list:
    return {
        # Note to declare 'result' in the output variables
        'result': knowledge1 + knowledge2
    }
```

### Example Function 4

Function to parse raw keywords paste into JSON.

```python
def main(arg1: str) -> dict:
    # Split into lines and clean
    lines = [line.strip() for line in arg1.splitlines() if line.strip()]
    
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
        'keywords_and_frequencies': markdown_json
    }
```
