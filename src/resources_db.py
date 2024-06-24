# Resource object code (Python 3)
# Created by: object code
# Created by: The Resource Compiler for Qt version 6.5.3
# WARNING! All changes made in this file will be lost!

from PySide6 import QtCore

qt_resource_data = b"\
\x00\x00\x00\x01\
0\
\
"

qt_resource_name = b"\
\x00\x10\
\x01\xdcA4\
\x00o\
\x00r\x00d\x00e\x00r\x00_\x00n\x00u\x00m\x00b\x00e\x00r\x00.\x00t\x00x\x00t\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x8f\x96b\xa2a\
"


def qInitResources():
    QtCore.qRegisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)


def qCleanupResources():
    QtCore.qUnregisterResourceData(0x03, qt_resource_struct, qt_resource_name, qt_resource_data)


qInitResources()
