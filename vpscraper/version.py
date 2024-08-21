VERSION = (0, 0, 1, '', 1)


def version():
    if VERSION[3] and VERSION[4]:
        return '{0}.{1}.{2}{3}{4}'.format(*VERSION)
    else:
        return '{0}.{1}.{2}'.format(*VERSION[0:3])


NAME = 'VPScraper'
VERSION_EXTRA = ''
LICENSE = 'MIT'
