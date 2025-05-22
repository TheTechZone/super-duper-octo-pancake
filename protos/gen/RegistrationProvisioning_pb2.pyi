from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegistrationProvisionEnvelope(_message.Message):
    __slots__ = ("publicKey", "body")
    PUBLICKEY_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    publicKey: bytes
    body: bytes
    def __init__(self, publicKey: _Optional[bytes] = ..., body: _Optional[bytes] = ...) -> None: ...

class RegistrationProvisionMessage(_message.Message):
    __slots__ = ("e164", "aci", "accountEntropyPool", "pin", "platform", "backupTimestampMs", "tier", "backupSizeBytes", "restoreMethodToken", "aciIdentityKeyPublic", "aciIdentityKeyPrivate", "pniIdentityKeyPublic", "pniIdentityKeyPrivate")
    class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ANDROID: _ClassVar[RegistrationProvisionMessage.Platform]
        IOS: _ClassVar[RegistrationProvisionMessage.Platform]
    ANDROID: RegistrationProvisionMessage.Platform
    IOS: RegistrationProvisionMessage.Platform
    class Tier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FREE: _ClassVar[RegistrationProvisionMessage.Tier]
        PAID: _ClassVar[RegistrationProvisionMessage.Tier]
    FREE: RegistrationProvisionMessage.Tier
    PAID: RegistrationProvisionMessage.Tier
    E164_FIELD_NUMBER: _ClassVar[int]
    ACI_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTENTROPYPOOL_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    BACKUPTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    TIER_FIELD_NUMBER: _ClassVar[int]
    BACKUPSIZEBYTES_FIELD_NUMBER: _ClassVar[int]
    RESTOREMETHODTOKEN_FIELD_NUMBER: _ClassVar[int]
    ACIIDENTITYKEYPUBLIC_FIELD_NUMBER: _ClassVar[int]
    ACIIDENTITYKEYPRIVATE_FIELD_NUMBER: _ClassVar[int]
    PNIIDENTITYKEYPUBLIC_FIELD_NUMBER: _ClassVar[int]
    PNIIDENTITYKEYPRIVATE_FIELD_NUMBER: _ClassVar[int]
    e164: str
    aci: bytes
    accountEntropyPool: str
    pin: str
    platform: RegistrationProvisionMessage.Platform
    backupTimestampMs: int
    tier: RegistrationProvisionMessage.Tier
    backupSizeBytes: int
    restoreMethodToken: str
    aciIdentityKeyPublic: bytes
    aciIdentityKeyPrivate: bytes
    pniIdentityKeyPublic: bytes
    pniIdentityKeyPrivate: bytes
    def __init__(self, e164: _Optional[str] = ..., aci: _Optional[bytes] = ..., accountEntropyPool: _Optional[str] = ..., pin: _Optional[str] = ..., platform: _Optional[_Union[RegistrationProvisionMessage.Platform, str]] = ..., backupTimestampMs: _Optional[int] = ..., tier: _Optional[_Union[RegistrationProvisionMessage.Tier, str]] = ..., backupSizeBytes: _Optional[int] = ..., restoreMethodToken: _Optional[str] = ..., aciIdentityKeyPublic: _Optional[bytes] = ..., aciIdentityKeyPrivate: _Optional[bytes] = ..., pniIdentityKeyPublic: _Optional[bytes] = ..., pniIdentityKeyPrivate: _Optional[bytes] = ...) -> None: ...
