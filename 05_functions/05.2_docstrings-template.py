"""
example credit: https://betterprogramming.pub/3-different-docstring-formats-for-python-d27be81e0d68

Google Docstring Style:
https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

Numpy Docstring Style:
https://numpydoc.readthedocs.io/en/latest/format.html

Sphinx Docstring Style:
https://sphinx-rtd-tutorial.readthedocs.io/en/latest/docstrings.html
"""




# Google Docstring

def add_fn_google_docstrings(num1 : int, num2 : int = 0) -> int:
    """Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Args:
        num1 (int): First number to add.
        num2 (int, optional): Second number to add, default 0.

    Returns:
        int: The sum of ``num1`` and ``num2``.

    Raises:
        AnyError: If anything bad happens.
    
    Examples:
        >>> add_fn_google_docstrings(9, 2)
        11
        >>> add_fn_google_docstrings(93, 0)
        93
        >>> add_fn_google_docstrings(10, -10)
        0
    """
    return num1 + num2



# NumPy Docstring

def add_fn_numpy_docstrings(num1: int, num2: int = 0) -> int:
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int, optional
        Second number to add, default 0.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    Raises
    ------
     MyException
        if anything bad happens.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add_fn_numpy_docstrings(9, 2)
    11
    >>> add_fn_numpy_docstrings(93, 0)
    93
    >>> add_fn_numpy_docstrings(10, -10)
    0
    """
    return num1 + num2



# Sphinx Docstring

def add_sphinx_docstrings(num1, num2) -> int:
    """Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    :param int num1: First number to add.
    :param int num2: Second number to add.
    :returns:  The sum of ``num1`` and ``num2``.
    :rtype: int
    :raises AnyError: If anything bad happens.
    """
    return num1 + num2