import pytest
import json
from json2mdheadings import JSON2MD

def test_init():
    converter = JSON2MD("test.json")
    assert converter.json_file == "test.json"
    assert converter.md_file == "test.md"
    assert converter.md == ""

def test_call(tmpdir):
    # Create a temporary JSON file
    p = tmpdir.mkdir("sub").join("test.json")
    p.write('{"title": "Test Title"}')
    converter = JSON2MD(str(p))
    converter()
    assert p.new(ext="md").read() == "# title\n\nTest Title\n"

def test_json_to_md():
    
    # Single key-value pair
    converter = JSON2MD("test.json")
    converter.json_to_md({"title": "Test Title"}, 1)
    assert converter.md == "# title\n\nTest Title\n"
    
    # Multiple key-value pairs
    converter = JSON2MD("test.json")
    converter.json_to_md({"title": "Test Title", "author": "Test Author"}, 1)
    assert converter.md == "# title\n\nTest Title\n# author\n\nTest Author\n"
    
    # Nested dictionary
    converter = JSON2MD("test.json")
    converter.json_to_md({"title": "Test Title", "author": {"name": "Test Author"}}, 1)
    assert converter.md == "# title\n\nTest Title\n# author\n## name\n\nTest Author\n"
    
    # With a list
    converter = JSON2MD("test.json")
    converter.json_to_md({"title": "Test Title", "authors": ["Author 1", "Author 2"]}, 1)
    assert converter.md == "# title\n\nTest Title\n# authors\n\n- Author 1\n- Author 2\n"