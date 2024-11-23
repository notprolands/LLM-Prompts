# Supported use cases

### Fixing Syntax Errors in JSON

- Missing quotes, misplaced commas, unescaped characters, and incomplete key-value pairs.
- Missing quotation marks, improperly formatted values (true, false, null), and repairs corrupted key-value structures.

### Repairing Malformed JSON Arrays and Objects

- Incomplete or broken arrays/objects by adding necessary elements (e.g., commas, brackets) or default values (null, "").
- The library can process JSON that includes extra non-JSON characters like comments or improperly placed characters, cleaning them up while maintaining valid structure.

### Auto-Completion for Missing JSON Values

- Automatically completes missing values in JSON fields with reasonable defaults (like empty strings or null), ensuring validity.

# How to use

Install the library with pip

    pip install json-repair

then you can use use it in your code like this

    from json_repair import repair_json

    good_json_string = repair_json(bad_json_string)
    # If the string was super broken this will return an empty string

You can use this library to completely replace `json.loads()`:

    import json_repair

    decoded_object = json_repair.loads(json_string)

or just

    import json_repair

    decoded_object = json_repair.repair_json(json_string, return_objects=True)

### Avoid this antipattern
Some users of this library adopt the following pattern:

    obj = {}
    try:
        obj = json.loads(string)
    except json.JSONDecodeError as e:
        obj = json_repair.loads(string)
        ...

This is wasteful because `json_repair` will already verify for you if the JSON is valid, if you still want to do that then add `skip_json_loads=True` to the call as explained the section below.

### Read json from a file or file descriptor

JSON repair provides also a drop-in replacement for `json.load()`:

    import json_repair

    try:
        file_descriptor = open(fname, 'rb')
    except OSError:
        ...

    with file_descriptor:
        decoded_object = json_repair.load(file_descriptor)

and another method to read from a file:

    import json_repair

    try:
        decoded_object = json_repair.from_file(json_file)
    except OSError:
        ...
    except IOError:
        ...

Keep in mind that the library will not catch any IO-related exception and those will need to be managed by you

### Non-Latin characters

When working with non-Latin characters (such as Chinese, Japanese, or Korean), you need to pass `ensure_ascii=False` to `repair_json()` in order to preserve the non-Latin characters in the output.

Here's an example using Chinese characters:

    repair_json("{'test_chinese_ascii':'统一码'}")

will return

    {"test_chinese_ascii": "\u7edf\u4e00\u7801"}

Instead passing `ensure_ascii=False`:

    repair_json("{'test_chinese_ascii':'统一码'}", ensure_ascii=False)

will return

    {"test_chinese_ascii": "统一码"}

### Performance considerations
If you find this library too slow because is using `json.loads()` you can skip that by passing `skip_json_loads=True` to `repair_json`. Like:

    from json_repair import repair_json

    good_json_string = repair_json(bad_json_string, skip_json_loads=True)

I made a choice of not using any fast json library to avoid having any external dependency, so that anybody can use it regardless of their stack.

Some rules of thumb to use:
- Setting `return_objects=True` will always be faster because the parser returns an object already and it doesn't have serialize that object to JSON
- `skip_json_loads` is faster only if you 100% know that the string is not a valid JSON
- If you are having issues with escaping pass the string as **raw** string like: `r"string with escaping\""`

# How it works
This module will parse the JSON file following the BNF definition:

    <json> ::= <primitive> | <container>

    <primitive> ::= <number> | <string> | <boolean>
    ; Where:
    ; <number> is a valid real number expressed in one of a number of given formats
    ; <string> is a string of valid characters enclosed in quotes
    ; <boolean> is one of the literal strings 'true', 'false', or 'null' (unquoted)

    <container> ::= <object> | <array>
    <array> ::= '[' [ <json> *(', ' <json>) ] ']' ; A sequence of JSON values separated by commas
    <object> ::= '{' [ <member> *(', ' <member>) ] '}' ; A sequence of 'members'
    <member> ::= <string> ': ' <json> ; A pair consisting of a name, and a JSON value

If something is wrong (a missing parentheses or quotes for example) it will use a few simple heuristics to fix the JSON string:
- Add the missing parentheses if the parser believes that the array or object should be closed
- Quote strings or add missing single quotes
- Adjust whitespaces and remove line breaks

I am sure some corner cases will be missing, if you have examples please open an issue or even better push a PR