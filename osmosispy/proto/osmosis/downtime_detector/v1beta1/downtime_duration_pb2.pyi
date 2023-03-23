"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Downtime:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _DowntimeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Downtime.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    DURATION_30S: _Downtime.ValueType  # 0
    DURATION_1M: _Downtime.ValueType  # 1
    DURATION_2M: _Downtime.ValueType  # 2
    DURATION_3M: _Downtime.ValueType  # 3
    DURATION_4M: _Downtime.ValueType  # 4
    DURATION_5M: _Downtime.ValueType  # 5
    DURATION_10M: _Downtime.ValueType  # 6
    DURATION_20M: _Downtime.ValueType  # 7
    DURATION_30M: _Downtime.ValueType  # 8
    DURATION_40M: _Downtime.ValueType  # 9
    DURATION_50M: _Downtime.ValueType  # 10
    DURATION_1H: _Downtime.ValueType  # 11
    DURATION_1_5H: _Downtime.ValueType  # 12
    DURATION_2H: _Downtime.ValueType  # 13
    DURATION_2_5H: _Downtime.ValueType  # 14
    DURATION_3H: _Downtime.ValueType  # 15
    DURATION_4H: _Downtime.ValueType  # 16
    DURATION_5H: _Downtime.ValueType  # 17
    DURATION_6H: _Downtime.ValueType  # 18
    DURATION_9H: _Downtime.ValueType  # 19
    DURATION_12H: _Downtime.ValueType  # 20
    DURATION_18H: _Downtime.ValueType  # 21
    DURATION_24H: _Downtime.ValueType  # 22
    DURATION_36H: _Downtime.ValueType  # 23
    DURATION_48H: _Downtime.ValueType  # 24

class Downtime(_Downtime, metaclass=_DowntimeEnumTypeWrapper): ...

DURATION_30S: Downtime.ValueType  # 0
DURATION_1M: Downtime.ValueType  # 1
DURATION_2M: Downtime.ValueType  # 2
DURATION_3M: Downtime.ValueType  # 3
DURATION_4M: Downtime.ValueType  # 4
DURATION_5M: Downtime.ValueType  # 5
DURATION_10M: Downtime.ValueType  # 6
DURATION_20M: Downtime.ValueType  # 7
DURATION_30M: Downtime.ValueType  # 8
DURATION_40M: Downtime.ValueType  # 9
DURATION_50M: Downtime.ValueType  # 10
DURATION_1H: Downtime.ValueType  # 11
DURATION_1_5H: Downtime.ValueType  # 12
DURATION_2H: Downtime.ValueType  # 13
DURATION_2_5H: Downtime.ValueType  # 14
DURATION_3H: Downtime.ValueType  # 15
DURATION_4H: Downtime.ValueType  # 16
DURATION_5H: Downtime.ValueType  # 17
DURATION_6H: Downtime.ValueType  # 18
DURATION_9H: Downtime.ValueType  # 19
DURATION_12H: Downtime.ValueType  # 20
DURATION_18H: Downtime.ValueType  # 21
DURATION_24H: Downtime.ValueType  # 22
DURATION_36H: Downtime.ValueType  # 23
DURATION_48H: Downtime.ValueType  # 24
global___Downtime = Downtime