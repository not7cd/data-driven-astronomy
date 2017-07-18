"""In this module are functions used to describe equatorial coordinates
and convert them to decimal degrees."""
import numpy as np


def angular_dist(ra1, dec1, ra2, dec2):
    """Return angular distance between two points
    """
    [ra1, dec1, ra2, dec2] = np.radians([ra1, dec1, ra2, dec2])
    a = np.sin(np.abs(dec1 - dec2) / 2)**2
    b = np.cos(dec1) * np.cos(dec2) * (np.sin(np.abs(ra1 - ra2) / 2)**2)
    result = 2 * np.arcsin(np.sqrt(a + b))
    return np.degrees(result)


def hms2dec(hours, minutes, seconds):
    """Returns decimal degrees from HMS notation

    Input is expected to be non-negative"""
    # can be 15 * hours + minutes / 4 + seconds / 240
    result = 15 * (hours + minutes / 60 + seconds / 3600)
    return result


def dms2dec(degrees, arcminutes, arcseconds):
    """Returns decimal degrees from DMS notation

    Returns negative value if degrees are negative
    Arcminutes and arcseconds are expected to be non-negative"""
    result = abs(degrees) + arcminutes / 60 + arcseconds / 3600
    return -result if degrees < 0 else result

if __name__ == '__main__':
    # Run your function with the first example in the question.
    print(angular_dist(21.07, 0.1, 21.15, 8.2))

    # Run your function with the second example in the question
    print(angular_dist(10.3, -3, 24.3, -29))

    # The first example from the question
    print(hms2dec(23, 12, 6))

    # The second example from the question
    print(dms2dec(22, 57, 18))

    # The third example from the question
    print(dms2dec(-66, 5, 5.1))
