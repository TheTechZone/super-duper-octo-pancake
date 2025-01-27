import wire_pb2 as _wire_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StoredTreeHead(_message.Message):
    __slots__ = ("tree_head", "root")
    TREE_HEAD_FIELD_NUMBER: _ClassVar[int]
    ROOT_FIELD_NUMBER: _ClassVar[int]
    tree_head: _wire_pb2.TreeHead
    root: bytes
    def __init__(self, tree_head: _Optional[_Union[_wire_pb2.TreeHead, _Mapping]] = ..., root: _Optional[bytes] = ...) -> None: ...

class StoredMonitoringData(_message.Message):
    __slots__ = ("index", "pos", "ptrs", "owned")
    class PtrsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    INDEX_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    PTRS_FIELD_NUMBER: _ClassVar[int]
    OWNED_FIELD_NUMBER: _ClassVar[int]
    index: bytes
    pos: int
    ptrs: _containers.ScalarMap[int, int]
    owned: bool
    def __init__(self, index: _Optional[bytes] = ..., pos: _Optional[int] = ..., ptrs: _Optional[_Mapping[int, int]] = ..., owned: bool = ...) -> None: ...

class StoredAccountData(_message.Message):
    __slots__ = ("aci", "e164", "username_hash", "last_tree_head")
    ACI_FIELD_NUMBER: _ClassVar[int]
    E164_FIELD_NUMBER: _ClassVar[int]
    USERNAME_HASH_FIELD_NUMBER: _ClassVar[int]
    LAST_TREE_HEAD_FIELD_NUMBER: _ClassVar[int]
    aci: StoredMonitoringData
    e164: StoredMonitoringData
    username_hash: StoredMonitoringData
    last_tree_head: StoredTreeHead
    def __init__(self, aci: _Optional[_Union[StoredMonitoringData, _Mapping]] = ..., e164: _Optional[_Union[StoredMonitoringData, _Mapping]] = ..., username_hash: _Optional[_Union[StoredMonitoringData, _Mapping]] = ..., last_tree_head: _Optional[_Union[StoredTreeHead, _Mapping]] = ...) -> None: ...
