# VPScraper
# Copyright 2022-2022 Vinson Phoan
# See LICENSE for details.

class VPScraperException(Exception):
    """Base exception for VPScraper
    .. versioned:: 0.1
    """
    pass


class ClientException(VPScraperException):
    pass
