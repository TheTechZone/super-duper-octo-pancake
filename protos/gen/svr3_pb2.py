# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: svr3.proto
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
    'svr3.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nsvr3.proto\x12\x0forg.signal.svr3\"\x8e\x01\n\x0c\x41SNPEvidence\x12\x18\n\x10\x61ttestation_data\x18\x01 \x01(\x0c\x12\x0c\n\x04pcrs\x18\x02 \x01(\x0c\x12\x0b\n\x03msg\x18\x03 \x01(\x0c\x12\x0b\n\x03sig\x18\x04 \x01(\x0c\x12\x12\n\nsnp_report\x18\x05 \x01(\x0c\x12\x14\n\x0cruntime_data\x18\x06 \x01(\x0c\x12\x12\n\nakcert_der\x18\x07 \x01(\x0c\"O\n\x10\x41SNPEndorsements\x12\x18\n\x10intermediate_der\x18\x01 \x01(\x0c\x12\x10\n\x08vcek_der\x18\x02 \x01(\x0c\x12\x0f\n\x07\x61sk_der\x18\x03 \x01(\x0c\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'svr3_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ASNPEVIDENCE']._serialized_start=32
  _globals['_ASNPEVIDENCE']._serialized_end=174
  _globals['_ASNPENDORSEMENTS']._serialized_start=176
  _globals['_ASNPENDORSEMENTS']._serialized_end=255
# @@protoc_insertion_point(module_scope)
