import os
from typing import List
def find_first_word_that_starts_with(word_list: List[str], starts_with: str) -> str:
    """Find the first word in the list that starts with the given string."""
    for word in word_list:
        if word.startswith(starts_with):
            return word
    return None