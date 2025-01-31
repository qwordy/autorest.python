# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import Any, Dict, List, Optional, Union

from azure.core.exceptions import HttpResponseError
import msrest.serialization

from ._auto_rest_complex_test_service_enums import *


class ArrayWrapper(msrest.serialization.Model):
    """ArrayWrapper.

    :param array:
    :type array: list[str]
    """

    _attribute_map = {
        "array": {"key": "array", "type": "[str]"},
    }

    def __init__(self, *, array: Optional[List[str]] = None, **kwargs):
        super(ArrayWrapper, self).__init__(**kwargs)
        self.array = array


class Basic(msrest.serialization.Model):
    """Basic.

    :param id: Basic Id.
    :type id: int
    :param name: Name property with a very long description that does not fit on a single line and
     a line break.
    :type name: str
    :param color:  Possible values include: "cyan", "Magenta", "YELLOW", "blacK".
    :type color: str or ~bodycomplex.models.CMYKColors
    """

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
        "color": {"key": "color", "type": "str"},
    }

    def __init__(
        self,
        *,
        id: Optional[int] = None,
        name: Optional[str] = None,
        color: Optional[Union[str, "CMYKColors"]] = None,
        **kwargs
    ):
        super(Basic, self).__init__(**kwargs)
        self.id = id
        self.name = name
        self.color = color


class BooleanWrapper(msrest.serialization.Model):
    """BooleanWrapper.

    :param field_true:
    :type field_true: bool
    :param field_false:
    :type field_false: bool
    """

    _attribute_map = {
        "field_true": {"key": "field_true", "type": "bool"},
        "field_false": {"key": "field_false", "type": "bool"},
    }

    def __init__(self, *, field_true: Optional[bool] = None, field_false: Optional[bool] = None, **kwargs):
        super(BooleanWrapper, self).__init__(**kwargs)
        self.field_true = field_true
        self.field_false = field_false


class ByteWrapper(msrest.serialization.Model):
    """ByteWrapper.

    :param field:
    :type field: bytearray
    """

    _attribute_map = {
        "field": {"key": "field", "type": "bytearray"},
    }

    def __init__(self, *, field: Optional[bytearray] = None, **kwargs):
        super(ByteWrapper, self).__init__(**kwargs)
        self.field = field


