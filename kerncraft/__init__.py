__version__ = '0.4.10'


def get_header_path():
    import os
    return os.path.abspath(os.path.dirname(os.path.realpath(__file__))) + '/headers/'
