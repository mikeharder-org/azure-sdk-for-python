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

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class ProductsOperations(object):
    """ProductsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Version of the API to be used with the client request. The current version is 2018-11-01-preview. Constant value: "2018-11-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-11-01-preview"

        self.config = config

    def list_by_billing_account_name(
            self, billing_account_name, filter=None, custom_headers=None, raw=False, **operation_config):
        """Lists products by billing account name.

        :param billing_account_name: billing Account Id.
        :type billing_account_name: str
        :param filter: May be used to filter by product type. The filter
         supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not
         currently support 'ne', 'or', or 'not'. Tag filter is a key value pair
         string where key and value is separated by a colon (:).
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of ProductSummary
        :rtype:
         ~azure.mgmt.billing.models.ProductSummaryPaged[~azure.mgmt.billing.models.ProductSummary]
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list_by_billing_account_name.metadata['url']
                path_format_arguments = {
                    'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
                if filter is not None:
                    query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.ProductSummaryPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.ProductSummaryPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list_by_billing_account_name.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/products'}

    def list_by_invoice_section_name(
            self, billing_account_name, invoice_section_name, filter=None, custom_headers=None, raw=False, **operation_config):
        """Lists products by invoice section name.

        :param billing_account_name: billing Account Id.
        :type billing_account_name: str
        :param invoice_section_name: InvoiceSection Id.
        :type invoice_section_name: str
        :param filter: May be used to filter by product type. The filter
         supports 'eq', 'lt', 'gt', 'le', 'ge', and 'and'. It does not
         currently support 'ne', 'or', or 'not'. Tag filter is a key value pair
         string where key and value is separated by a colon (:).
        :type filter: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ProductsListResult or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.billing.models.ProductsListResult or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.list_by_invoice_section_name.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'invoiceSectionName': self._serialize.url("invoice_section_name", invoice_section_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query("filter", filter, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ProductsListResult', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    list_by_invoice_section_name.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/products'}

    def get(
            self, billing_account_name, invoice_section_name, product_name, custom_headers=None, raw=False, **operation_config):
        """Get a single product by name.

        :param billing_account_name: billing Account Id.
        :type billing_account_name: str
        :param invoice_section_name: InvoiceSection Id.
        :type invoice_section_name: str
        :param product_name: Invoice Id.
        :type product_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ProductSummary or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.billing.models.ProductSummary or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'invoiceSectionName': self._serialize.url("invoice_section_name", invoice_section_name, 'str'),
            'productName': self._serialize.url("product_name", product_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('ProductSummary', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/products/{productName}'}

    def transfer(
            self, billing_account_name, invoice_section_name, product_name, destination_invoice_section_id=None, custom_headers=None, raw=False, **operation_config):
        """The operation to transfer a Product to another invoice section.

        :param billing_account_name: billing Account Id.
        :type billing_account_name: str
        :param invoice_section_name: InvoiceSection Id.
        :type invoice_section_name: str
        :param product_name: Invoice Id.
        :type product_name: str
        :param destination_invoice_section_id: Destination invoice section id.
        :type destination_invoice_section_id: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ProductSummary or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.billing.models.ProductSummary or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        parameters = models.TransferProductRequestProperties(destination_invoice_section_id=destination_invoice_section_id)

        # Construct URL
        url = self.transfer.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'invoiceSectionName': self._serialize.url("invoice_section_name", invoice_section_name, 'str'),
            'productName': self._serialize.url("product_name", product_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(parameters, 'TransferProductRequestProperties')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 202]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('ProductSummary', response)
            header_dict = {
                'Location': 'str',
                'Retry-After': 'int',
                'Azure-AsyncOperation': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    transfer.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/products/{productName}/transfer'}

    def update_auto_renew_by_billing_account_name(
            self, billing_account_name, product_name, auto_renew=None, custom_headers=None, raw=False, **operation_config):
        """Cancel auto renew for product by product id and billing account name.

        :param billing_account_name: billing Account Id.
        :type billing_account_name: str
        :param product_name: Invoice Id.
        :type product_name: str
        :param auto_renew: Request parameters to update auto renew policy a
         product. Possible values include: 'true', 'false'
        :type auto_renew: str or ~azure.mgmt.billing.models.UpdateAutoRenew
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: UpdateAutoRenewOperationSummary or ClientRawResponse if
         raw=true
        :rtype: ~azure.mgmt.billing.models.UpdateAutoRenewOperationSummary or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        body = models.UpdateAutoRenewRequest(auto_renew=auto_renew)

        # Construct URL
        url = self.update_auto_renew_by_billing_account_name.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'productName': self._serialize.url("product_name", product_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(body, 'UpdateAutoRenewRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('UpdateAutoRenewOperationSummary', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_auto_renew_by_billing_account_name.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/products/{productName}/updateAutoRenew'}

    def update_auto_renew_by_invoice_section_name(
            self, billing_account_name, invoice_section_name, product_name, auto_renew=None, custom_headers=None, raw=False, **operation_config):
        """Cancel auto renew for product by product id and invoice section name.

        :param billing_account_name: billing Account Id.
        :type billing_account_name: str
        :param invoice_section_name: InvoiceSection Id.
        :type invoice_section_name: str
        :param product_name: Invoice Id.
        :type product_name: str
        :param auto_renew: Request parameters to update auto renew policy a
         product. Possible values include: 'true', 'false'
        :type auto_renew: str or ~azure.mgmt.billing.models.UpdateAutoRenew
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: UpdateAutoRenewOperationSummary or ClientRawResponse if
         raw=true
        :rtype: ~azure.mgmt.billing.models.UpdateAutoRenewOperationSummary or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<azure.mgmt.billing.models.ErrorResponseException>`
        """
        body = models.UpdateAutoRenewRequest(auto_renew=auto_renew)

        # Construct URL
        url = self.update_auto_renew_by_invoice_section_name.metadata['url']
        path_format_arguments = {
            'billingAccountName': self._serialize.url("billing_account_name", billing_account_name, 'str'),
            'invoiceSectionName': self._serialize.url("invoice_section_name", invoice_section_name, 'str'),
            'productName': self._serialize.url("product_name", product_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct body
        body_content = self._serialize.body(body, 'UpdateAutoRenewRequest')

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters, body_content)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('UpdateAutoRenewOperationSummary', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    update_auto_renew_by_invoice_section_name.metadata = {'url': '/providers/Microsoft.Billing/billingAccounts/{billingAccountName}/invoiceSections/{invoiceSectionName}/products/{productName}/updateAutoRenew'}
