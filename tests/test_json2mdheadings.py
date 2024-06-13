import pytest
import json
from json2mdheadings import JSON2MD

def test_init():
    converter = JSON2MD()
    assert converter.md == ""

def test_call(tmpdir):
    # Create a temporary JSON file
    p = tmpdir.mkdir("sub").join("test.json")
    p.write('{"title": "Test Title"}')
    converter = JSON2MD()
    converter(str(p))
    assert p.new(ext="md").read() == "# title\n\nTest Title\n\n"

def test_json_to_md():
    
    converter = JSON2MD()

    # Single key-value pair
    converter.json_to_md({"title": "Test Title"}, 1)
    assert converter.md == "# title\n\nTest Title\n\n"
    
    # Multiple key-value pairs
    converter.md = ""
    converter.json_to_md({"title": "Test Title", "author": "Test Author"}, 1)
    assert converter.md == "# title\n\nTest Title\n\n# author\n\nTest Author\n\n"
    
    # Nested dictionary
    converter.md = ""
    converter.json_to_md({"title": "Test Title", "author": {"name": "Test Author"}}, 1)
    assert converter.md == "# title\n\nTest Title\n\n# author\n## name\n\nTest Author\n\n"
    
    # With a list
    converter.md = ""
    converter.json_to_md({"title": "Test Title", "authors": ["Author 1", "Author 2"]}, 1)
    assert converter.md == "# title\n\nTest Title\n\n# authors\n\n- Author 1\n- Author 2\n\n"