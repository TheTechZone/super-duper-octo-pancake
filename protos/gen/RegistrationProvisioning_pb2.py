# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: RegistrationProvisioning.proto
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
    'RegistrationProvisioning.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eRegistrationProvisioning.proto\"@\n\x1dRegistrationProvisionEnvelope\x12\x11\n\tpublicKey\x18\x01 \x01(\x0c\x12\x0c\n\x04\x62ody\x18\x02 \x01(\x0c\"\xa5\x04\n\x1cRegistrationProvisionMessage\x12\x0c\n\x04\x65\x31\x36\x34\x18\x01 \x01(\t\x12\x0b\n\x03\x61\x63i\x18\x02 \x01(\x0c\x12\x1a\n\x12\x61\x63\x63ountEntropyPool\x18\x03 \x01(\t\x12\x10\n\x03pin\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x38\n\x08platform\x18\x05 \x01(\x0e\x32&.RegistrationProvisionMessage.Platform\x12\x1e\n\x11\x62\x61\x63kupTimestampMs\x18\x06 \x01(\x04H\x01\x88\x01\x01\x12\x35\n\x04tier\x18\x07 \x01(\x0e\x32\".RegistrationProvisionMessage.TierH\x02\x88\x01\x01\x12\x1c\n\x0f\x62\x61\x63kupSizeBytes\x18\x08 \x01(\x04H\x03\x88\x01\x01\x12\x1a\n\x12restoreMethodToken\x18\t \x01(\t\x12\x1c\n\x14\x61\x63iIdentityKeyPublic\x18\n \x01(\x0c\x12\x1d\n\x15\x61\x63iIdentityKeyPrivate\x18\x0b \x01(\x0c\x12\x1c\n\x14pniIdentityKeyPublic\x18\x0c \x01(\x0c\x12\x1d\n\x15pniIdentityKeyPrivate\x18\r \x01(\x0c\" \n\x08Platform\x12\x0b\n\x07\x41NDROID\x10\x00\x12\x07\n\x03IOS\x10\x01\"\x1a\n\x04Tier\x12\x08\n\x04\x46REE\x10\x00\x12\x08\n\x04PAID\x10\x01\x42\x06\n\x04_pinB\x14\n\x12_backupTimestampMsB\x07\n\x05_tierB\x12\n\x10_backupSizeBytesB!\n\x1dorg.signal.registration.protoP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RegistrationProvisioning_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\035org.signal.registration.protoP\001'
  _globals['_REGISTRATIONPROVISIONENVELOPE']._serialized_start=34
  _globals['_REGISTRATIONPROVISIONENVELOPE']._serialized_end=98
  _globals['_REGISTRATIONPROVISIONMESSAGE']._serialized_start=101
  _globals['_REGISTRATIONPROVISIONMESSAGE']._serialized_end=650
  _globals['_REGISTRATIONPROVISIONMESSAGE_PLATFORM']._serialized_start=531
  _globals['_REGISTRATIONPROVISIONMESSAGE_PLATFORM']._serialized_end=563
  _globals['_REGISTRATIONPROVISIONMESSAGE_TIER']._serialized_start=565
  _globals['_REGISTRATIONPROVISIONMESSAGE_TIER']._serialized_end=591
# @@protoc_insertion_point(module_scope)
