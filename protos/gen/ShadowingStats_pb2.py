# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ShadowingStats.proto
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
    'ShadowingStats.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14ShadowingStats.proto\x12\rsignalservice\"u\n\x08Snapshot\x12\x18\n\x10requestsCompared\x18\x01 \x01(\x05\x12\x10\n\x08\x66\x61ilures\x18\x02 \x01(\x05\x12\x13\n\x0b\x62\x61\x64Statuses\x18\x03 \x01(\x05\x12\x12\n\nreconnects\x18\x04 \x01(\x05\x12\x14\n\x0clastNotified\x18\x05 \x01(\x03\x42\x45\n3org.whispersystems.signalservice.internal.websocketB\x0eShadowingStatsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ShadowingStats_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n3org.whispersystems.signalservice.internal.websocketB\016ShadowingStats'
  _globals['_SNAPSHOT']._serialized_start=39
  _globals['_SNAPSHOT']._serialized_end=156
# @@protoc_insertion_point(module_scope)