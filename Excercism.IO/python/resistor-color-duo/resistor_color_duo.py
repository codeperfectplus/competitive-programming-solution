expected = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]
        
def value(colors):
    new_list = []
    for color in colors:
        new_list.append(str(expected.index(color)))
    return int(str(''.join(new_list))[:2])