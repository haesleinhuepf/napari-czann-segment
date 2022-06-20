# -*- coding: utf-8 -*-

#################################################################
# File        : get_testdata.py
# Author      : sebi06
#
# Disclaimer: This code is purely experimental. Feel free to
# use it at your own risk.
#
#################################################################

import os
import pkg_resources
from napari_czann_segment import utils

PACKAGE_NAME = r"napari_czann_segment"
PACKAGE_DATA = r"_data/"


def get_modelfile(name_czann: str = "PGC_nucleus_detector.czann") -> str:
    """Function to get the path of a CZANN for testing

    Args:
        name_czann (str, optional): Name of the CZANN model. Defaults to "PGC_nucleus_detector.czann".

    Returns:
        str: Absolute path of the CZANN (or CZMODEL) file
    """

    datadir = pkg_resources.resource_filename(PACKAGE_NAME, PACKAGE_DATA)
    czann_file = os.path.join(datadir, name_czann)

    utils.check_file(czann_file)

    return czann_file


def get_czifile(name_czi: str = "PGC_10x_S02.czi") -> str:
    """Function to get the path of a CZI for testing. Lower and upper case are important.

    Args:
        name_czi (str, optional): Name of the CZI file. Defaults to "PGC_10x_S02.czi".

    Returns:
        str: Absolute path of the CZI file
    """

    datadir = pkg_resources.resource_filename(PACKAGE_NAME, PACKAGE_DATA)
    czi_file = os.path.join(datadir, name_czi)

    utils.check_file(czi_file)

    return czi_file
