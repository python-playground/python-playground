# In this file you will find several ways to read
# a file and how to consume a file line by line.

def use_iterator(filepath):
    """Reads a file content line by line file iterator
    which is more efficent for large files. This replaced
    a very old Python syntax .xreadlines(). Every
    line reads from the iterator will contain the newline
    character. To strip, you must do it manually using
    .strip() method on each line as each line is
    returned.
    """
    lines = []
    with open(filepath, "r") as f:
        for line in f:
            lines.append(line)
    return lines

def use_compreh(filepath):
    """Reads a file content and builds the full list
    of lines using list comphrension. This is slightly
    more efficent if the file is small and the list
    is needed immediately. The newline character
    is also not stripped automatically.
    """
    # Always a good idea to define first
    lines = None
    with open(filepath, "r") as f:
        lines = [line for line in f]
    return lines

def use_readlines(filepath):
    """Reads a file content and returns a list
    immediately, but newline character \n is not
    stripped.
    """
    lines = None
    with open(filepath, "r") as f:
        lines = f.readlines()
    return lines

def use_splitlines(filepath):
    """Reads a file content and returns a list
    immediately with the trailing newline
    character stripped autotmatically for you.
    """
    lines = None
    with open(filepath, "r") as f:
        lines = f.read().splitlines()
    return lines

def use_iterator_newlineless(filepath):
    """Similar to use_iterator except the newline
    character is stripped out as each line is
    consumed from the iterator
    """
    lines = []
    with open(filepath, "r") as f:
        for line in f:
            lines.append(line.strip())
    # Note the result may contain empty string
    # in the list IF the original line is just
    # the newline character.
    # See use_iterator_newlineless_fixed
    # and use_read for fixes.
    return lines

def use_iterator_newlineless_fixed(filepath):
    """Similar to use_iterator_newlinesless
    EXCEPT empty strings are filtered out.
    See use_read() function for full details.
    """
    lines = use_iterator_newlineless(filepath)
    return [line for line in lines if line]

def use_read(filepath):
    """Reads the whole file using .read() which
    returns a string. Split line by line using
    the newline character as the delimeter to
    break into lines.
    """
    content = None
    with open(filepath, "r") as f:
        content = f.read()
    # As we split on "\n" for string A\nB,
    # if either A or B is empty, there will be
    # an empty string produced.
    # Take our example.txt:
    #   hello\nworld\n\nlast line\n
    # The split will produce the following list:
    # [hello, world, "", last_line, ""]
    # because between the \n before "last line"
    # is splitted on EMPTY\n"last line\n". We
    # need to filter out these empty strings.
    #
    # The list comprehnsion below does the filtering.
    # Internally content.split is evaluated first
    # and a list is generated. The list comprehension
    # will append the new newline-less line to the list
    # if the line is not empty.
    return [line for line in content.split("\n") if line]

    # Another way to write the above is
    #lines = content.split("\n")
    #return filter(None, lines)
    #
    # Another way is to first remove the very last \n.
    #content = f.read().rstrip()
    # And then outside the with statement, we can
    #return filter(None, content.split("\n"))
    #
    # Finally, if we expect to see the last element
    # being the *ONLY* an empty string, just slice.
    # return content.split("\n")[:-1]
