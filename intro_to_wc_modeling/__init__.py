import pkg_resources

with open(pkg_resources.resource_filename('intro_to_wc_modeling', 'VERSION'), 'r') as file:
    __version__ = file.read().strip()
# :obj:`str`: version
