# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import msrest.serialization


class Paths14Hl8BdFormsdataurlencodedPetAddPetidPostRequestbodyContentApplicationXWwwFormUrlencodedSchema(
    msrest.serialization.Model
):
    """Paths14Hl8BdFormsdataurlencodedPetAddPetidPostRequestbodyContentApplicationXWwwFormUrlencodedSchema.

    All required parameters must be populated in order to send to Azure.

    :param pet_type: Required. Can take a value of dog, or cat, or fish. Possible values include:
     "dog", "cat", "fish".
    :type pet_type: str or ~bodyformurlencodeddata.models.PostContentSchemaPetType
    :param pet_food: Required. Can take a value of meat, or fish, or plant. Possible values
     include: "meat", "fish", "plant".
    :type pet_food: str or ~bodyformurlencodeddata.models.PetFood
    :param pet_age: Required. How many years is it old?.
    :type pet_age: int
    :param name: Updated name of the pet.
    :type name: str
    :param status: Updated status of the pet.
    :type status: str
    """

    _validation = {
        "pet_type": {"required": True},
        "pet_food": {"required": True},
        "pet_age": {"required": True},
    }

    _attribute_map = {
        "pet_type": {"key": "pet_type", "type": "str"},
        "pet_food": {"key": "pet_food", "type": "str"},
        "pet_age": {"key": "pet_age", "type": "int"},
        "name": {"key": "name", "type": "str"},
        "status": {"key": "status", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(
            Paths14Hl8BdFormsdataurlencodedPetAddPetidPostRequestbodyContentApplicationXWwwFormUrlencodedSchema, self
        ).__init__(**kwargs)
        self.pet_type = kwargs["pet_type"]
        self.pet_food = kwargs["pet_food"]
        self.pet_age = kwargs["pet_age"]
        self.name = kwargs.get("name", None)
        self.status = kwargs.get("status", None)
