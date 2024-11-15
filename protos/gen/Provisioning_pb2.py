# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: Provisioning.proto
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
    'Provisioning.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12Provisioning.proto\x12\rsignalservice\"&\n\x13ProvisioningAddress\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"4\n\x11ProvisionEnvelope\x12\x11\n\tpublicKey\x18\x01 \x01(\x0c\x12\x0c\n\x04\x62ody\x18\x02 \x01(\x0c\"\x91\x03\n\x10ProvisionMessage\x12\x1c\n\x14\x61\x63iIdentityKeyPublic\x18\x01 \x01(\x0c\x12\x1d\n\x15\x61\x63iIdentityKeyPrivate\x18\x02 \x01(\x0c\x12\x1c\n\x14pniIdentityKeyPublic\x18\x0b \x01(\x0c\x12\x1d\n\x15pniIdentityKeyPrivate\x18\x0c \x01(\x0c\x12\x0b\n\x03\x61\x63i\x18\x08 \x01(\t\x12\x0b\n\x03pni\x18\n \x01(\t\x12\x0e\n\x06number\x18\x03 \x01(\t\x12\x18\n\x10provisioningCode\x18\x04 \x01(\t\x12\x11\n\tuserAgent\x18\x05 \x01(\t\x12\x12\n\nprofileKey\x18\x06 \x01(\x0c\x12\x14\n\x0creadReceipts\x18\x07 \x01(\x08\x12\x1b\n\x13provisioningVersion\x18\t \x01(\r\x12\x11\n\tmasterKey\x18\r \x01(\x0c\x12\x1a\n\x12\x65phemeralBackupKey\x18\x0e \x01(\x0c\x12\x1a\n\x12\x61\x63\x63ountEntropyPool\x18\x0f \x01(\t\x12\x1a\n\x12mediaRootBackupKey\x18\x10 \x01(\x0c*G\n\x13ProvisioningVersion\x12\x0b\n\x07INITIAL\x10\x00\x12\x12\n\x0eTABLET_SUPPORT\x10\x01\x12\x0b\n\x07\x43URRENT\x10\x01\x1a\x02\x10\x01\x42\x44\n.org.whispersystems.signalservice.internal.pushB\x12ProvisioningProtos')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Provisioning_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n.org.whispersystems.signalservice.internal.pushB\022ProvisioningProtos'
  _globals['_PROVISIONINGVERSION']._loaded_options = None
  _globals['_PROVISIONINGVERSION']._serialized_options = b'\020\001'
  _globals['_PROVISIONINGVERSION']._serialized_start=535
  _globals['_PROVISIONINGVERSION']._serialized_end=606
  _globals['_PROVISIONINGADDRESS']._serialized_start=37
  _globals['_PROVISIONINGADDRESS']._serialized_end=75
  _globals['_PROVISIONENVELOPE']._serialized_start=77
  _globals['_PROVISIONENVELOPE']._serialized_end=129
  _globals['_PROVISIONMESSAGE']._serialized_start=132
  _globals['_PROVISIONMESSAGE']._serialized_end=533
# @@protoc_insertion_point(module_scope)