class Pet(msrest.serialization.Model):
    """Pet.

    :param id:
    :type id: int
    :param name:
    :type name: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
    }

    def __init__(self, *, id: Optional[int] = None, name: Optional[str] = None, **kwargs):
        super(Pet, self).__init__(**kwargs)
        self.id = id
        self.name = name


class Cat(Pet):
    """Cat.

    :param id:
    :type id: int
    :param name:
    :type name: str
    :param color:
    :type color: str
    :param hates:
    :type hates: list[~bodycomplex.models.Dog]
    """

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
        "color": {"key": "color", "type": "str"},
        "hates": {"key": "hates", "type": "[Dog]"},
    }

    def __init__(
        self,
        *,
        id: Optional[int] = None,
        name: Optional[str] = None,
        color: Optional[str] = None,
        hates: Optional[List["Dog"]] = None,
        **kwargs
    ):
        super(Cat, self).__init__(id=id, name=name, **kwargs)
        self.color = color
        self.hates = hates


class Fish(msrest.serialization.Model):
    """Fish.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: Salmon, Shark.

    All required parameters must be populated in order to send to Azure.

    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    """

    _validation = {
        "fishtype": {"required": True},
        "length": {"required": True},
    }

    _attribute_map = {
        "fishtype": {"key": "fishtype", "type": "str"},
        "species": {"key": "species", "type": "str"},
        "length": {"key": "length", "type": "float"},
        "siblings": {"key": "siblings", "type": "[Fish]"},
    }

    _subtype_map = {"fishtype": {"salmon": "Salmon", "shark": "Shark"}}

    def __init__(
        self, *, length: float, species: Optional[str] = None, siblings: Optional[List["Fish"]] = None, **kwargs
    ):
        super(Fish, self).__init__(**kwargs)
        self.fishtype = None  # type: Optional[str]
        self.species = species
        self.length = length
        self.siblings = siblings


class Shark(Fish):
    """Shark.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: Cookiecuttershark, Goblinshark, Sawshark.

    All required parameters must be populated in order to send to Azure.

    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    :param age:
    :type age: int
    :param birthday: Required.
    :type birthday: ~datetime.datetime
    """

    _validation = {
        "fishtype": {"required": True},
        "length": {"required": True},
        "birthday": {"required": True},
    }

    _attribute_map = {
        "fishtype": {"key": "fishtype", "type": "str"},
        "species": {"key": "species", "type": "str"},
        "length": {"key": "length", "type": "float"},
        "siblings": {"key": "siblings", "type": "[Fish]"},
        "age": {"key": "age", "type": "int"},
        "birthday": {"key": "birthday", "type": "iso-8601"},
    }

    _subtype_map = {
        "fishtype": {"cookiecuttershark": "Cookiecuttershark", "goblin": "Goblinshark", "sawshark": "Sawshark"}
    }

    def __init__(
        self,
        *,
        length: float,
        birthday: datetime.datetime,
        species: Optional[str] = None,
        siblings: Optional[List["Fish"]] = None,
        age: Optional[int] = None,
        **kwargs
    ):
        super(Shark, self).__init__(species=species, length=length, siblings=siblings, **kwargs)
        self.fishtype = "shark"  # type: str
        self.age = age
        self.birthday = birthday


class Cookiecuttershark(Shark):
    """Cookiecuttershark.

    All required parameters must be populated in order to send to Azure.

    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    :param age:
    :type age: int
    :param birthday: Required.
    :type birthday: ~datetime.datetime
    """

    _validation = {
        "fishtype": {"required": True},
        "length": {"required": True},
        "birthday": {"required": True},
    }

    _attribute_map = {
        "fishtype": {"key": "fishtype", "type": "str"},
        "species": {"key": "species", "type": "str"},
        "length": {"key": "length", "type": "float"},
        "siblings": {"key": "siblings", "type": "[Fish]"},
        "age": {"key": "age", "type": "int"},
        "birthday": {"key": "birthday", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        length: float,
        birthday: datetime.datetime,
        species: Optional[str] = None,
        siblings: Optional[List["Fish"]] = None,
        age: Optional[int] = None,
        **kwargs
    ):
        super(Cookiecuttershark, self).__init__(
            species=species, length=length, siblings=siblings, age=age, birthday=birthday, **kwargs
        )
        self.fishtype = "cookiecuttershark"  # type: str


class Datetimerfc1123Wrapper(msrest.serialization.Model):
    """Datetimerfc1123Wrapper.

    :param field:
    :type field: ~datetime.datetime
    :param now:
    :type now: ~datetime.datetime
    """

    _attribute_map = {
        "field": {"key": "field", "type": "rfc-1123"},
        "now": {"key": "now", "type": "rfc-1123"},
    }

    def __init__(self, *, field: Optional[datetime.datetime] = None, now: Optional[datetime.datetime] = None, **kwargs):
        super(Datetimerfc1123Wrapper, self).__init__(**kwargs)
        self.field = field
        self.now = now


class DatetimeWrapper(msrest.serialization.Model):
    """DatetimeWrapper.

    :param field:
    :type field: ~datetime.datetime
    :param now:
    :type now: ~datetime.datetime
    """

    _attribute_map = {
        "field": {"key": "field", "type": "iso-8601"},
        "now": {"key": "now", "type": "iso-8601"},
    }

    def __init__(self, *, field: Optional[datetime.datetime] = None, now: Optional[datetime.datetime] = None, **kwargs):
        super(DatetimeWrapper, self).__init__(**kwargs)
        self.field = field
        self.now = now


class DateWrapper(msrest.serialization.Model):
    """DateWrapper.

    :param field:
    :type field: ~datetime.date
    :param leap:
    :type leap: ~datetime.date
    """

    _attribute_map = {
        "field": {"key": "field", "type": "date"},
        "leap": {"key": "leap", "type": "date"},
    }

    def __init__(self, *, field: Optional[datetime.date] = None, leap: Optional[datetime.date] = None, **kwargs):
        super(DateWrapper, self).__init__(**kwargs)
        self.field = field
        self.leap = leap


class DictionaryWrapper(msrest.serialization.Model):
    """DictionaryWrapper.

    :param default_program: Dictionary of :code:`<string>`.
    :type default_program: dict[str, str]
    """

    _attribute_map = {
        "default_program": {"key": "defaultProgram", "type": "{str}"},
    }

    def __init__(self, *, default_program: Optional[Dict[str, str]] = None, **kwargs):
        super(DictionaryWrapper, self).__init__(**kwargs)
        self.default_program = default_program


class Dog(Pet):
    """Dog.

    :param id:
    :type id: int
    :param name:
    :type name: str
    :param food:
    :type food: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
        "food": {"key": "food", "type": "str"},
    }

    def __init__(self, *, id: Optional[int] = None, name: Optional[str] = None, food: Optional[str] = None, **kwargs):
        super(Dog, self).__init__(id=id, name=name, **kwargs)
        self.food = food


