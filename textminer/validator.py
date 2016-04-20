import re


def binary(t):
    """String must be a binary number."""
    return re.match(r'[01]', t)


def binary_even(t):
    """String must be a binary number and be even."""
    return re.match(r'^[01]+0$', t)


def hex(t):
    return re.match(r'[A-F0-9]+$', t)


def word(t):
    return re.match(r'[a-zA-Z0-9-]*[^\d]$', t)


def words(text, count=None):

    matches = re.findall(r'[a-zA-Z0-9-]*[^\d]', text)

    if count:
        return len(matches) == count

    else:
        return len(matches) > 0


def phone_number(t):
    """US phone numbers only."""
    return re.match(r'\(?[0-9]{3}\)?[-\. ]?[0-9]{3}[-\.]?[0-9]{4}$', t)


def money(t):
    """We are just concerned with dollars here."""
    # money = re.compile('|'.join([
    #   r'^\$?(\.\d{2})$',            # e.g., $.50, .50, $1.50, $.5, .5
    #   r'^\$?(,?[0-9]{3})*',         # e.g., $500, $5, 500, 5
    #   r'^\$([0-9]{1,3})',           # e.g., $5.
    #
    # ]))
    #
    #   r'^\$?(\d*\.\d{1,2})$',  # e.g., $.50, .50, $1.50, $.5, .5
    #   r'^\$?(\d+)$',           # e.g., $500, $5, 500, 5
    #   r'^\$(\d+\.?)$',         # e.g., $5.
    # return money
    return re.match(r'^\$([0-9]{1,3})(,?[0-9]{3})*(\.[0-9]{2})?$', t)


def zipcode(t):
    return re.match(r'(\d{5})(-\d{4})?$', t)


def date(t):
    return re.match(r'(\d{1,2}/\d{1,2}/\d{4})?(\d{4}-\d{2}-\d{2})?$', t)
    # return re.match(r'[0-9]{1,4}[/|-][0-9]{1,4}[/|-]?[0-9]{1,4}$', t)
