from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LeastActiveLinkedDevice(_message.Message):
    __slots__ = ("name", "lastActiveTimestamp")
    NAME_FIELD_NUMBER: _ClassVar[int]
    LASTACTIVETIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    name: str
    lastActiveTimestamp: int
    def __init__(self, name: _Optional[str] = ..., lastActiveTimestamp: _Optional[int] = ...) -> None: ...

class ArchiveUploadProgressState(_message.Message):
    __slots__ = ("state", "backupPhase", "frameExportCount", "frameTotalCount", "backupFileUploadedBytes", "backupFileTotalBytes", "mediaUploadedBytes", "mediaTotalBytes")
    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        None: _ClassVar[ArchiveUploadProgressState.State]
        Export: _ClassVar[ArchiveUploadProgressState.State]
        UploadBackupFile: _ClassVar[ArchiveUploadProgressState.State]
        UploadMedia: _ClassVar[ArchiveUploadProgressState.State]
    None: ArchiveUploadProgressState.State
    Export: ArchiveUploadProgressState.State
    UploadBackupFile: ArchiveUploadProgressState.State
    UploadMedia: ArchiveUploadProgressState.State
    class BackupPhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BackupPhaseNone: _ClassVar[ArchiveUploadProgressState.BackupPhase]
        Account: _ClassVar[ArchiveUploadProgressState.BackupPhase]
        Recipient: _ClassVar[ArchiveUploadProgressState.BackupPhase]
        Thread: _ClassVar[ArchiveUploadProgressState.BackupPhase]
        Call: _ClassVar[ArchiveUploadProgressState.BackupPhase]
        Sticker: _ClassVar[ArchiveUploadProgressState.BackupPhase]
        Message: _ClassVar[ArchiveUploadProgressState.BackupPhase]
        NotificationProfile: _ClassVar[ArchiveUploadProgressState.BackupPhase]
        ChatFolder: _ClassVar[ArchiveUploadProgressState.BackupPhase]
    BackupPhaseNone: ArchiveUploadProgressState.BackupPhase
    Account: ArchiveUploadProgressState.BackupPhase
    Recipient: ArchiveUploadProgressState.BackupPhase
    Thread: ArchiveUploadProgressState.BackupPhase
    Call: ArchiveUploadProgressState.BackupPhase
    Sticker: ArchiveUploadProgressState.BackupPhase
    Message: ArchiveUploadProgressState.BackupPhase
    NotificationProfile: ArchiveUploadProgressState.BackupPhase
    ChatFolder: ArchiveUploadProgressState.BackupPhase
    STATE_FIELD_NUMBER: _ClassVar[int]
    BACKUPPHASE_FIELD_NUMBER: _ClassVar[int]
    FRAMEEXPORTCOUNT_FIELD_NUMBER: _ClassVar[int]
    FRAMETOTALCOUNT_FIELD_NUMBER: _ClassVar[int]
    BACKUPFILEUPLOADEDBYTES_FIELD_NUMBER: _ClassVar[int]
    BACKUPFILETOTALBYTES_FIELD_NUMBER: _ClassVar[int]
    MEDIAUPLOADEDBYTES_FIELD_NUMBER: _ClassVar[int]
    MEDIATOTALBYTES_FIELD_NUMBER: _ClassVar[int]
    state: ArchiveUploadProgressState.State
    backupPhase: ArchiveUploadProgressState.BackupPhase
    frameExportCount: int
    frameTotalCount: int
    backupFileUploadedBytes: int
    backupFileTotalBytes: int
    mediaUploadedBytes: int
    mediaTotalBytes: int
    def __init__(self, state: _Optional[_Union[ArchiveUploadProgressState.State, str]] = ..., backupPhase: _Optional[_Union[ArchiveUploadProgressState.BackupPhase, str]] = ..., frameExportCount: _Optional[int] = ..., frameTotalCount: _Optional[int] = ..., backupFileUploadedBytes: _Optional[int] = ..., backupFileTotalBytes: _Optional[int] = ..., mediaUploadedBytes: _Optional[int] = ..., mediaTotalBytes: _Optional[int] = ...) -> None: ...
