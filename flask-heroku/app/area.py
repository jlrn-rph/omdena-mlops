def area_to_acre(length, width):
    '''
    Calculate the length and width of a farmer's field in feet then convert it to acre.

    Input: length and width in feet
    Output: area in acres
    '''

    area = length * width
    acre = area / 43560

    return acre
