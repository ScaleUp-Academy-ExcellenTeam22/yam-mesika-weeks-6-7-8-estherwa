

def group_by(function, iterable):
    """
    A function that gets an iterable,
    :param function: The function that goes with the iterable.
    :param iterable: The iterable that we use.
    :return: A dictionary whose keys are the values that we get.
    """

    return {function(index): list(filter(lambda term: function(term) == function(index), iterable))for index in iterable}



