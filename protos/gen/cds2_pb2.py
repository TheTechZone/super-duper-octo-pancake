# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: cds2.proto
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
    'cds2.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncds2.proto\x12\x0forg.signal.cds2\"M\n\x14\x43lientHandshakeStart\x12\x0e\n\x06pubkey\x18\x01 \x01(\x0c\x12\x10\n\x08\x65vidence\x18\x02 \x01(\x0c\x12\x13\n\x0b\x65ndorsement\x18\x03 \x01(\x0c\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cds2_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CLIENTHANDSHAKESTART']._serialized_start=31
  _globals['_CLIENTHANDSHAKESTART']._serialized_end=108
# @@protoc_insertion_point(module_scope)