class DotFish(msrest.serialization.Model):
    """DotFish.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: DotSalmon.

    All required parameters must be populated in order to send to Azure.

    :param fish_type: Required. Constant filled by server.
    :type fish_type: str
    :param species:
    :type species: str
    """

    _validation = {
        "fish_type": {"required": True},
    }

    _attribute_map = {
        "fish_type": {"key": "fish\\.type", "type": "str"},
        "species": {"key": "species", "type": "str"},
    }

    _subtype_map = {"fish_type": {"DotSalmon": "DotSalmon"}}

    def __init__(self, *, species: Optional[str] = None, **kwargs):
        super(DotFish, self).__init__(**kwargs)
        self.fish_type = None  # type: Optional[str]
        self.species = species


class DotFishMarket(msrest.serialization.Model):
    """DotFishMarket.

    :param sample_salmon:
    :type sample_salmon: ~bodycomplex.models.DotSalmon
    :param salmons:
    :type salmons: list[~bodycomplex.models.DotSalmon]
    :param sample_fish:
    :type sample_fish: ~bodycomplex.models.DotFish
    :param fishes:
    :type fishes: list[~bodycomplex.models.DotFish]
    """

    _attribute_map = {
        "sample_salmon": {"key": "sampleSalmon", "type": "DotSalmon"},
        "salmons": {"key": "salmons", "type": "[DotSalmon]"},
        "sample_fish": {"key": "sampleFish", "type": "DotFish"},
        "fishes": {"key": "fishes", "type": "[DotFish]"},
    }

    def __init__(
        self,
        *,
        sample_salmon: Optional["DotSalmon"] = None,
        salmons: Optional[List["DotSalmon"]] = None,
        sample_fish: Optional["DotFish"] = None,
        fishes: Optional[List["DotFish"]] = None,
        **kwargs
    ):
        super(DotFishMarket, self).__init__(**kwargs)
        self.sample_salmon = sample_salmon
        self.salmons = salmons
        self.sample_fish = sample_fish
        self.fishes = fishes


class DotSalmon(DotFish):
    """DotSalmon.

    All required parameters must be populated in order to send to Azure.

    :param fish_type: Required. Constant filled by server.
    :type fish_type: str
    :param species:
    :type species: str
    :param location:
    :type location: str
    :param iswild:
    :type iswild: bool
    """

    _validation = {
        "fish_type": {"required": True},
    }

    _attribute_map = {
        "fish_type": {"key": "fish\\.type", "type": "str"},
        "species": {"key": "species", "type": "str"},
        "location": {"key": "location", "type": "str"},
        "iswild": {"key": "iswild", "type": "bool"},
    }

    def __init__(
        self, *, species: Optional[str] = None, location: Optional[str] = None, iswild: Optional[bool] = None, **kwargs
    ):
        super(DotSalmon, self).__init__(species=species, **kwargs)
        self.fish_type = "DotSalmon"  # type: str
        self.location = location
        self.iswild = iswild


class DoubleWrapper(msrest.serialization.Model):
    """DoubleWrapper.

    :param field1:
    :type field1: float
    :param
     field56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose:
    :type
     field56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose:
     float
    """

    _attribute_map = {
        "field1": {"key": "field1", "type": "float"},
        "field56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose": {
            "key": "field_56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose",
            "type": "float",
        },
    }

    def __init__(
        self,
        *,
        field1: Optional[float] = None,
        field56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose: Optional[
            float
        ] = None,
        **kwargs
    ):
        super(DoubleWrapper, self).__init__(**kwargs)
        self.field1 = field1
        self.field56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose = (
            field56_zeros_after_the_dot_and_negative_zero_before_dot_and_this_is_a_long_field_name_on_purpose
        )


