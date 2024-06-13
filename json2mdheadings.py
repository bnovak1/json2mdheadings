"""
A Python package for converting JSON data to Markdown with keys as headings up to the 6th level, then using nested lists after that.
"""

import json

class JSON2MD:
    
    def __init__(self, json_file):
        """
        Initializes an instance of the Json2MdHeadings class.

        Parameters:
        - json_file (str): The name of the JSON input file.

        Attributes:
        - json_file (str): The name of the JSON input file.
        - md_file (str): The name of the Markdown output file derived from the JSON file name.
        - md (str): The Markdown content, initially set to an empty string.
        """
        
        self.json_file = json_file
        self.md_file = json_file.replace(".json", ".md")
        self.md = ""
                    
    def __call__(self):
        """
        Read in the JSON file. Convert the JSON data to Markdown and write it to a file.
        """
        
        with open(self.json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        self.json_to_md(data)
        
        with open(self.md_file, 'w', encoding='utf-8') as file:
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
        
        # Otherwise, write the data in Markdown.
        else:
            self.md += f"\n{data}\n"