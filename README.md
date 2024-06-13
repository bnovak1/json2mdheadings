# json2md-headings

A Python package for converting JSON data to Markdown with keys as headings up to the 6th level, then using nested lists after that.

## Installation

You can install json2md-headings using pip:

```shell
pip install json2md-headings
```

## Usage

To use json2md-headings, import the `json2md_headings` module and call the `convert_to_headings` function with your JSON data:

```python
from json2md_headings import convert_to_headings

json_data = {
    "title": "My Document",
    "sections": [
        {
            "title": "Section 1",
            "subsections": [
                {
                    "title": "Subsection 1.1",
                    "content": "Lorem ipsum dolor sit amet."
                },
                {
                    "title": "Subsection 1.2",
                    "content": "Consectetur adipiscing elit."
                }
            ]
        },
        {
            "title": "Section 2",
            "subsections": [
                {
                    "title": "Subsection 2.1",
                    "content": "Sed do eiusmod tempor incididunt."
                },
                {
                    "title": "Subsection 2.2",
                    "content": "Ut labore et dolore magna aliqua."
                }
            ]
        }
    ]
}

markdown = convert_to_headings(json_data)
print(markdown)
```

This will convert the JSON data to Markdown headings and return the result as a string.

## Testing

To run the unit tests for json2md-headings, use the following command:

```shell
python -m unittest discover tests
```

## License

json2md-headings is licensed under the MIT License. See [LICENSE](LICENSE) for more information.