class DurationWrapper(msrest.serialization.Model):
    """DurationWrapper.

    :param field:
    :type field: ~datetime.timedelta
    """

    _attribute_map = {
        "field": {"key": "field", "type": "duration"},
    }

    def __init__(self, *, field: Optional[datetime.timedelta] = None, **kwargs):
        super(DurationWrapper, self).__init__(**kwargs)
        self.field = field


class Error(msrest.serialization.Model):
    """Error.

    :param status:
    :type status: int
    :param message:
    :type message: str
    """

    _attribute_map = {
        "status": {"key": "status", "type": "int"},
        "message": {"key": "message", "type": "str"},
    }

    def __init__(self, *, status: Optional[int] = None, message: Optional[str] = None, **kwargs):
        super(Error, self).__init__(**kwargs)
        self.status = status
        self.message = message


class FloatWrapper(msrest.serialization.Model):
    """FloatWrapper.

    :param field1:
    :type field1: float
    :param field2:
    :type field2: float
    """

    _attribute_map = {
        "field1": {"key": "field1", "type": "float"},
        "field2": {"key": "field2", "type": "float"},
    }

    def __init__(self, *, field1: Optional[float] = None, field2: Optional[float] = None, **kwargs):
        super(FloatWrapper, self).__init__(**kwargs)
        self.field1 = field1
        self.field2 = field2


class Goblinshark(Shark):
    """Goblinshark.

    All required parameters must be populated in order to send to Azure.

    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    :param age:
    :type age: int
    :param birthday: Required.
    :type birthday: ~datetime.datetime
    :param jawsize:
    :type jawsize: int
    :param color: Colors possible. Possible values include: "pink", "gray", "brown", "RED", "red".
     Default value: "gray".
    :type color: str or ~bodycomplex.models.GoblinSharkColor
    """

    _validation = {
        "fishtype": {"required": True},
        "length": {"required": True},
        "birthday": {"required": True},
    }

    _attribute_map = {
        "fishtype": {"key": "fishtype", "type": "str"},
        "species": {"key": "species", "type": "str"},
        "length": {"key": "length", "type": "float"},
        "siblings": {"key": "siblings", "type": "[Fish]"},
        "age": {"key": "age", "type": "int"},
        "birthday": {"key": "birthday", "type": "iso-8601"},
        "jawsize": {"key": "jawsize", "type": "int"},
        "color": {"key": "color", "type": "str"},
    }

    def __init__(
        self,
        *,
        length: float,
        birthday: datetime.datetime,
        species: Optional[str] = None,
        siblings: Optional[List["Fish"]] = None,
        age: Optional[int] = None,
        jawsize: Optional[int] = None,
        color: Optional[Union[str, "GoblinSharkColor"]] = "gray",
        **kwargs
    ):
        super(Goblinshark, self).__init__(
            species=species, length=length, siblings=siblings, age=age, birthday=birthday, **kwargs
        )
        self.fishtype = "goblin"  # type: str
        self.jawsize = jawsize
        self.color = color


class IntWrapper(msrest.serialization.Model):
    """IntWrapper.

    :param field1:
    :type field1: int
    :param field2:
    :type field2: int
    """

    _attribute_map = {
        "field1": {"key": "field1", "type": "int"},
        "field2": {"key": "field2", "type": "int"},
    }

    def __init__(self, *, field1: Optional[int] = None, field2: Optional[int] = None, **kwargs):
        super(IntWrapper, self).__init__(**kwargs)
        self.field1 = field1
        self.field2 = field2


class LongWrapper(msrest.serialization.Model):
    """LongWrapper.

    :param field1:
    :type field1: long
    :param field2:
    :type field2: long
    """

    _attribute_map = {
        "field1": {"key": "field1", "type": "long"},
        "field2": {"key": "field2", "type": "long"},
    }

    def __init__(self, *, field1: Optional[int] = None, field2: Optional[int] = None, **kwargs):
        super(LongWrapper, self).__init__(**kwargs)
        self.field1 = field1
        self.field2 = field2


