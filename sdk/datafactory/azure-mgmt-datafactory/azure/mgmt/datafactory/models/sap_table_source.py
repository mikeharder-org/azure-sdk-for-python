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

from .copy_source import CopySource


class SapTableSource(CopySource):
    """A copy activity source for SAP Table source.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param source_retry_count: Source retry count. Type: integer (or
     Expression with resultType integer).
    :type source_retry_count: object
    :param source_retry_wait: Source retry wait. Type: string (or Expression
     with resultType string), pattern:
     ((\\d+)\\.)?(\\d\\d):(60|([0-5][0-9])):(60|([0-5][0-9])).
    :type source_retry_wait: object
    :param max_concurrent_connections: The maximum concurrent connection count
     for the source data store. Type: integer (or Expression with resultType
     integer).
    :type max_concurrent_connections: object
    :param type: Required. Constant filled by server.
    :type type: str
    :param row_count: The number of rows to be retrieved. Type: integer(or
     Expression with resultType integer).
    :type row_count: object
    :param row_skips: The number of rows that will be skipped. Type: integer
     (or Expression with resultType integer).
    :type row_skips: object
    :param rfc_table_fields: The fields of the SAP table that will be
     retrieved. For example, column0, column1. Type: string (or Expression with
     resultType string).
    :type rfc_table_fields: object
    :param rfc_table_options: The options for the filtering of the SAP Table.
     For example, COLUMN0 EQ SOME VALUE. Type: string (or Expression with
     resultType string).
    :type rfc_table_options: object
    :param batch_size: Specifies the maximum number of rows that will be
     retrieved at a time when retrieving data from SAP Table. Type: integer (or
     Expression with resultType integer).
    :type batch_size: object
    :param custom_rfc_read_table_function_module: Specifies the custom RFC
     function module that will be used to read data from SAP Table. Type:
     string (or Expression with resultType string).
    :type custom_rfc_read_table_function_module: object
    :param partition_option: The partition mechanism that will be used for SAP
     table read in parallel. Possible values include: 'None', 'PartitionOnInt',
     'PartitionOnCalendarYear', 'PartitionOnCalendarMonth',
     'PartitionOnCalendarDate'
    :type partition_option: str or
     ~azure.mgmt.datafactory.models.SapTablePartitionOption
    :param partition_settings: The settings that will be leveraged for SAP
     table source partitioning.
    :type partition_settings:
     ~azure.mgmt.datafactory.models.SapTablePartitionSettings
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'source_retry_count': {'key': 'sourceRetryCount', 'type': 'object'},
        'source_retry_wait': {'key': 'sourceRetryWait', 'type': 'object'},
        'max_concurrent_connections': {'key': 'maxConcurrentConnections', 'type': 'object'},
        'type': {'key': 'type', 'type': 'str'},
        'row_count': {'key': 'rowCount', 'type': 'object'},
        'row_skips': {'key': 'rowSkips', 'type': 'object'},
        'rfc_table_fields': {'key': 'rfcTableFields', 'type': 'object'},
        'rfc_table_options': {'key': 'rfcTableOptions', 'type': 'object'},
        'batch_size': {'key': 'batchSize', 'type': 'object'},
        'custom_rfc_read_table_function_module': {'key': 'customRfcReadTableFunctionModule', 'type': 'object'},
        'partition_option': {'key': 'partitionOption', 'type': 'str'},
        'partition_settings': {'key': 'partitionSettings', 'type': 'SapTablePartitionSettings'},
    }

    def __init__(self, **kwargs):
        super(SapTableSource, self).__init__(**kwargs)
        self.row_count = kwargs.get('row_count', None)
        self.row_skips = kwargs.get('row_skips', None)
        self.rfc_table_fields = kwargs.get('rfc_table_fields', None)
        self.rfc_table_options = kwargs.get('rfc_table_options', None)
        self.batch_size = kwargs.get('batch_size', None)
        self.custom_rfc_read_table_function_module = kwargs.get('custom_rfc_read_table_function_module', None)
        self.partition_option = kwargs.get('partition_option', None)
        self.partition_settings = kwargs.get('partition_settings', None)
        self.type = 'SapTableSource'
