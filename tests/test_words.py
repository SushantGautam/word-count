from pathlib import Path
import sys

here = Path(__file__).parent
sys.path.append((here / ".." / "code").as_posix())

from words import find_first_word_that_starts_with

def test_find_first_word_that_starts_with():
    words=["apple", "banana", "cherry", "date", "elderberry"]
    assert find_first_word_that_starts_with(words, "e") == "elderberry"

from count import count_words

def test_count_words():
    text = "apple banana cherry date elderberry"
    assert count_words(text) == {"apple": 1, "banana": 1, "cherry": 1, "date": 1, "elderberry": 1}
    text = "apple banana cherry date elderberry apple banana cherry date elderberry apple banana cherry date elderberry"
    assert count_words(text) == {"apple": 3, "banana": 3, "cherry": 3, "date": 3, "elderberry": 3}