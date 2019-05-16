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


class AnalyzeResult(Model):
    """Analyze API call result.

    :param status: Status of the analyze operation. Possible values include:
     'success', 'partialSuccess', 'failure'
    :type status: str or ~azure.cognitiveservices.formrecognizer.models.enum
    :param pages: Page level information extracted in the analyzed
     document.
    :type pages:
     list[~azure.cognitiveservices.formrecognizer.models.ExtractedPage]
    :param errors: List of errors reported during the analyze
     operation.
    :type errors:
     list[~azure.cognitiveservices.formrecognizer.models.FormOperationError]
    """

    _attribute_map = {
        'status': {'key': 'status', 'type': 'str'},
        'pages': {'key': 'pages', 'type': '[ExtractedPage]'},
        'errors': {'key': 'errors', 'type': '[FormOperationError]'},
    }

    def __init__(self, **kwargs):
        super(AnalyzeResult, self).__init__(**kwargs)
        self.status = kwargs.get('status', None)
        self.pages = kwargs.get('pages', None)
        self.errors = kwargs.get('errors', None)