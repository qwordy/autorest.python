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

try:
    from .child_product_py3 import ChildProduct
    from .constant_product_py3 import ConstantProduct
    from .product_py3 import Product
    from .error_py3 import Error, ErrorException
except (SyntaxError, ImportError):
    from .child_product import ChildProduct
    from .constant_product import ConstantProduct
    from .product import Product
    from .error import Error, ErrorException
from .auto_rest_validation_test_enums import (
    EnumConst,
)

__all__ = [
    'ChildProduct',
    'ConstantProduct',
    'Product',
    'Error', 'ErrorException',
    'EnumConst',
]