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


class OperationStatus(Model):
    """status of the Billing POST/PUT operation.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: The operation Id.
    :vartype id: str
    :param status: Status of the pending operation
    :type status: str
    :param status_detail: Status Detail of the pending operation
    :type status_detail: str
    """

    _validation = {
        'id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'status_detail': {'key': 'statusDetail', 'type': 'str'},
    }

    def __init__(self, *, status: str=None, status_detail: str=None, **kwargs) -> None:
        super(OperationStatus, self).__init__(**kwargs)
        self.id = None
        self.status = status
        self.status_detail = status_detail
