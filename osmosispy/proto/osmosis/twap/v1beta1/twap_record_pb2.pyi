"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class TwapRecord(google.protobuf.message.Message):
    """A TWAP record should be indexed in state by pool_id, (asset pair), timestamp
    The asset pair assets should be lexicographically sorted.
    Technically (pool_id, asset_0_denom, asset_1_denom, height) do not need to
    appear in the struct however we view this as the wrong performance tradeoff
    given SDK today. Would rather we optimize for readability and correctness,
    than an optimal state storage format. The system bottleneck is elsewhere for
    now.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POOL_ID_FIELD_NUMBER: builtins.int
    ASSET0_DENOM_FIELD_NUMBER: builtins.int
    ASSET1_DENOM_FIELD_NUMBER: builtins.int
    HEIGHT_FIELD_NUMBER: builtins.int
    TIME_FIELD_NUMBER: builtins.int
    P0_LAST_SPOT_PRICE_FIELD_NUMBER: builtins.int
    P1_LAST_SPOT_PRICE_FIELD_NUMBER: builtins.int
    P0_ARITHMETIC_TWAP_ACCUMULATOR_FIELD_NUMBER: builtins.int
    P1_ARITHMETIC_TWAP_ACCUMULATOR_FIELD_NUMBER: builtins.int
    GEOMETRIC_TWAP_ACCUMULATOR_FIELD_NUMBER: builtins.int
    LAST_ERROR_TIME_FIELD_NUMBER: builtins.int
    pool_id: builtins.int
    asset0_denom: builtins.str
    """Lexicographically smaller denom of the pair"""
    asset1_denom: builtins.str
    """Lexicographically larger denom of the pair"""
    height: builtins.int
    """height this record corresponds to, for debugging purposes"""
    @property
    def time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """This field should only exist until we have a global registry in the state
        machine, mapping prior block heights within {TIME RANGE} to times.
        """
    p0_last_spot_price: builtins.str
    """We store the last spot prices in the struct, so that we can interpolate
    accumulator values for times between when accumulator records are stored.
    """
    p1_last_spot_price: builtins.str
    p0_arithmetic_twap_accumulator: builtins.str
    p1_arithmetic_twap_accumulator: builtins.str
    geometric_twap_accumulator: builtins.str
    @property
    def last_error_time(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """This field contains the time in which the last spot price error occured.
        It is used to alert the caller if they are getting a potentially erroneous
        TWAP, due to an unforeseen underlying error.
        """
    def __init__(
        self,
        *,
        pool_id: builtins.int = ...,
        asset0_denom: builtins.str = ...,
        asset1_denom: builtins.str = ...,
        height: builtins.int = ...,
        time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        p0_last_spot_price: builtins.str = ...,
        p1_last_spot_price: builtins.str = ...,
        p0_arithmetic_twap_accumulator: builtins.str = ...,
        p1_arithmetic_twap_accumulator: builtins.str = ...,
        geometric_twap_accumulator: builtins.str = ...,
        last_error_time: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["last_error_time", b"last_error_time", "time", b"time"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["asset0_denom", b"asset0_denom", "asset1_denom", b"asset1_denom", "geometric_twap_accumulator", b"geometric_twap_accumulator", "height", b"height", "last_error_time", b"last_error_time", "p0_arithmetic_twap_accumulator", b"p0_arithmetic_twap_accumulator", "p0_last_spot_price", b"p0_last_spot_price", "p1_arithmetic_twap_accumulator", b"p1_arithmetic_twap_accumulator", "p1_last_spot_price", b"p1_last_spot_price", "pool_id", b"pool_id", "time", b"time"]) -> None: ...

global___TwapRecord = TwapRecord