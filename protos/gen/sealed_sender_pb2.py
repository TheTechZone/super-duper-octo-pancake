# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sealed_sender.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13sealed_sender.proto\x12\x1asignal.proto.sealed_sender\"c\n\x11ServerCertificate\x12\x13\n\x0b\x63\x65rtificate\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x1a&\n\x0b\x43\x65rtificate\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0b\n\x03key\x18\x02 \x01(\x0c\"\xee\x01\n\x11SenderCertificate\x12\x13\n\x0b\x63\x65rtificate\x18\x01 \x01(\x0c\x12\x11\n\tsignature\x18\x02 \x01(\x0c\x1a\xb0\x01\n\x0b\x43\x65rtificate\x12\x12\n\nsenderE164\x18\x01 \x01(\t\x12\x12\n\nsenderUuid\x18\x06 \x01(\t\x12\x14\n\x0csenderDevice\x18\x02 \x01(\r\x12\x0f\n\x07\x65xpires\x18\x03 \x01(\x06\x12\x13\n\x0bidentityKey\x18\x04 \x01(\x0c\x12=\n\x06signer\x18\x05 \x01(\x0b\x32-.signal.proto.sealed_sender.ServerCertificate\"\xf2\x03\n\x19UnidentifiedSenderMessage\x12\x17\n\x0f\x65phemeralPublic\x18\x01 \x01(\x0c\x12\x17\n\x0f\x65ncryptedStatic\x18\x02 \x01(\x0c\x12\x18\n\x10\x65ncryptedMessage\x18\x03 \x01(\x0c\x1a\x88\x03\n\x07Message\x12P\n\x04type\x18\x01 \x01(\x0e\x32\x42.signal.proto.sealed_sender.UnidentifiedSenderMessage.Message.Type\x12\x19\n\x11senderCertificate\x18\x02 \x01(\x0c\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\x0c\x12^\n\x0b\x63ontentHint\x18\x04 \x01(\x0e\x32I.signal.proto.sealed_sender.UnidentifiedSenderMessage.Message.ContentHint\x12\x0f\n\x07groupId\x18\x05 \x01(\x0c\"[\n\x04Type\x12\x12\n\x0ePREKEY_MESSAGE\x10\x01\x12\x0b\n\x07MESSAGE\x10\x02\x12\x15\n\x11SENDERKEY_MESSAGE\x10\x07\x12\x15\n\x11PLAINTEXT_CONTENT\x10\x08\"\x04\x08\x03\x10\x06\"1\n\x0b\x43ontentHint\x12\x0e\n\nRESENDABLE\x10\x01\x12\x0c\n\x08IMPLICIT\x10\x02\"\x04\x08\x00\x10\x00')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sealed_sender_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_SERVERCERTIFICATE']._serialized_start=51
  _globals['_SERVERCERTIFICATE']._serialized_end=150
  _globals['_SERVERCERTIFICATE_CERTIFICATE']._serialized_start=112
  _globals['_SERVERCERTIFICATE_CERTIFICATE']._serialized_end=150
  _globals['_SENDERCERTIFICATE']._serialized_start=153
  _globals['_SENDERCERTIFICATE']._serialized_end=391
  _globals['_SENDERCERTIFICATE_CERTIFICATE']._serialized_start=215
  _globals['_SENDERCERTIFICATE_CERTIFICATE']._serialized_end=391
  _globals['_UNIDENTIFIEDSENDERMESSAGE']._serialized_start=394
  _globals['_UNIDENTIFIEDSENDERMESSAGE']._serialized_end=892
  _globals['_UNIDENTIFIEDSENDERMESSAGE_MESSAGE']._serialized_start=500
  _globals['_UNIDENTIFIEDSENDERMESSAGE_MESSAGE']._serialized_end=892
  _globals['_UNIDENTIFIEDSENDERMESSAGE_MESSAGE_TYPE']._serialized_start=750
  _globals['_UNIDENTIFIEDSENDERMESSAGE_MESSAGE_TYPE']._serialized_end=841
  _globals['_UNIDENTIFIEDSENDERMESSAGE_MESSAGE_CONTENTHINT']._serialized_start=843
  _globals['_UNIDENTIFIEDSENDERMESSAGE_MESSAGE_CONTENTHINT']._serialized_end=892
# @@protoc_insertion_point(module_scope)
