from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ClientHandshakeStart(_message.Message):
    __slots__ = ("pubkey", "evidence", "endorsement")
    PUBKEY_FIELD_NUMBER: _ClassVar[int]
    EVIDENCE_FIELD_NUMBER: _ClassVar[int]
    ENDORSEMENT_FIELD_NUMBER: _ClassVar[int]
    pubkey: bytes
    evidence: bytes
    endorsement: bytes
    def __init__(self, pubkey: _Optional[bytes] = ..., evidence: _Optional[bytes] = ..., endorsement: _Optional[bytes] = ...) -> None: ...
