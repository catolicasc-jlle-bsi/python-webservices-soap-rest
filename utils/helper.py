

def is_number(content):
    try:
        float(content)
        return True
    except ValueError:
        pass
    return False