class MyBaseType(msrest.serialization.Model):
    """MyBaseType.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: MyDerivedType.

    All required parameters must be populated in order to send to Azure.

    :param kind: Required. Constant filled by server.  Possible values include: "Kind1".
    :type kind: str or ~bodycomplex.models.MyKind
    :param prop_b1:
    :type prop_b1: str
    :param prop_bh1:
    :type prop_bh1: str
    """

    _validation = {
        "kind": {"required": True},
    }

    _attribute_map = {
        "kind": {"key": "kind", "type": "str"},
        "prop_b1": {"key": "propB1", "type": "str"},
        "prop_bh1": {"key": "helper.propBH1", "type": "str"},
    }

    _subtype_map = {"kind": {"Kind1": "MyDerivedType"}}

    def __init__(self, *, prop_b1: Optional[str] = None, prop_bh1: Optional[str] = None, **kwargs):
        super(MyBaseType, self).__init__(**kwargs)
        self.kind = None  # type: Optional[str]
        self.prop_b1 = prop_b1
        self.prop_bh1 = prop_bh1


class MyDerivedType(MyBaseType):
    """MyDerivedType.

    All required parameters must be populated in order to send to Azure.

    :param kind: Required. Constant filled by server.  Possible values include: "Kind1".
    :type kind: str or ~bodycomplex.models.MyKind
    :param prop_b1:
    :type prop_b1: str
    :param prop_bh1:
    :type prop_bh1: str
    :param prop_d1:
    :type prop_d1: str
    """

    _validation = {
        "kind": {"required": True},
    }

    _attribute_map = {
        "kind": {"key": "kind", "type": "str"},
        "prop_b1": {"key": "propB1", "type": "str"},
        "prop_bh1": {"key": "helper.propBH1", "type": "str"},
        "prop_d1": {"key": "propD1", "type": "str"},
    }

    def __init__(
        self, *, prop_b1: Optional[str] = None, prop_bh1: Optional[str] = None, prop_d1: Optional[str] = None, **kwargs
    ):
        super(MyDerivedType, self).__init__(prop_b1=prop_b1, prop_bh1=prop_bh1, **kwargs)
        self.kind = "Kind1"  # type: str
        self.prop_d1 = prop_d1


class ReadonlyObj(msrest.serialization.Model):
    """ReadonlyObj.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id:
    :vartype id: str
    :param size:
    :type size: int
    """

    _validation = {
        "id": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "size": {"key": "size", "type": "int"},
    }

    def __init__(self, *, size: Optional[int] = None, **kwargs):
        super(ReadonlyObj, self).__init__(**kwargs)
        self.id = None
        self.size = size


class Salmon(Fish):
    """Salmon.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: SmartSalmon.

    All required parameters must be populated in order to send to Azure.

    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    :param location:
    :type location: str
    :param iswild:
    :type iswild: bool
    """

    _validation = {
        "fishtype": {"required": True},
        "length": {"required": True},
    }

    _attribute_map = {
        "fishtype": {"key": "fishtype", "type": "str"},
        "species": {"key": "species", "type": "str"},
        "length": {"key": "length", "type": "float"},
        "siblings": {"key": "siblings", "type": "[Fish]"},
        "location": {"key": "location", "type": "str"},
        "iswild": {"key": "iswild", "type": "bool"},
    }

    _subtype_map = {"fishtype": {"smart_salmon": "SmartSalmon"}}

    def __init__(
        self,
        *,
        length: float,
        species: Optional[str] = None,
        siblings: Optional[List["Fish"]] = None,
        location: Optional[str] = None,
        iswild: Optional[bool] = None,
        **kwargs
    ):
        super(Salmon, self).__init__(species=species, length=length, siblings=siblings, **kwargs)
        self.fishtype = "salmon"  # type: str
        self.location = location
        self.iswild = iswild


