from tail import Tail

def tail(file, lines=10):
    """
    Test returning the end [x] lines of the file.

    >>> import StringIO
    >>> f = StringIO.StringIO()
    >>> for i in range(10):
    ...     f.write('Line %d\\n' % (i + 1))
    >>> tail(f, 4)
    ['Line 7', 'Line 8', 'Line 9', 'Line 10']
    """
    return Tail(file).tail(lines)

def follow(file, delay=1.0):
    """
    Test following a file.

    >>> import os
    >>> f = file('test_follow.txt', 'w')
    >>> f_r = file('test_follow.txt', 'r')
    >>> generator = follow(f_r)
    >>> f.write('Line 1\\n')
    >>> f.flush()
    >>> generator.next()
    'Line 1'
    >>> f.write('Line 2\\n')
    >>> f.flush()
    >>> generator.next()
    'Line 2'
    >>> f.close()
    >>> f_r.close()
    >>> os.remove('test_follow.txt')
    """
    return Tail(file).follow(delay=delay)

if __name__ == "__main__":
    import doctest
    doctest.testmod()