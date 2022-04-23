from collections import defaultdict

def count_occurrences_function(txt: str):
    """ function to count the occurrence of each character in a string 
    
    Args:
        txt (str): string to be counted
    
    Returns:
        dict: dictionary of characters and their occurrence
    
    Examples:
        >>> count_occurrences_function('a')
        {'a': 1}
        >>> count_occurrences_function('aa')
        {'a': 2}
        >>> count_occurrences_function('aaa')
        {'a': 3}
    """
    output_dict = defaultdict(int)
    txt = txt.lower().replace(' ', '')
    for char in txt:
        output_dict[char] += 1
    
    return output_dict
