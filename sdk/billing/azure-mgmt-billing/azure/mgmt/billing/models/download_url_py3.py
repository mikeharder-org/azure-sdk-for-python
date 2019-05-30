# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DownloadUrl(Model):
    """A secure URL that can be used to download a an entity until the URL
    expires.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar expiry_time: The time in UTC at which this download URL will expire.
    :vartype expiry_time: datetime
    :ivar url: The URL to the PDF file.
    :vartype url: str
    """

    _validation = {
        'expiry_time': {'readonly': True},
        'url': {'readonly': True},
    }

    _attribute_map = {
        'expiry_time': {'key': 'expiryTime', 'type': 'iso-8601'},
        'url': {'key': 'url', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(DownloadUrl, self).__init__(**kwargs)
        self.expiry_time = None
        self.url = None
