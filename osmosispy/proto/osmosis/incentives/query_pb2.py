# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: osmosis/incentives/query.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from osmosis.incentives import gauge_pb2 as osmosis_dot_incentives_dot_gauge__pb2
from osmosis.lockup import lock_pb2 as osmosis_dot_lockup_dot_lock__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eosmosis/incentives/query.proto\x12\x12osmosis.incentives\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1eosmosis/incentives/gauge.proto\x1a\x19osmosis/lockup/lock.proto\" \n\x1eModuleToDistributeCoinsRequest\"}\n\x1fModuleToDistributeCoinsResponse\x12Z\n\x05\x63oins\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"\x1e\n\x10GaugeByIDRequest\x12\n\n\x02id\x18\x01 \x01(\x04\"=\n\x11GaugeByIDResponse\x12(\n\x05gauge\x18\x01 \x01(\x0b\x32\x19.osmosis.incentives.Gauge\"K\n\rGaugesRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"|\n\x0eGaugesResponse\x12-\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"Q\n\x13\x41\x63tiveGaugesRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x82\x01\n\x14\x41\x63tiveGaugesResponse\x12-\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"h\n\x1b\x41\x63tiveGaugesPerDenomRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x8a\x01\n\x1c\x41\x63tiveGaugesPerDenomResponse\x12-\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"S\n\x15UpcomingGaugesRequest\x12:\n\npagination\x18\x01 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x84\x01\n\x16UpcomingGaugesResponse\x12-\n\x04\x64\x61ta\x18\x01 \x03(\x0b\x32\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"j\n\x1dUpcomingGaugesPerDenomRequest\x12\r\n\x05\x64\x65nom\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b\x32&.cosmos.base.query.v1beta1.PageRequest\"\x97\x01\n\x1eUpcomingGaugesPerDenomResponse\x12\x38\n\x0fupcoming_gauges\x18\x01 \x03(\x0b\x32\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.cosmos.base.query.v1beta1.PageResponse\"Y\n\x11RewardsEstRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:\"owner\"\x12\x10\n\x08lock_ids\x18\x02 \x03(\x04\x12\x11\n\tend_epoch\x18\x03 \x01(\x03\"p\n\x12RewardsEstResponse\x12Z\n\x05\x63oins\x18\x01 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\"\x1f\n\x1dQueryLockableDurationsRequest\"~\n\x1eQueryLockableDurationsResponse\x12\\\n\x12lockable_durations\x18\x01 \x03(\x0b\x32\x19.google.protobuf.DurationB%\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xf2\xde\x1f\x19yaml:\"lockable_durations\"2\xd6\x0b\n\x05Query\x12\xc2\x01\n\x17ModuleToDistributeCoins\x12\x32.osmosis.incentives.ModuleToDistributeCoinsRequest\x1a\x33.osmosis.incentives.ModuleToDistributeCoinsResponse\">\x82\xd3\xe4\x93\x02\x38\x12\x36/osmosis/incentives/v1beta1/module_to_distribute_coins\x12\x8e\x01\n\tGaugeByID\x12$.osmosis.incentives.GaugeByIDRequest\x1a%.osmosis.incentives.GaugeByIDResponse\"4\x82\xd3\xe4\x93\x02.\x12,/osmosis/incentives/v1beta1/gauge_by_id/{id}\x12{\n\x06Gauges\x12!.osmosis.incentives.GaugesRequest\x1a\".osmosis.incentives.GaugesResponse\"*\x82\xd3\xe4\x93\x02$\x12\"/osmosis/incentives/v1beta1/gauges\x12\x94\x01\n\x0c\x41\x63tiveGauges\x12\'.osmosis.incentives.ActiveGaugesRequest\x1a(.osmosis.incentives.ActiveGaugesResponse\"1\x82\xd3\xe4\x93\x02+\x12)/osmosis/incentives/v1beta1/active_gauges\x12\xb6\x01\n\x14\x41\x63tiveGaugesPerDenom\x12/.osmosis.incentives.ActiveGaugesPerDenomRequest\x1a\x30.osmosis.incentives.ActiveGaugesPerDenomResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/osmosis/incentives/v1beta1/active_gauges_per_denom\x12\x9c\x01\n\x0eUpcomingGauges\x12).osmosis.incentives.UpcomingGaugesRequest\x1a*.osmosis.incentives.UpcomingGaugesResponse\"3\x82\xd3\xe4\x93\x02-\x12+/osmosis/incentives/v1beta1/upcoming_gauges\x12\xbe\x01\n\x16UpcomingGaugesPerDenom\x12\x31.osmosis.incentives.UpcomingGaugesPerDenomRequest\x1a\x32.osmosis.incentives.UpcomingGaugesPerDenomResponse\"=\x82\xd3\xe4\x93\x02\x37\x12\x35/osmosis/incentives/v1beta1/upcoming_gauges_per_denom\x12\x94\x01\n\nRewardsEst\x12%.osmosis.incentives.RewardsEstRequest\x1a&.osmosis.incentives.RewardsEstResponse\"7\x82\xd3\xe4\x93\x02\x31\x12//osmosis/incentives/v1beta1/rewards_est/{owner}\x12\xb2\x01\n\x11LockableDurations\x12\x31.osmosis.incentives.QueryLockableDurationsRequest\x1a\x32.osmosis.incentives.QueryLockableDurationsResponse\"6\x82\xd3\xe4\x93\x02\x30\x12./osmosis/incentives/v1beta1/lockable_durationsB8Z6github.com/osmosis-labs/osmosis/v14/x/incentives/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.incentives.query_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6github.com/osmosis-labs/osmosis/v14/x/incentives/types'
  _MODULETODISTRIBUTECOINSRESPONSE.fields_by_name['coins']._options = None
  _MODULETODISTRIBUTECOINSRESPONSE.fields_by_name['coins']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _GAUGESRESPONSE.fields_by_name['data']._options = None
  _GAUGESRESPONSE.fields_by_name['data']._serialized_options = b'\310\336\037\000'
  _ACTIVEGAUGESRESPONSE.fields_by_name['data']._options = None
  _ACTIVEGAUGESRESPONSE.fields_by_name['data']._serialized_options = b'\310\336\037\000'
  _ACTIVEGAUGESPERDENOMRESPONSE.fields_by_name['data']._options = None
  _ACTIVEGAUGESPERDENOMRESPONSE.fields_by_name['data']._serialized_options = b'\310\336\037\000'
  _UPCOMINGGAUGESRESPONSE.fields_by_name['data']._options = None
  _UPCOMINGGAUGESRESPONSE.fields_by_name['data']._serialized_options = b'\310\336\037\000'
  _UPCOMINGGAUGESPERDENOMRESPONSE.fields_by_name['upcoming_gauges']._options = None
  _UPCOMINGGAUGESPERDENOMRESPONSE.fields_by_name['upcoming_gauges']._serialized_options = b'\310\336\037\000'
  _REWARDSESTREQUEST.fields_by_name['owner']._options = None
  _REWARDSESTREQUEST.fields_by_name['owner']._serialized_options = b'\362\336\037\014yaml:\"owner\"'
  _REWARDSESTRESPONSE.fields_by_name['coins']._options = None
  _REWARDSESTRESPONSE.fields_by_name['coins']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _QUERYLOCKABLEDURATIONSRESPONSE.fields_by_name['lockable_durations']._options = None
  _QUERYLOCKABLEDURATIONSRESPONSE.fields_by_name['lockable_durations']._serialized_options = b'\310\336\037\000\230\337\037\001\362\336\037\031yaml:\"lockable_durations\"'
  _QUERY.methods_by_name['ModuleToDistributeCoins']._options = None
  _QUERY.methods_by_name['ModuleToDistributeCoins']._serialized_options = b'\202\323\344\223\0028\0226/osmosis/incentives/v1beta1/module_to_distribute_coins'
  _QUERY.methods_by_name['GaugeByID']._options = None
  _QUERY.methods_by_name['GaugeByID']._serialized_options = b'\202\323\344\223\002.\022,/osmosis/incentives/v1beta1/gauge_by_id/{id}'
  _QUERY.methods_by_name['Gauges']._options = None
  _QUERY.methods_by_name['Gauges']._serialized_options = b'\202\323\344\223\002$\022\"/osmosis/incentives/v1beta1/gauges'
  _QUERY.methods_by_name['ActiveGauges']._options = None
  _QUERY.methods_by_name['ActiveGauges']._serialized_options = b'\202\323\344\223\002+\022)/osmosis/incentives/v1beta1/active_gauges'
  _QUERY.methods_by_name['ActiveGaugesPerDenom']._options = None
  _QUERY.methods_by_name['ActiveGaugesPerDenom']._serialized_options = b'\202\323\344\223\0025\0223/osmosis/incentives/v1beta1/active_gauges_per_denom'
  _QUERY.methods_by_name['UpcomingGauges']._options = None
  _QUERY.methods_by_name['UpcomingGauges']._serialized_options = b'\202\323\344\223\002-\022+/osmosis/incentives/v1beta1/upcoming_gauges'
  _QUERY.methods_by_name['UpcomingGaugesPerDenom']._options = None
  _QUERY.methods_by_name['UpcomingGaugesPerDenom']._serialized_options = b'\202\323\344\223\0027\0225/osmosis/incentives/v1beta1/upcoming_gauges_per_denom'
  _QUERY.methods_by_name['RewardsEst']._options = None
  _QUERY.methods_by_name['RewardsEst']._serialized_options = b'\202\323\344\223\0021\022//osmosis/incentives/v1beta1/rewards_est/{owner}'
  _QUERY.methods_by_name['LockableDurations']._options = None
  _QUERY.methods_by_name['LockableDurations']._serialized_options = b'\202\323\344\223\0020\022./osmosis/incentives/v1beta1/lockable_durations'
  _MODULETODISTRIBUTECOINSREQUEST._serialized_start=273
  _MODULETODISTRIBUTECOINSREQUEST._serialized_end=305
  _MODULETODISTRIBUTECOINSRESPONSE._serialized_start=307
  _MODULETODISTRIBUTECOINSRESPONSE._serialized_end=432
  _GAUGEBYIDREQUEST._serialized_start=434
  _GAUGEBYIDREQUEST._serialized_end=464
  _GAUGEBYIDRESPONSE._serialized_start=466
  _GAUGEBYIDRESPONSE._serialized_end=527
  _GAUGESREQUEST._serialized_start=529
  _GAUGESREQUEST._serialized_end=604
  _GAUGESRESPONSE._serialized_start=606
  _GAUGESRESPONSE._serialized_end=730
  _ACTIVEGAUGESREQUEST._serialized_start=732
  _ACTIVEGAUGESREQUEST._serialized_end=813
  _ACTIVEGAUGESRESPONSE._serialized_start=816
  _ACTIVEGAUGESRESPONSE._serialized_end=946
  _ACTIVEGAUGESPERDENOMREQUEST._serialized_start=948
  _ACTIVEGAUGESPERDENOMREQUEST._serialized_end=1052
  _ACTIVEGAUGESPERDENOMRESPONSE._serialized_start=1055
  _ACTIVEGAUGESPERDENOMRESPONSE._serialized_end=1193
  _UPCOMINGGAUGESREQUEST._serialized_start=1195
  _UPCOMINGGAUGESREQUEST._serialized_end=1278
  _UPCOMINGGAUGESRESPONSE._serialized_start=1281
  _UPCOMINGGAUGESRESPONSE._serialized_end=1413
  _UPCOMINGGAUGESPERDENOMREQUEST._serialized_start=1415
  _UPCOMINGGAUGESPERDENOMREQUEST._serialized_end=1521
  _UPCOMINGGAUGESPERDENOMRESPONSE._serialized_start=1524
  _UPCOMINGGAUGESPERDENOMRESPONSE._serialized_end=1675
  _REWARDSESTREQUEST._serialized_start=1677
  _REWARDSESTREQUEST._serialized_end=1766
  _REWARDSESTRESPONSE._serialized_start=1768
  _REWARDSESTRESPONSE._serialized_end=1880
  _QUERYLOCKABLEDURATIONSREQUEST._serialized_start=1882
  _QUERYLOCKABLEDURATIONSREQUEST._serialized_end=1913
  _QUERYLOCKABLEDURATIONSRESPONSE._serialized_start=1915
  _QUERYLOCKABLEDURATIONSRESPONSE._serialized_end=2041
  _QUERY._serialized_start=2044
  _QUERY._serialized_end=3538
# @@protoc_insertion_point(module_scope)