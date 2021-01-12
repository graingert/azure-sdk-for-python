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


class PersonalPreferencesOperationsPayload(Model):
    """Represents payload for any Environment operations like get, start, stop,
    connect.

    :param lab_account_resource_id: Resource Id of the lab account
    :type lab_account_resource_id: str
    :param add_remove: Enum indicating if user is adding or removing a
     favorite lab. Possible values include: 'Add', 'Remove'
    :type add_remove: str or ~azure.mgmt.labservices.models.AddRemove
    :param lab_resource_id: Resource Id of the lab to add/remove from the
     favorites list
    :type lab_resource_id: str
    """

    _attribute_map = {
        'lab_account_resource_id': {'key': 'labAccountResourceId', 'type': 'str'},
        'add_remove': {'key': 'addRemove', 'type': 'str'},
        'lab_resource_id': {'key': 'labResourceId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PersonalPreferencesOperationsPayload, self).__init__(**kwargs)
        self.lab_account_resource_id = kwargs.get('lab_account_resource_id', None)
        self.add_remove = kwargs.get('add_remove', None)
        self.lab_resource_id = kwargs.get('lab_resource_id', None)