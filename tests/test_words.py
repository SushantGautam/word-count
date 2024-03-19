from pathlib import Path
import sys

here = Path(__file__).parent
sys.path.append((here / ".." / "code").as_posix())

from words import find_first_word_that_starts_with

def test_find_first_word_that_starts_with():
    words=["apple", "banana", "cherry", "date", "elderberry"]
    assert find_first_word_that_starts_with(words, "a") == "apple"