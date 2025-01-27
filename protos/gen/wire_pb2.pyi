from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PrefixProof(_message.Message):
    __slots__ = ("proof", "counter")
    PROOF_FIELD_NUMBER: _ClassVar[int]
    COUNTER_FIELD_NUMBER: _ClassVar[int]
    proof: _containers.RepeatedScalarFieldContainer[bytes]
    counter: int
    def __init__(self, proof: _Optional[_Iterable[bytes]] = ..., counter: _Optional[int] = ...) -> None: ...

class TreeHead(_message.Message):
    __slots__ = ("tree_size", "timestamp", "signature")
    TREE_SIZE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    tree_size: int
    timestamp: int
    signature: bytes
    def __init__(self, tree_size: _Optional[int] = ..., timestamp: _Optional[int] = ..., signature: _Optional[bytes] = ...) -> None: ...

class AuditorTreeHead(_message.Message):
    __slots__ = ("tree_head", "root_value", "consistency")
    TREE_HEAD_FIELD_NUMBER: _ClassVar[int]
    ROOT_VALUE_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    tree_head: TreeHead
    root_value: bytes
    consistency: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, tree_head: _Optional[_Union[TreeHead, _Mapping]] = ..., root_value: _Optional[bytes] = ..., consistency: _Optional[_Iterable[bytes]] = ...) -> None: ...

class FullTreeHead(_message.Message):
    __slots__ = ("tree_head", "last", "distinguished", "auditor_tree_head")
    TREE_HEAD_FIELD_NUMBER: _ClassVar[int]
    LAST_FIELD_NUMBER: _ClassVar[int]
    DISTINGUISHED_FIELD_NUMBER: _ClassVar[int]
    AUDITOR_TREE_HEAD_FIELD_NUMBER: _ClassVar[int]
    tree_head: TreeHead
    last: _containers.RepeatedScalarFieldContainer[bytes]
    distinguished: _containers.RepeatedScalarFieldContainer[bytes]
    auditor_tree_head: AuditorTreeHead
    def __init__(self, tree_head: _Optional[_Union[TreeHead, _Mapping]] = ..., last: _Optional[_Iterable[bytes]] = ..., distinguished: _Optional[_Iterable[bytes]] = ..., auditor_tree_head: _Optional[_Union[AuditorTreeHead, _Mapping]] = ...) -> None: ...

class ProofStep(_message.Message):
    __slots__ = ("prefix", "commitment")
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    COMMITMENT_FIELD_NUMBER: _ClassVar[int]
    prefix: PrefixProof
    commitment: bytes
    def __init__(self, prefix: _Optional[_Union[PrefixProof, _Mapping]] = ..., commitment: _Optional[bytes] = ...) -> None: ...

class SearchProof(_message.Message):
    __slots__ = ("pos", "steps", "inclusion")
    POS_FIELD_NUMBER: _ClassVar[int]
    STEPS_FIELD_NUMBER: _ClassVar[int]
    INCLUSION_FIELD_NUMBER: _ClassVar[int]
    pos: int
    steps: _containers.RepeatedCompositeFieldContainer[ProofStep]
    inclusion: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, pos: _Optional[int] = ..., steps: _Optional[_Iterable[_Union[ProofStep, _Mapping]]] = ..., inclusion: _Optional[_Iterable[bytes]] = ...) -> None: ...

class UpdateValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bytes
    def __init__(self, value: _Optional[bytes] = ...) -> None: ...

class Consistency(_message.Message):
    __slots__ = ("last", "distinguished")
    LAST_FIELD_NUMBER: _ClassVar[int]
    DISTINGUISHED_FIELD_NUMBER: _ClassVar[int]
    last: int
    distinguished: int
    def __init__(self, last: _Optional[int] = ..., distinguished: _Optional[int] = ...) -> None: ...

class CondensedTreeSearchResponse(_message.Message):
    __slots__ = ("vrf_proof", "search", "opening", "value")
    VRF_PROOF_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    OPENING_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    vrf_proof: bytes
    search: SearchProof
    opening: bytes
    value: UpdateValue
    def __init__(self, vrf_proof: _Optional[bytes] = ..., search: _Optional[_Union[SearchProof, _Mapping]] = ..., opening: _Optional[bytes] = ..., value: _Optional[_Union[UpdateValue, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("search_key", "value", "consistency")
    SEARCH_KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    search_key: bytes
    value: bytes
    consistency: Consistency
    def __init__(self, search_key: _Optional[bytes] = ..., value: _Optional[bytes] = ..., consistency: _Optional[_Union[Consistency, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("tree_head", "vrf_proof", "search", "opening")
    TREE_HEAD_FIELD_NUMBER: _ClassVar[int]
    VRF_PROOF_FIELD_NUMBER: _ClassVar[int]
    SEARCH_FIELD_NUMBER: _ClassVar[int]
    OPENING_FIELD_NUMBER: _ClassVar[int]
    tree_head: FullTreeHead
    vrf_proof: bytes
    search: SearchProof
    opening: bytes
    def __init__(self, tree_head: _Optional[_Union[FullTreeHead, _Mapping]] = ..., vrf_proof: _Optional[bytes] = ..., search: _Optional[_Union[SearchProof, _Mapping]] = ..., opening: _Optional[bytes] = ...) -> None: ...

class MonitorKey(_message.Message):
    __slots__ = ("search_key", "entry_position", "commitment_index")
    SEARCH_KEY_FIELD_NUMBER: _ClassVar[int]
    ENTRY_POSITION_FIELD_NUMBER: _ClassVar[int]
    COMMITMENT_INDEX_FIELD_NUMBER: _ClassVar[int]
    search_key: bytes
    entry_position: int
    commitment_index: bytes
    def __init__(self, search_key: _Optional[bytes] = ..., entry_position: _Optional[int] = ..., commitment_index: _Optional[bytes] = ...) -> None: ...

class MonitorRequest(_message.Message):
    __slots__ = ("keys", "consistency")
    KEYS_FIELD_NUMBER: _ClassVar[int]
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.RepeatedCompositeFieldContainer[MonitorKey]
    consistency: Consistency
    def __init__(self, keys: _Optional[_Iterable[_Union[MonitorKey, _Mapping]]] = ..., consistency: _Optional[_Union[Consistency, _Mapping]] = ...) -> None: ...

class MonitorProof(_message.Message):
    __slots__ = ("steps",)
    STEPS_FIELD_NUMBER: _ClassVar[int]
    steps: _containers.RepeatedCompositeFieldContainer[ProofStep]
    def __init__(self, steps: _Optional[_Iterable[_Union[ProofStep, _Mapping]]] = ...) -> None: ...

class MonitorResponse(_message.Message):
    __slots__ = ("tree_head", "proofs", "inclusion")
    TREE_HEAD_FIELD_NUMBER: _ClassVar[int]
    PROOFS_FIELD_NUMBER: _ClassVar[int]
    INCLUSION_FIELD_NUMBER: _ClassVar[int]
    tree_head: FullTreeHead
    proofs: _containers.RepeatedCompositeFieldContainer[MonitorProof]
    inclusion: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, tree_head: _Optional[_Union[FullTreeHead, _Mapping]] = ..., proofs: _Optional[_Iterable[_Union[MonitorProof, _Mapping]]] = ..., inclusion: _Optional[_Iterable[bytes]] = ...) -> None: ...
