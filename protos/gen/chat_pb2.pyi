import wire_pb2 as _wire_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchResponse(_message.Message):
    __slots__ = ("tree_head", "aci", "e164", "username_hash")
    TREE_HEAD_FIELD_NUMBER: _ClassVar[int]
    ACI_FIELD_NUMBER: _ClassVar[int]
    E164_FIELD_NUMBER: _ClassVar[int]
    USERNAME_HASH_FIELD_NUMBER: _ClassVar[int]
    tree_head: _wire_pb2.FullTreeHead
    aci: _wire_pb2.CondensedTreeSearchResponse
    e164: _wire_pb2.CondensedTreeSearchResponse
    username_hash: _wire_pb2.CondensedTreeSearchResponse
    def __init__(self, tree_head: _Optional[_Union[_wire_pb2.FullTreeHead, _Mapping]] = ..., aci: _Optional[_Union[_wire_pb2.CondensedTreeSearchResponse, _Mapping]] = ..., e164: _Optional[_Union[_wire_pb2.CondensedTreeSearchResponse, _Mapping]] = ..., username_hash: _Optional[_Union[_wire_pb2.CondensedTreeSearchResponse, _Mapping]] = ...) -> None: ...

class DistinguishedResponse(_message.Message):
    __slots__ = ("tree_head", "distinguished")
    TREE_HEAD_FIELD_NUMBER: _ClassVar[int]
    DISTINGUISHED_FIELD_NUMBER: _ClassVar[int]
    tree_head: _wire_pb2.FullTreeHead
    distinguished: _wire_pb2.CondensedTreeSearchResponse
    def __init__(self, tree_head: _Optional[_Union[_wire_pb2.FullTreeHead, _Mapping]] = ..., distinguished: _Optional[_Union[_wire_pb2.CondensedTreeSearchResponse, _Mapping]] = ...) -> None: ...

class ChatMonitorResponse(_message.Message):
    __slots__ = ("tree_head", "aci", "username_hash", "e164", "inclusion")
    TREE_HEAD_FIELD_NUMBER: _ClassVar[int]
    ACI_FIELD_NUMBER: _ClassVar[int]
    USERNAME_HASH_FIELD_NUMBER: _ClassVar[int]
    E164_FIELD_NUMBER: _ClassVar[int]
    INCLUSION_FIELD_NUMBER: _ClassVar[int]
    tree_head: _wire_pb2.FullTreeHead
    aci: _wire_pb2.MonitorProof
    username_hash: _wire_pb2.MonitorProof
    e164: _wire_pb2.MonitorProof
    inclusion: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, tree_head: _Optional[_Union[_wire_pb2.FullTreeHead, _Mapping]] = ..., aci: _Optional[_Union[_wire_pb2.MonitorProof, _Mapping]] = ..., username_hash: _Optional[_Union[_wire_pb2.MonitorProof, _Mapping]] = ..., e164: _Optional[_Union[_wire_pb2.MonitorProof, _Mapping]] = ..., inclusion: _Optional[_Iterable[bytes]] = ...) -> None: ...