class Sawshark(Shark):
    """Sawshark.

    All required parameters must be populated in order to send to Azure.

    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    :param age:
    :type age: int
    :param birthday: Required.
    :type birthday: ~datetime.datetime
    :param picture:
    :type picture: bytearray
    """

    _validation = {
        "fishtype": {"required": True},
        "length": {"required": True},
        "birthday": {"required": True},
    }

    _attribute_map = {
        "fishtype": {"key": "fishtype", "type": "str"},
        "species": {"key": "species", "type": "str"},
        "length": {"key": "length", "type": "float"},
        "siblings": {"key": "siblings", "type": "[Fish]"},
        "age": {"key": "age", "type": "int"},
        "birthday": {"key": "birthday", "type": "iso-8601"},
        "picture": {"key": "picture", "type": "bytearray"},
    }

    def __init__(
        self,
        *,
        length: float,
        birthday: datetime.datetime,
        species: Optional[str] = None,
        siblings: Optional[List["Fish"]] = None,
        age: Optional[int] = None,
        picture: Optional[bytearray] = None,
        **kwargs
    ):
        super(Sawshark, self).__init__(
            species=species, length=length, siblings=siblings, age=age, birthday=birthday, **kwargs
        )
        self.fishtype = "sawshark"  # type: str
        self.picture = picture


class Siamese(Cat):
    """Siamese.

    :param id:
    :type id: int
    :param name:
    :type name: str
    :param color:
    :type color: str
    :param hates:
    :type hates: list[~bodycomplex.models.Dog]
    :param breed:
    :type breed: str
    """

    _attribute_map = {
        "id": {"key": "id", "type": "int"},
        "name": {"key": "name", "type": "str"},
        "color": {"key": "color", "type": "str"},
        "hates": {"key": "hates", "type": "[Dog]"},
        "breed": {"key": "breed", "type": "str"},
    }

    def __init__(
        self,
        *,
        id: Optional[int] = None,
        name: Optional[str] = None,
        color: Optional[str] = None,
        hates: Optional[List["Dog"]] = None,
        breed: Optional[str] = None,
        **kwargs
    ):
        super(Siamese, self).__init__(id=id, name=name, color=color, hates=hates, **kwargs)
        self.breed = breed


class SmartSalmon(Salmon):
    """SmartSalmon.

    All required parameters must be populated in order to send to Azure.

    :param fishtype: Required. Constant filled by server.
    :type fishtype: str
    :param species:
    :type species: str
    :param length: Required.
    :type length: float
    :param siblings:
    :type siblings: list[~bodycomplex.models.Fish]
    :param location:
    :type location: str
    :param iswild:
    :type iswild: bool
    :param additional_properties: Unmatched properties from the message are deserialized to this
     collection.
    :type additional_properties: dict[str, any]
    :param college_degree:
    :type college_degree: str
    """

    _validation = {
        "fishtype": {"required": True},
        "length": {"required": True},
    }

    _attribute_map = {
        "fishtype": {"key": "fishtype", "type": "str"},
        "species": {"key": "species", "type": "str"},
        "length": {"key": "length", "type": "float"},
        "siblings": {"key": "siblings", "type": "[Fish]"},
        "location": {"key": "location", "type": "str"},
        "iswild": {"key": "iswild", "type": "bool"},
        "additional_properties": {"key": "", "type": "{object}"},
        "college_degree": {"key": "college_degree", "type": "str"},
    }

    def __init__(
        self,
        *,
        length: float,
        species: Optional[str] = None,
        siblings: Optional[List["Fish"]] = None,
        location: Optional[str] = None,
        iswild: Optional[bool] = None,
        additional_properties: Optional[Dict[str, Any]] = None,
        college_degree: Optional[str] = None,
        **kwargs
    ):
        super(SmartSalmon, self).__init__(
            species=species, length=length, siblings=siblings, location=location, iswild=iswild, **kwargs
        )
        self.fishtype = "smart_salmon"  # type: str
        self.additional_properties = additional_properties
        self.college_degree = college_degree


class StringWrapper(msrest.serialization.Model):
    """StringWrapper.

    :param field:
    :type field: str
    :param empty:
    :type empty: str
    :param null:
    :type null: str
    """

    _attribute_map = {
        "field": {"key": "field", "type": "str"},
        "empty": {"key": "empty", "type": "str"},
        "null": {"key": "null", "type": "str"},
    }

    def __init__(
        self, *, field: Optional[str] = None, empty: Optional[str] = None, null: Optional[str] = None, **kwargs
    ):
        super(StringWrapper, self).__init__(**kwargs)
        self.field = field
        self.empty = empty
        self.null = null
