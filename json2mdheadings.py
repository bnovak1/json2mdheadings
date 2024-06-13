"""
A Python package for converting JSON data to Markdown with keys as headings. Since markdown only supports headings up to level 6, this will not work "correctly" for JSON data with more than 6 levels of nesting. Nested lists might be used for JSON data with more than 6 levels of nesting, but this is not currently implemented. For lists of dictionaries, the keys of the dictionaries will not be converted to headings and the list will just be converted to a markdown list. The package is currently intended to be used for JSON data with a maximum of 6 levels of nesting and no lists of dictionaries.
"""

import json

class JSON2MD:
    
    def __init__(self):
        """
        Initializes an instance of the Json2MdHeadings class.

        Attributes:
        - md (str): The Markdown content, initially set to an empty string.
        """
        
        self.md = ""
                    
    def __call__(self, json_file):
            """
            Read in the JSON file. Convert the JSON data to Markdown and write it to a file.

            Parameters:
            - json_file (str): The path to the JSON file to be converted.

            Returns:
            None
            """
            
            md_file = json_file.replace(".json", ".md")
            
            with open(json_file, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            self.json_to_md(data)
            
            with open(md_file, 'w', encoding='utf-8') as file:
                file.write(self.md)

    def json_to_md(self, data, level=1):
        """
        Convert JSON data to Markdown recursively.

        Args:
            data (str): JSON data to convert.
            level (int): JSON key level.

        Returns:
            None

        Raises:
            None
        """
        
        # If data is a dictionary, iterate over the keys.
        if isinstance(data, dict):
            for key in data:
                self.md += f"{'#' * level} {key}\n"
                self.json_to_md(data[key], level + 1)
        
        # If data is a list, write a list in Markdown.
        elif isinstance(data, list):
            self.md += "\n"
            for item in data:
                self.md += f"- {item}\n"
            self.md += "\n"
        
        # Otherwise, write the data in Markdown.
        else:
            self.md += f"\n{data}\n\n"