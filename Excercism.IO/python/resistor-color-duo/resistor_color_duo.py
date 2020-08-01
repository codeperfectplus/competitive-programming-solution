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
    list = []
    for color in colors:
        list.append(str(expected.index(color)))
    return int(str(''.join(list))[:2])