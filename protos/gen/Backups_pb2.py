# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Backups.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rBackups.proto\x12\x06signal\"\xe2\x01\n\x0cSqlStatement\x12\x11\n\tstatement\x18\x01 \x01(\t\x12\x35\n\nparameters\x18\x02 \x03(\x0b\x32!.signal.SqlStatement.SqlParameter\x1a\x87\x01\n\x0cSqlParameter\x12\x16\n\x0estringParamter\x18\x01 \x01(\t\x12\x18\n\x10integerParameter\x18\x02 \x01(\x04\x12\x17\n\x0f\x64oubleParameter\x18\x03 \x01(\x01\x12\x15\n\rblobParameter\x18\x04 \x01(\x0c\x12\x15\n\rnullparameter\x18\x05 \x01(\x08\"\x84\x01\n\x10SharedPreference\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t\x12\x14\n\x0c\x62ooleanValue\x18\x04 \x01(\x08\x12\x16\n\x0estringSetValue\x18\x05 \x03(\t\x12\x18\n\x10isStringSetValue\x18\x06 \x01(\x08\"A\n\nAttachment\x12\r\n\x05rowId\x18\x01 \x01(\x04\x12\x14\n\x0c\x61ttachmentId\x18\x02 \x01(\x04\x12\x0e\n\x06length\x18\x03 \x01(\r\"(\n\x07Sticker\x12\r\n\x05rowId\x18\x01 \x01(\x04\x12\x0e\n\x06length\x18\x02 \x01(\r\";\n\x06\x41vatar\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0brecipientId\x18\x03 \x01(\t\x12\x0e\n\x06length\x18\x02 \x01(\r\"\"\n\x0f\x44\x61tabaseVersion\x12\x0f\n\x07version\x18\x01 \x01(\r\"3\n\x06Header\x12\n\n\x02iv\x18\x01 \x01(\x0c\x12\x0c\n\x04salt\x18\x02 \x01(\x0c\x12\x0f\n\x07version\x18\x03 \x01(\r\"\x92\x01\n\x08KeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x11\n\tblobValue\x18\x02 \x01(\x0c\x12\x14\n\x0c\x62ooleanValue\x18\x03 \x01(\x08\x12\x12\n\nfloatValue\x18\x04 \x01(\x02\x12\x14\n\x0cintegerValue\x18\x05 \x01(\x05\x12\x11\n\tlongValue\x18\x06 \x01(\x03\x12\x13\n\x0bstringValue\x18\x07 \x01(\t\"\xc9\x02\n\x0b\x42\x61\x63kupFrame\x12\x1e\n\x06header\x18\x01 \x01(\x0b\x32\x0e.signal.Header\x12\'\n\tstatement\x18\x02 \x01(\x0b\x32\x14.signal.SqlStatement\x12,\n\npreference\x18\x03 \x01(\x0b\x32\x18.signal.SharedPreference\x12&\n\nattachment\x18\x04 \x01(\x0b\x32\x12.signal.Attachment\x12(\n\x07version\x18\x05 \x01(\x0b\x32\x17.signal.DatabaseVersion\x12\x0b\n\x03\x65nd\x18\x06 \x01(\x08\x12\x1e\n\x06\x61vatar\x18\x07 \x01(\x0b\x32\x0e.signal.Avatar\x12 \n\x07sticker\x18\x08 \x01(\x0b\x32\x0f.signal.Sticker\x12\"\n\x08keyValue\x18\t \x01(\x0b\x32\x10.signal.KeyValueB)\n\'org.thoughtcrime.securesms.backup.proto')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Backups_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\'org.thoughtcrime.securesms.backup.proto'
  _globals['_SQLSTATEMENT']._serialized_start=26
  _globals['_SQLSTATEMENT']._serialized_end=252
  _globals['_SQLSTATEMENT_SQLPARAMETER']._serialized_start=117
  _globals['_SQLSTATEMENT_SQLPARAMETER']._serialized_end=252
  _globals['_SHAREDPREFERENCE']._serialized_start=255
  _globals['_SHAREDPREFERENCE']._serialized_end=387
  _globals['_ATTACHMENT']._serialized_start=389
  _globals['_ATTACHMENT']._serialized_end=454
  _globals['_STICKER']._serialized_start=456
  _globals['_STICKER']._serialized_end=496
  _globals['_AVATAR']._serialized_start=498
  _globals['_AVATAR']._serialized_end=557
  _globals['_DATABASEVERSION']._serialized_start=559
  _globals['_DATABASEVERSION']._serialized_end=593
  _globals['_HEADER']._serialized_start=595
  _globals['_HEADER']._serialized_end=646
  _globals['_KEYVALUE']._serialized_start=649
  _globals['_KEYVALUE']._serialized_end=795
  _globals['_BACKUPFRAME']._serialized_start=798
  _globals['_BACKUPFRAME']._serialized_end=1127
# @@protoc_insertion_point(module_scope)
