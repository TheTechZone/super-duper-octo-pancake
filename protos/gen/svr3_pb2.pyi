from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ("create", "evaluate", "remove", "query")
    CREATE_FIELD_NUMBER: _ClassVar[int]
    EVALUATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    create: CreateRequest
    evaluate: EvaluateRequest
    remove: RemoveRequest
    query: QueryRequest
    def __init__(self, create: _Optional[_Union[CreateRequest, _Mapping]] = ..., evaluate: _Optional[_Union[EvaluateRequest, _Mapping]] = ..., remove: _Optional[_Union[RemoveRequest, _Mapping]] = ..., query: _Optional[_Union[QueryRequest, _Mapping]] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("create", "evaluate", "remove", "query")
    CREATE_FIELD_NUMBER: _ClassVar[int]
    EVALUATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    create: CreateResponse
    evaluate: EvaluateResponse
    remove: RemoveResponse
    query: QueryResponse
    def __init__(self, create: _Optional[_Union[CreateResponse, _Mapping]] = ..., evaluate: _Optional[_Union[EvaluateResponse, _Mapping]] = ..., remove: _Optional[_Union[RemoveResponse, _Mapping]] = ..., query: _Optional[_Union[QueryResponse, _Mapping]] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("max_tries", "blinded_element")
    MAX_TRIES_FIELD_NUMBER: _ClassVar[int]
    BLINDED_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    max_tries: int
    blinded_element: bytes
    def __init__(self, max_tries: _Optional[int] = ..., blinded_element: _Optional[bytes] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("status", "evaluated_element")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSET: _ClassVar[CreateResponse.Status]
        OK: _ClassVar[CreateResponse.Status]
        INVALID_REQUEST: _ClassVar[CreateResponse.Status]
        ERROR: _ClassVar[CreateResponse.Status]
    UNSET: CreateResponse.Status
    OK: CreateResponse.Status
    INVALID_REQUEST: CreateResponse.Status
    ERROR: CreateResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    status: CreateResponse.Status
    evaluated_element: bytes
    def __init__(self, status: _Optional[_Union[CreateResponse.Status, str]] = ..., evaluated_element: _Optional[bytes] = ...) -> None: ...

class EvaluateRequest(_message.Message):
    __slots__ = ("blinded_element",)
    BLINDED_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    blinded_element: bytes
    def __init__(self, blinded_element: _Optional[bytes] = ...) -> None: ...

class EvaluateResponse(_message.Message):
    __slots__ = ("status", "evaluated_element", "tries_remaining")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSET: _ClassVar[EvaluateResponse.Status]
        OK: _ClassVar[EvaluateResponse.Status]
        MISSING: _ClassVar[EvaluateResponse.Status]
        INVALID_REQUEST: _ClassVar[EvaluateResponse.Status]
        ERROR: _ClassVar[EvaluateResponse.Status]
    UNSET: EvaluateResponse.Status
    OK: EvaluateResponse.Status
    MISSING: EvaluateResponse.Status
    INVALID_REQUEST: EvaluateResponse.Status
    ERROR: EvaluateResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    EVALUATED_ELEMENT_FIELD_NUMBER: _ClassVar[int]
    TRIES_REMAINING_FIELD_NUMBER: _ClassVar[int]
    status: EvaluateResponse.Status
    evaluated_element: bytes
    tries_remaining: int
    def __init__(self, status: _Optional[_Union[EvaluateResponse.Status, str]] = ..., evaluated_element: _Optional[bytes] = ..., tries_remaining: _Optional[int] = ...) -> None: ...

class RemoveRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryResponse(_message.Message):
    __slots__ = ("status", "tries_remaining")
    class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSET: _ClassVar[QueryResponse.Status]
        OK: _ClassVar[QueryResponse.Status]
        MISSING: _ClassVar[QueryResponse.Status]
    UNSET: QueryResponse.Status
    OK: QueryResponse.Status
    MISSING: QueryResponse.Status
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TRIES_REMAINING_FIELD_NUMBER: _ClassVar[int]
    status: QueryResponse.Status
    tries_remaining: int
    def __init__(self, status: _Optional[_Union[QueryResponse.Status, str]] = ..., tries_remaining: _Optional[int] = ...) -> None: ...
