# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: osmosis/superfluid/tx.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from osmosis.superfluid import superfluid_pb2 as osmosis_dot_superfluid_dot_superfluid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bosmosis/superfluid/tx.proto\x12\x12osmosis.superfluid\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1e\x63osmos/base/v1beta1/coin.proto\x1a#osmosis/superfluid/superfluid.proto\"]\n\x15MsgSuperfluidDelegate\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12\x0f\n\x07lock_id\x18\x02 \x01(\x04\x12\x10\n\x08val_addr\x18\x03 \x01(\t\"\x1f\n\x1dMsgSuperfluidDelegateResponse\"M\n\x17MsgSuperfluidUndelegate\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12\x0f\n\x07lock_id\x18\x02 \x01(\x04\"!\n\x1fMsgSuperfluidUndelegateResponse\"M\n\x17MsgSuperfluidUnbondLock\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12\x0f\n\x07lock_id\x18\x02 \x01(\x04\"!\n\x1fMsgSuperfluidUnbondLockResponse\"\xaf\x01\n\x1cMsgLockAndSuperfluidDelegate\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12Z\n\x05\x63oins\x18\x02 \x03(\x0b\x32\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12\x10\n\x08val_addr\x18\x03 \x01(\t\"2\n$MsgLockAndSuperfluidDelegateResponse\x12\n\n\x02ID\x18\x01 \x01(\x04\"b\n\x18MsgUnPoolWhitelistedPool\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:\"sender\"\x12#\n\x07pool_id\x18\x02 \x01(\x04\x42\x12\xf2\xde\x1f\x0eyaml:\"pool_id\"\";\n MsgUnPoolWhitelistedPoolResponse\x12\x17\n\x0f\x65xited_lock_ids\x18\x01 \x03(\x04\x32\xf4\x04\n\x03Msg\x12r\n\x12SuperfluidDelegate\x12).osmosis.superfluid.MsgSuperfluidDelegate\x1a\x31.osmosis.superfluid.MsgSuperfluidDelegateResponse\x12x\n\x14SuperfluidUndelegate\x12+.osmosis.superfluid.MsgSuperfluidUndelegate\x1a\x33.osmosis.superfluid.MsgSuperfluidUndelegateResponse\x12x\n\x14SuperfluidUnbondLock\x12+.osmosis.superfluid.MsgSuperfluidUnbondLock\x1a\x33.osmosis.superfluid.MsgSuperfluidUnbondLockResponse\x12\x87\x01\n\x19LockAndSuperfluidDelegate\x12\x30.osmosis.superfluid.MsgLockAndSuperfluidDelegate\x1a\x38.osmosis.superfluid.MsgLockAndSuperfluidDelegateResponse\x12{\n\x15UnPoolWhitelistedPool\x12,.osmosis.superfluid.MsgUnPoolWhitelistedPool\x1a\x34.osmosis.superfluid.MsgUnPoolWhitelistedPoolResponseB8Z6github.com/osmosis-labs/osmosis/v14/x/superfluid/typesb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.superfluid.tx_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z6github.com/osmosis-labs/osmosis/v14/x/superfluid/types'
  _MSGSUPERFLUIDDELEGATE.fields_by_name['sender']._options = None
  _MSGSUPERFLUIDDELEGATE.fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _MSGSUPERFLUIDUNDELEGATE.fields_by_name['sender']._options = None
  _MSGSUPERFLUIDUNDELEGATE.fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _MSGSUPERFLUIDUNBONDLOCK.fields_by_name['sender']._options = None
  _MSGSUPERFLUIDUNBONDLOCK.fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _MSGLOCKANDSUPERFLUIDDELEGATE.fields_by_name['sender']._options = None
  _MSGLOCKANDSUPERFLUIDDELEGATE.fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _MSGLOCKANDSUPERFLUIDDELEGATE.fields_by_name['coins']._options = None
  _MSGLOCKANDSUPERFLUIDDELEGATE.fields_by_name['coins']._serialized_options = b'\310\336\037\000\252\337\037(github.com/cosmos/cosmos-sdk/types.Coins'
  _MSGUNPOOLWHITELISTEDPOOL.fields_by_name['sender']._options = None
  _MSGUNPOOLWHITELISTEDPOOL.fields_by_name['sender']._serialized_options = b'\362\336\037\ryaml:\"sender\"'
  _MSGUNPOOLWHITELISTEDPOOL.fields_by_name['pool_id']._options = None
  _MSGUNPOOLWHITELISTEDPOOL.fields_by_name['pool_id']._serialized_options = b'\362\336\037\016yaml:\"pool_id\"'
  _MSGSUPERFLUIDDELEGATE._serialized_start=174
  _MSGSUPERFLUIDDELEGATE._serialized_end=267
  _MSGSUPERFLUIDDELEGATERESPONSE._serialized_start=269
  _MSGSUPERFLUIDDELEGATERESPONSE._serialized_end=300
  _MSGSUPERFLUIDUNDELEGATE._serialized_start=302
  _MSGSUPERFLUIDUNDELEGATE._serialized_end=379
  _MSGSUPERFLUIDUNDELEGATERESPONSE._serialized_start=381
  _MSGSUPERFLUIDUNDELEGATERESPONSE._serialized_end=414
  _MSGSUPERFLUIDUNBONDLOCK._serialized_start=416
  _MSGSUPERFLUIDUNBONDLOCK._serialized_end=493
  _MSGSUPERFLUIDUNBONDLOCKRESPONSE._serialized_start=495
  _MSGSUPERFLUIDUNBONDLOCKRESPONSE._serialized_end=528
  _MSGLOCKANDSUPERFLUIDDELEGATE._serialized_start=531
  _MSGLOCKANDSUPERFLUIDDELEGATE._serialized_end=706
  _MSGLOCKANDSUPERFLUIDDELEGATERESPONSE._serialized_start=708
  _MSGLOCKANDSUPERFLUIDDELEGATERESPONSE._serialized_end=758
  _MSGUNPOOLWHITELISTEDPOOL._serialized_start=760
  _MSGUNPOOLWHITELISTEDPOOL._serialized_end=858
  _MSGUNPOOLWHITELISTEDPOOLRESPONSE._serialized_start=860
  _MSGUNPOOLWHITELISTEDPOOLRESPONSE._serialized_end=919
  _MSG._serialized_start=922
  _MSG._serialized_end=1550
# @@protoc_insertion_point(module_scope)
