# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: storage.proto
# Protobuf Python Version: 5.27.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    3,
    '',
    'storage.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rstorage.proto\x12\x14signal.proto.storage\"\xb7\x08\n\x10SessionStructure\x12\x17\n\x0fsession_version\x18\x01 \x01(\r\x12\x1d\n\x15local_identity_public\x18\x02 \x01(\x0c\x12\x1e\n\x16remote_identity_public\x18\x03 \x01(\x0c\x12\x10\n\x08root_key\x18\x04 \x01(\x0c\x12\x18\n\x10previous_counter\x18\x05 \x01(\r\x12\x42\n\x0csender_chain\x18\x06 \x01(\x0b\x32,.signal.proto.storage.SessionStructure.Chain\x12\x45\n\x0freceiver_chains\x18\x07 \x03(\x0b\x32,.signal.proto.storage.SessionStructure.Chain\x12M\n\x0fpending_pre_key\x18\t \x01(\x0b\x32\x34.signal.proto.storage.SessionStructure.PendingPreKey\x12X\n\x15pending_kyber_pre_key\x18\x0e \x01(\x0b\x32\x39.signal.proto.storage.SessionStructure.PendingKyberPreKey\x12\x1e\n\x16remote_registration_id\x18\n \x01(\r\x12\x1d\n\x15local_registration_id\x18\x0b \x01(\r\x12\x16\n\x0e\x61lice_base_key\x18\r \x01(\x0c\x1a\xd6\x02\n\x05\x43hain\x12\x1a\n\x12sender_ratchet_key\x18\x01 \x01(\x0c\x12\"\n\x1asender_ratchet_key_private\x18\x02 \x01(\x0c\x12H\n\tchain_key\x18\x03 \x01(\x0b\x32\x35.signal.proto.storage.SessionStructure.Chain.ChainKey\x12M\n\x0cmessage_keys\x18\x04 \x03(\x0b\x32\x37.signal.proto.storage.SessionStructure.Chain.MessageKey\x1a&\n\x08\x43hainKey\x12\r\n\x05index\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\x0c\x1aL\n\nMessageKey\x12\r\n\x05index\x18\x01 \x01(\r\x12\x12\n\ncipher_key\x18\x02 \x01(\x0c\x12\x0f\n\x07mac_key\x18\x03 \x01(\x0c\x12\n\n\x02iv\x18\x04 \x01(\x0c\x1aw\n\rPendingPreKey\x12\x17\n\npre_key_id\x18\x01 \x01(\rH\x00\x88\x01\x01\x12\x19\n\x11signed_pre_key_id\x18\x03 \x01(\x05\x12\x10\n\x08\x62\x61se_key\x18\x02 \x01(\x0c\x12\x11\n\ttimestamp\x18\x04 \x01(\x04\x42\r\n\x0b_pre_key_id\x1a<\n\x12PendingKyberPreKey\x12\x12\n\npre_key_id\x18\x01 \x01(\r\x12\x12\n\nciphertext\x18\x02 \x01(\x0cJ\x04\x08\x0c\x10\r\"m\n\x0fRecordStructure\x12?\n\x0f\x63urrent_session\x18\x01 \x01(\x0b\x32&.signal.proto.storage.SessionStructure\x12\x19\n\x11previous_sessions\x18\x02 \x03(\x0c\"L\n\x15PreKeyRecordStructure\x12\n\n\x02id\x18\x01 \x01(\r\x12\x12\n\npublic_key\x18\x02 \x01(\x0c\x12\x13\n\x0bprivate_key\x18\x03 \x01(\x0c\"x\n\x1bSignedPreKeyRecordStructure\x12\n\n\x02id\x18\x01 \x01(\r\x12\x12\n\npublic_key\x18\x02 \x01(\x0c\x12\x13\n\x0bprivate_key\x18\x03 \x01(\x0c\x12\x11\n\tsignature\x18\x04 \x01(\x0c\x12\x11\n\ttimestamp\x18\x05 \x01(\x06\"C\n\x18IdentityKeyPairStructure\x12\x12\n\npublic_key\x18\x01 \x01(\x0c\x12\x13\n\x0bprivate_key\x18\x02 \x01(\x0c\"\xf2\x03\n\x17SenderKeyStateStructure\x12\x17\n\x0fmessage_version\x18\x05 \x01(\r\x12\x10\n\x08\x63hain_id\x18\x01 \x01(\r\x12V\n\x10sender_chain_key\x18\x02 \x01(\x0b\x32<.signal.proto.storage.SenderKeyStateStructure.SenderChainKey\x12Z\n\x12sender_signing_key\x18\x03 \x01(\x0b\x32>.signal.proto.storage.SenderKeyStateStructure.SenderSigningKey\x12[\n\x13sender_message_keys\x18\x04 \x03(\x0b\x32>.signal.proto.storage.SenderKeyStateStructure.SenderMessageKey\x1a\x31\n\x0eSenderChainKey\x12\x11\n\titeration\x18\x01 \x01(\r\x12\x0c\n\x04seed\x18\x02 \x01(\x0c\x1a\x33\n\x10SenderMessageKey\x12\x11\n\titeration\x18\x01 \x01(\r\x12\x0c\n\x04seed\x18\x02 \x01(\x0c\x1a\x33\n\x10SenderSigningKey\x12\x0e\n\x06public\x18\x01 \x01(\x0c\x12\x0f\n\x07private\x18\x02 \x01(\x0c\"d\n\x18SenderKeyRecordStructure\x12H\n\x11sender_key_states\x18\x01 \x03(\x0b\x32-.signal.proto.storage.SenderKeyStateStructureb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'storage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SESSIONSTRUCTURE']._serialized_start=40
  _globals['_SESSIONSTRUCTURE']._serialized_end=1119
  _globals['_SESSIONSTRUCTURE_CHAIN']._serialized_start=588
  _globals['_SESSIONSTRUCTURE_CHAIN']._serialized_end=930
  _globals['_SESSIONSTRUCTURE_CHAIN_CHAINKEY']._serialized_start=814
  _globals['_SESSIONSTRUCTURE_CHAIN_CHAINKEY']._serialized_end=852
  _globals['_SESSIONSTRUCTURE_CHAIN_MESSAGEKEY']._serialized_start=854
  _globals['_SESSIONSTRUCTURE_CHAIN_MESSAGEKEY']._serialized_end=930
  _globals['_SESSIONSTRUCTURE_PENDINGPREKEY']._serialized_start=932
  _globals['_SESSIONSTRUCTURE_PENDINGPREKEY']._serialized_end=1051
  _globals['_SESSIONSTRUCTURE_PENDINGKYBERPREKEY']._serialized_start=1053
  _globals['_SESSIONSTRUCTURE_PENDINGKYBERPREKEY']._serialized_end=1113
  _globals['_RECORDSTRUCTURE']._serialized_start=1121
  _globals['_RECORDSTRUCTURE']._serialized_end=1230
  _globals['_PREKEYRECORDSTRUCTURE']._serialized_start=1232
  _globals['_PREKEYRECORDSTRUCTURE']._serialized_end=1308
  _globals['_SIGNEDPREKEYRECORDSTRUCTURE']._serialized_start=1310
  _globals['_SIGNEDPREKEYRECORDSTRUCTURE']._serialized_end=1430
  _globals['_IDENTITYKEYPAIRSTRUCTURE']._serialized_start=1432
  _globals['_IDENTITYKEYPAIRSTRUCTURE']._serialized_end=1499
  _globals['_SENDERKEYSTATESTRUCTURE']._serialized_start=1502
  _globals['_SENDERKEYSTATESTRUCTURE']._serialized_end=2000
  _globals['_SENDERKEYSTATESTRUCTURE_SENDERCHAINKEY']._serialized_start=1845
  _globals['_SENDERKEYSTATESTRUCTURE_SENDERCHAINKEY']._serialized_end=1894
  _globals['_SENDERKEYSTATESTRUCTURE_SENDERMESSAGEKEY']._serialized_start=1896
  _globals['_SENDERKEYSTATESTRUCTURE_SENDERMESSAGEKEY']._serialized_end=1947
  _globals['_SENDERKEYSTATESTRUCTURE_SENDERSIGNINGKEY']._serialized_start=1949
  _globals['_SENDERKEYSTATESTRUCTURE_SENDERSIGNINGKEY']._serialized_end=2000
  _globals['_SENDERKEYRECORDSTRUCTURE']._serialized_start=2002
  _globals['_SENDERKEYRECORDSTRUCTURE']._serialized_end=2102
# @@protoc_insertion_point(module_scope)
