from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OptionalBool(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNSET: _ClassVar[OptionalBool]
    ENABLED: _ClassVar[OptionalBool]
    DISABLED: _ClassVar[OptionalBool]

class AvatarColor(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    A100: _ClassVar[AvatarColor]
    A110: _ClassVar[AvatarColor]
    A120: _ClassVar[AvatarColor]
    A130: _ClassVar[AvatarColor]
    A140: _ClassVar[AvatarColor]
    A150: _ClassVar[AvatarColor]
    A160: _ClassVar[AvatarColor]
    A170: _ClassVar[AvatarColor]
    A180: _ClassVar[AvatarColor]
    A190: _ClassVar[AvatarColor]
    A200: _ClassVar[AvatarColor]
    A210: _ClassVar[AvatarColor]
UNSET: OptionalBool
ENABLED: OptionalBool
DISABLED: OptionalBool
A100: AvatarColor
A110: AvatarColor
A120: AvatarColor
A130: AvatarColor
A140: AvatarColor
A150: AvatarColor
A160: AvatarColor
A170: AvatarColor
A180: AvatarColor
A190: AvatarColor
A200: AvatarColor
A210: AvatarColor

class StorageManifest(_message.Message):
    __slots__ = ("version", "value")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    version: int
    value: bytes
    def __init__(self, version: _Optional[int] = ..., value: _Optional[bytes] = ...) -> None: ...

class StorageItem(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: bytes
    value: bytes
    def __init__(self, key: _Optional[bytes] = ..., value: _Optional[bytes] = ...) -> None: ...

class StorageItems(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[StorageItem]
    def __init__(self, items: _Optional[_Iterable[_Union[StorageItem, _Mapping]]] = ...) -> None: ...

class ReadOperation(_message.Message):
    __slots__ = ("readKey",)
    READKEY_FIELD_NUMBER: _ClassVar[int]
    readKey: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, readKey: _Optional[_Iterable[bytes]] = ...) -> None: ...

class WriteOperation(_message.Message):
    __slots__ = ("manifest", "insertItem", "deleteKey", "clearAll")
    MANIFEST_FIELD_NUMBER: _ClassVar[int]
    INSERTITEM_FIELD_NUMBER: _ClassVar[int]
    DELETEKEY_FIELD_NUMBER: _ClassVar[int]
    CLEARALL_FIELD_NUMBER: _ClassVar[int]
    manifest: StorageManifest
    insertItem: _containers.RepeatedCompositeFieldContainer[StorageItem]
    deleteKey: _containers.RepeatedScalarFieldContainer[bytes]
    clearAll: bool
    def __init__(self, manifest: _Optional[_Union[StorageManifest, _Mapping]] = ..., insertItem: _Optional[_Iterable[_Union[StorageItem, _Mapping]]] = ..., deleteKey: _Optional[_Iterable[bytes]] = ..., clearAll: bool = ...) -> None: ...

class ManifestRecord(_message.Message):
    __slots__ = ("version", "sourceDevice", "identifiers", "recordIkm")
    class Identifier(_message.Message):
        __slots__ = ("raw", "type")
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[ManifestRecord.Identifier.Type]
            CONTACT: _ClassVar[ManifestRecord.Identifier.Type]
            GROUPV1: _ClassVar[ManifestRecord.Identifier.Type]
            GROUPV2: _ClassVar[ManifestRecord.Identifier.Type]
            ACCOUNT: _ClassVar[ManifestRecord.Identifier.Type]
            STORY_DISTRIBUTION_LIST: _ClassVar[ManifestRecord.Identifier.Type]
            CALL_LINK: _ClassVar[ManifestRecord.Identifier.Type]
            CHAT_FOLDER: _ClassVar[ManifestRecord.Identifier.Type]
        UNKNOWN: ManifestRecord.Identifier.Type
        CONTACT: ManifestRecord.Identifier.Type
        GROUPV1: ManifestRecord.Identifier.Type
        GROUPV2: ManifestRecord.Identifier.Type
        ACCOUNT: ManifestRecord.Identifier.Type
        STORY_DISTRIBUTION_LIST: ManifestRecord.Identifier.Type
        CALL_LINK: ManifestRecord.Identifier.Type
        CHAT_FOLDER: ManifestRecord.Identifier.Type
        RAW_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        raw: bytes
        type: ManifestRecord.Identifier.Type
        def __init__(self, raw: _Optional[bytes] = ..., type: _Optional[_Union[ManifestRecord.Identifier.Type, str]] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SOURCEDEVICE_FIELD_NUMBER: _ClassVar[int]
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    RECORDIKM_FIELD_NUMBER: _ClassVar[int]
    version: int
    sourceDevice: int
    identifiers: _containers.RepeatedCompositeFieldContainer[ManifestRecord.Identifier]
    recordIkm: bytes
    def __init__(self, version: _Optional[int] = ..., sourceDevice: _Optional[int] = ..., identifiers: _Optional[_Iterable[_Union[ManifestRecord.Identifier, _Mapping]]] = ..., recordIkm: _Optional[bytes] = ...) -> None: ...

class StorageRecord(_message.Message):
    __slots__ = ("contact", "groupV1", "groupV2", "account", "storyDistributionList", "callLink", "chatFolder")
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    GROUPV1_FIELD_NUMBER: _ClassVar[int]
    GROUPV2_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    STORYDISTRIBUTIONLIST_FIELD_NUMBER: _ClassVar[int]
    CALLLINK_FIELD_NUMBER: _ClassVar[int]
    CHATFOLDER_FIELD_NUMBER: _ClassVar[int]
    contact: ContactRecord
    groupV1: GroupV1Record
    groupV2: GroupV2Record
    account: AccountRecord
    storyDistributionList: StoryDistributionListRecord
    callLink: CallLinkRecord
    chatFolder: ChatFolderRecord
    def __init__(self, contact: _Optional[_Union[ContactRecord, _Mapping]] = ..., groupV1: _Optional[_Union[GroupV1Record, _Mapping]] = ..., groupV2: _Optional[_Union[GroupV2Record, _Mapping]] = ..., account: _Optional[_Union[AccountRecord, _Mapping]] = ..., storyDistributionList: _Optional[_Union[StoryDistributionListRecord, _Mapping]] = ..., callLink: _Optional[_Union[CallLinkRecord, _Mapping]] = ..., chatFolder: _Optional[_Union[ChatFolderRecord, _Mapping]] = ...) -> None: ...

class ContactRecord(_message.Message):
    __slots__ = ("aci", "e164", "pni", "profileKey", "identityKey", "identityState", "givenName", "familyName", "username", "blocked", "whitelisted", "archived", "markedUnread", "mutedUntilTimestamp", "hideStory", "unregisteredAtTimestamp", "systemGivenName", "systemFamilyName", "systemNickname", "hidden", "pniSignatureVerified", "nickname", "note", "avatarColor")
    class IdentityState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[ContactRecord.IdentityState]
        VERIFIED: _ClassVar[ContactRecord.IdentityState]
        UNVERIFIED: _ClassVar[ContactRecord.IdentityState]
    DEFAULT: ContactRecord.IdentityState
    VERIFIED: ContactRecord.IdentityState
    UNVERIFIED: ContactRecord.IdentityState
    class Name(_message.Message):
        __slots__ = ("given", "family")
        GIVEN_FIELD_NUMBER: _ClassVar[int]
        FAMILY_FIELD_NUMBER: _ClassVar[int]
        given: str
        family: str
        def __init__(self, given: _Optional[str] = ..., family: _Optional[str] = ...) -> None: ...
    ACI_FIELD_NUMBER: _ClassVar[int]
    E164_FIELD_NUMBER: _ClassVar[int]
    PNI_FIELD_NUMBER: _ClassVar[int]
    PROFILEKEY_FIELD_NUMBER: _ClassVar[int]
    IDENTITYKEY_FIELD_NUMBER: _ClassVar[int]
    IDENTITYSTATE_FIELD_NUMBER: _ClassVar[int]
    GIVENNAME_FIELD_NUMBER: _ClassVar[int]
    FAMILYNAME_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    WHITELISTED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    MARKEDUNREAD_FIELD_NUMBER: _ClassVar[int]
    MUTEDUNTILTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    HIDESTORY_FIELD_NUMBER: _ClassVar[int]
    UNREGISTEREDATTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SYSTEMGIVENNAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEMFAMILYNAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEMNICKNAME_FIELD_NUMBER: _ClassVar[int]
    HIDDEN_FIELD_NUMBER: _ClassVar[int]
    PNISIGNATUREVERIFIED_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    NOTE_FIELD_NUMBER: _ClassVar[int]
    AVATARCOLOR_FIELD_NUMBER: _ClassVar[int]
    aci: str
    e164: str
    pni: str
    profileKey: bytes
    identityKey: bytes
    identityState: ContactRecord.IdentityState
    givenName: str
    familyName: str
    username: str
    blocked: bool
    whitelisted: bool
    archived: bool
    markedUnread: bool
    mutedUntilTimestamp: int
    hideStory: bool
    unregisteredAtTimestamp: int
    systemGivenName: str
    systemFamilyName: str
    systemNickname: str
    hidden: bool
    pniSignatureVerified: bool
    nickname: ContactRecord.Name
    note: str
    avatarColor: AvatarColor
    def __init__(self, aci: _Optional[str] = ..., e164: _Optional[str] = ..., pni: _Optional[str] = ..., profileKey: _Optional[bytes] = ..., identityKey: _Optional[bytes] = ..., identityState: _Optional[_Union[ContactRecord.IdentityState, str]] = ..., givenName: _Optional[str] = ..., familyName: _Optional[str] = ..., username: _Optional[str] = ..., blocked: bool = ..., whitelisted: bool = ..., archived: bool = ..., markedUnread: bool = ..., mutedUntilTimestamp: _Optional[int] = ..., hideStory: bool = ..., unregisteredAtTimestamp: _Optional[int] = ..., systemGivenName: _Optional[str] = ..., systemFamilyName: _Optional[str] = ..., systemNickname: _Optional[str] = ..., hidden: bool = ..., pniSignatureVerified: bool = ..., nickname: _Optional[_Union[ContactRecord.Name, _Mapping]] = ..., note: _Optional[str] = ..., avatarColor: _Optional[_Union[AvatarColor, str]] = ...) -> None: ...

class GroupV1Record(_message.Message):
    __slots__ = ("id", "blocked", "whitelisted", "archived", "markedUnread", "mutedUntilTimestamp")
    ID_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    WHITELISTED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    MARKEDUNREAD_FIELD_NUMBER: _ClassVar[int]
    MUTEDUNTILTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    id: bytes
    blocked: bool
    whitelisted: bool
    archived: bool
    markedUnread: bool
    mutedUntilTimestamp: int
    def __init__(self, id: _Optional[bytes] = ..., blocked: bool = ..., whitelisted: bool = ..., archived: bool = ..., markedUnread: bool = ..., mutedUntilTimestamp: _Optional[int] = ...) -> None: ...

class GroupV2Record(_message.Message):
    __slots__ = ("masterKey", "blocked", "whitelisted", "archived", "markedUnread", "mutedUntilTimestamp", "dontNotifyForMentionsIfMuted", "hideStory", "storySendMode", "avatarColor")
    class StorySendMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEFAULT: _ClassVar[GroupV2Record.StorySendMode]
        DISABLED: _ClassVar[GroupV2Record.StorySendMode]
        ENABLED: _ClassVar[GroupV2Record.StorySendMode]
    DEFAULT: GroupV2Record.StorySendMode
    DISABLED: GroupV2Record.StorySendMode
    ENABLED: GroupV2Record.StorySendMode
    MASTERKEY_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    WHITELISTED_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    MARKEDUNREAD_FIELD_NUMBER: _ClassVar[int]
    MUTEDUNTILTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    DONTNOTIFYFORMENTIONSIFMUTED_FIELD_NUMBER: _ClassVar[int]
    HIDESTORY_FIELD_NUMBER: _ClassVar[int]
    STORYSENDMODE_FIELD_NUMBER: _ClassVar[int]
    AVATARCOLOR_FIELD_NUMBER: _ClassVar[int]
    masterKey: bytes
    blocked: bool
    whitelisted: bool
    archived: bool
    markedUnread: bool
    mutedUntilTimestamp: int
    dontNotifyForMentionsIfMuted: bool
    hideStory: bool
    storySendMode: GroupV2Record.StorySendMode
    avatarColor: AvatarColor
    def __init__(self, masterKey: _Optional[bytes] = ..., blocked: bool = ..., whitelisted: bool = ..., archived: bool = ..., markedUnread: bool = ..., mutedUntilTimestamp: _Optional[int] = ..., dontNotifyForMentionsIfMuted: bool = ..., hideStory: bool = ..., storySendMode: _Optional[_Union[GroupV2Record.StorySendMode, str]] = ..., avatarColor: _Optional[_Union[AvatarColor, str]] = ...) -> None: ...

class Payments(_message.Message):
    __slots__ = ("enabled", "entropy")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    ENTROPY_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    entropy: bytes
    def __init__(self, enabled: bool = ..., entropy: _Optional[bytes] = ...) -> None: ...

class AccountRecord(_message.Message):
    __slots__ = ("profileKey", "givenName", "familyName", "avatarUrlPath", "noteToSelfArchived", "readReceipts", "sealedSenderIndicators", "typingIndicators", "noteToSelfMarkedUnread", "linkPreviews", "phoneNumberSharingMode", "unlistedPhoneNumber", "pinnedConversations", "preferContactAvatars", "payments", "universalExpireTimer", "primarySendsSms", "e164", "preferredReactionEmoji", "subscriberId", "subscriberCurrencyCode", "displayBadgesOnProfile", "subscriptionManuallyCancelled", "keepMutedChatsArchived", "hasSetMyStoriesPrivacy", "hasViewedOnboardingStory", "storiesDisabled", "storyViewReceiptsEnabled", "hasSeenGroupStoryEducationSheet", "username", "hasCompletedUsernameOnboarding", "usernameLink", "hasBackup", "backupTier", "backupSubscriberData", "avatarColor")
    class PhoneNumberSharingMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[AccountRecord.PhoneNumberSharingMode]
        EVERYBODY: _ClassVar[AccountRecord.PhoneNumberSharingMode]
        NOBODY: _ClassVar[AccountRecord.PhoneNumberSharingMode]
    UNKNOWN: AccountRecord.PhoneNumberSharingMode
    EVERYBODY: AccountRecord.PhoneNumberSharingMode
    NOBODY: AccountRecord.PhoneNumberSharingMode
    class PinnedConversation(_message.Message):
        __slots__ = ("contact", "legacyGroupId", "groupMasterKey")
        class Contact(_message.Message):
            __slots__ = ("serviceId", "e164")
            SERVICEID_FIELD_NUMBER: _ClassVar[int]
            E164_FIELD_NUMBER: _ClassVar[int]
            serviceId: str
            e164: str
            def __init__(self, serviceId: _Optional[str] = ..., e164: _Optional[str] = ...) -> None: ...
        CONTACT_FIELD_NUMBER: _ClassVar[int]
        LEGACYGROUPID_FIELD_NUMBER: _ClassVar[int]
        GROUPMASTERKEY_FIELD_NUMBER: _ClassVar[int]
        contact: AccountRecord.PinnedConversation.Contact
        legacyGroupId: bytes
        groupMasterKey: bytes
        def __init__(self, contact: _Optional[_Union[AccountRecord.PinnedConversation.Contact, _Mapping]] = ..., legacyGroupId: _Optional[bytes] = ..., groupMasterKey: _Optional[bytes] = ...) -> None: ...
    class UsernameLink(_message.Message):
        __slots__ = ("entropy", "serverId", "color")
        class Color(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[AccountRecord.UsernameLink.Color]
            BLUE: _ClassVar[AccountRecord.UsernameLink.Color]
            WHITE: _ClassVar[AccountRecord.UsernameLink.Color]
            GREY: _ClassVar[AccountRecord.UsernameLink.Color]
            OLIVE: _ClassVar[AccountRecord.UsernameLink.Color]
            GREEN: _ClassVar[AccountRecord.UsernameLink.Color]
            ORANGE: _ClassVar[AccountRecord.UsernameLink.Color]
            PINK: _ClassVar[AccountRecord.UsernameLink.Color]
            PURPLE: _ClassVar[AccountRecord.UsernameLink.Color]
        UNKNOWN: AccountRecord.UsernameLink.Color
        BLUE: AccountRecord.UsernameLink.Color
        WHITE: AccountRecord.UsernameLink.Color
        GREY: AccountRecord.UsernameLink.Color
        OLIVE: AccountRecord.UsernameLink.Color
        GREEN: AccountRecord.UsernameLink.Color
        ORANGE: AccountRecord.UsernameLink.Color
        PINK: AccountRecord.UsernameLink.Color
        PURPLE: AccountRecord.UsernameLink.Color
        ENTROPY_FIELD_NUMBER: _ClassVar[int]
        SERVERID_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        entropy: bytes
        serverId: bytes
        color: AccountRecord.UsernameLink.Color
        def __init__(self, entropy: _Optional[bytes] = ..., serverId: _Optional[bytes] = ..., color: _Optional[_Union[AccountRecord.UsernameLink.Color, str]] = ...) -> None: ...
    class IAPSubscriberData(_message.Message):
        __slots__ = ("subscriberId", "purchaseToken", "originalTransactionId")
        SUBSCRIBERID_FIELD_NUMBER: _ClassVar[int]
        PURCHASETOKEN_FIELD_NUMBER: _ClassVar[int]
        ORIGINALTRANSACTIONID_FIELD_NUMBER: _ClassVar[int]
        subscriberId: bytes
        purchaseToken: str
        originalTransactionId: int
        def __init__(self, subscriberId: _Optional[bytes] = ..., purchaseToken: _Optional[str] = ..., originalTransactionId: _Optional[int] = ...) -> None: ...
    PROFILEKEY_FIELD_NUMBER: _ClassVar[int]
    GIVENNAME_FIELD_NUMBER: _ClassVar[int]
    FAMILYNAME_FIELD_NUMBER: _ClassVar[int]
    AVATARURLPATH_FIELD_NUMBER: _ClassVar[int]
    NOTETOSELFARCHIVED_FIELD_NUMBER: _ClassVar[int]
    READRECEIPTS_FIELD_NUMBER: _ClassVar[int]
    SEALEDSENDERINDICATORS_FIELD_NUMBER: _ClassVar[int]
    TYPINGINDICATORS_FIELD_NUMBER: _ClassVar[int]
    NOTETOSELFMARKEDUNREAD_FIELD_NUMBER: _ClassVar[int]
    LINKPREVIEWS_FIELD_NUMBER: _ClassVar[int]
    PHONENUMBERSHARINGMODE_FIELD_NUMBER: _ClassVar[int]
    UNLISTEDPHONENUMBER_FIELD_NUMBER: _ClassVar[int]
    PINNEDCONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    PREFERCONTACTAVATARS_FIELD_NUMBER: _ClassVar[int]
    PAYMENTS_FIELD_NUMBER: _ClassVar[int]
    UNIVERSALEXPIRETIMER_FIELD_NUMBER: _ClassVar[int]
    PRIMARYSENDSSMS_FIELD_NUMBER: _ClassVar[int]
    E164_FIELD_NUMBER: _ClassVar[int]
    PREFERREDREACTIONEMOJI_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBERID_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBERCURRENCYCODE_FIELD_NUMBER: _ClassVar[int]
    DISPLAYBADGESONPROFILE_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIPTIONMANUALLYCANCELLED_FIELD_NUMBER: _ClassVar[int]
    KEEPMUTEDCHATSARCHIVED_FIELD_NUMBER: _ClassVar[int]
    HASSETMYSTORIESPRIVACY_FIELD_NUMBER: _ClassVar[int]
    HASVIEWEDONBOARDINGSTORY_FIELD_NUMBER: _ClassVar[int]
    STORIESDISABLED_FIELD_NUMBER: _ClassVar[int]
    STORYVIEWRECEIPTSENABLED_FIELD_NUMBER: _ClassVar[int]
    HASSEENGROUPSTORYEDUCATIONSHEET_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    HASCOMPLETEDUSERNAMEONBOARDING_FIELD_NUMBER: _ClassVar[int]
    USERNAMELINK_FIELD_NUMBER: _ClassVar[int]
    HASBACKUP_FIELD_NUMBER: _ClassVar[int]
    BACKUPTIER_FIELD_NUMBER: _ClassVar[int]
    BACKUPSUBSCRIBERDATA_FIELD_NUMBER: _ClassVar[int]
    AVATARCOLOR_FIELD_NUMBER: _ClassVar[int]
    profileKey: bytes
    givenName: str
    familyName: str
    avatarUrlPath: str
    noteToSelfArchived: bool
    readReceipts: bool
    sealedSenderIndicators: bool
    typingIndicators: bool
    noteToSelfMarkedUnread: bool
    linkPreviews: bool
    phoneNumberSharingMode: AccountRecord.PhoneNumberSharingMode
    unlistedPhoneNumber: bool
    pinnedConversations: _containers.RepeatedCompositeFieldContainer[AccountRecord.PinnedConversation]
    preferContactAvatars: bool
    payments: Payments
    universalExpireTimer: int
    primarySendsSms: bool
    e164: str
    preferredReactionEmoji: _containers.RepeatedScalarFieldContainer[str]
    subscriberId: bytes
    subscriberCurrencyCode: str
    displayBadgesOnProfile: bool
    subscriptionManuallyCancelled: bool
    keepMutedChatsArchived: bool
    hasSetMyStoriesPrivacy: bool
    hasViewedOnboardingStory: bool
    storiesDisabled: bool
    storyViewReceiptsEnabled: OptionalBool
    hasSeenGroupStoryEducationSheet: bool
    username: str
    hasCompletedUsernameOnboarding: bool
    usernameLink: AccountRecord.UsernameLink
    hasBackup: bool
    backupTier: int
    backupSubscriberData: AccountRecord.IAPSubscriberData
    avatarColor: AvatarColor
    def __init__(self, profileKey: _Optional[bytes] = ..., givenName: _Optional[str] = ..., familyName: _Optional[str] = ..., avatarUrlPath: _Optional[str] = ..., noteToSelfArchived: bool = ..., readReceipts: bool = ..., sealedSenderIndicators: bool = ..., typingIndicators: bool = ..., noteToSelfMarkedUnread: bool = ..., linkPreviews: bool = ..., phoneNumberSharingMode: _Optional[_Union[AccountRecord.PhoneNumberSharingMode, str]] = ..., unlistedPhoneNumber: bool = ..., pinnedConversations: _Optional[_Iterable[_Union[AccountRecord.PinnedConversation, _Mapping]]] = ..., preferContactAvatars: bool = ..., payments: _Optional[_Union[Payments, _Mapping]] = ..., universalExpireTimer: _Optional[int] = ..., primarySendsSms: bool = ..., e164: _Optional[str] = ..., preferredReactionEmoji: _Optional[_Iterable[str]] = ..., subscriberId: _Optional[bytes] = ..., subscriberCurrencyCode: _Optional[str] = ..., displayBadgesOnProfile: bool = ..., subscriptionManuallyCancelled: bool = ..., keepMutedChatsArchived: bool = ..., hasSetMyStoriesPrivacy: bool = ..., hasViewedOnboardingStory: bool = ..., storiesDisabled: bool = ..., storyViewReceiptsEnabled: _Optional[_Union[OptionalBool, str]] = ..., hasSeenGroupStoryEducationSheet: bool = ..., username: _Optional[str] = ..., hasCompletedUsernameOnboarding: bool = ..., usernameLink: _Optional[_Union[AccountRecord.UsernameLink, _Mapping]] = ..., hasBackup: bool = ..., backupTier: _Optional[int] = ..., backupSubscriberData: _Optional[_Union[AccountRecord.IAPSubscriberData, _Mapping]] = ..., avatarColor: _Optional[_Union[AvatarColor, str]] = ...) -> None: ...

class StoryDistributionListRecord(_message.Message):
    __slots__ = ("identifier", "name", "recipientServiceIds", "deletedAtTimestamp", "allowsReplies", "isBlockList")
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RECIPIENTSERVICEIDS_FIELD_NUMBER: _ClassVar[int]
    DELETEDATTIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ALLOWSREPLIES_FIELD_NUMBER: _ClassVar[int]
    ISBLOCKLIST_FIELD_NUMBER: _ClassVar[int]
    identifier: bytes
    name: str
    recipientServiceIds: _containers.RepeatedScalarFieldContainer[str]
    deletedAtTimestamp: int
    allowsReplies: bool
    isBlockList: bool
    def __init__(self, identifier: _Optional[bytes] = ..., name: _Optional[str] = ..., recipientServiceIds: _Optional[_Iterable[str]] = ..., deletedAtTimestamp: _Optional[int] = ..., allowsReplies: bool = ..., isBlockList: bool = ...) -> None: ...

class CallLinkRecord(_message.Message):
    __slots__ = ("rootKey", "adminPasskey", "deletedAtTimestampMs")
    ROOTKEY_FIELD_NUMBER: _ClassVar[int]
    ADMINPASSKEY_FIELD_NUMBER: _ClassVar[int]
    DELETEDATTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    rootKey: bytes
    adminPasskey: bytes
    deletedAtTimestampMs: int
    def __init__(self, rootKey: _Optional[bytes] = ..., adminPasskey: _Optional[bytes] = ..., deletedAtTimestampMs: _Optional[int] = ...) -> None: ...

class ChatFolderRecord(_message.Message):
    __slots__ = ("identifier", "name", "position", "showOnlyUnread", "showMutedChats", "includeAllIndividualChats", "includeAllGroupChats", "folderType", "includedRecipients", "excludedRecipients", "deletedAtTimestampMs")
    class FolderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN: _ClassVar[ChatFolderRecord.FolderType]
        ALL: _ClassVar[ChatFolderRecord.FolderType]
        CUSTOM: _ClassVar[ChatFolderRecord.FolderType]
    UNKNOWN: ChatFolderRecord.FolderType
    ALL: ChatFolderRecord.FolderType
    CUSTOM: ChatFolderRecord.FolderType
    class Recipient(_message.Message):
        __slots__ = ("contact", "legacyGroupId", "groupMasterKey")
        class Contact(_message.Message):
            __slots__ = ("serviceId", "e164")
            SERVICEID_FIELD_NUMBER: _ClassVar[int]
            E164_FIELD_NUMBER: _ClassVar[int]
            serviceId: str
            e164: str
            def __init__(self, serviceId: _Optional[str] = ..., e164: _Optional[str] = ...) -> None: ...
        CONTACT_FIELD_NUMBER: _ClassVar[int]
        LEGACYGROUPID_FIELD_NUMBER: _ClassVar[int]
        GROUPMASTERKEY_FIELD_NUMBER: _ClassVar[int]
        contact: ChatFolderRecord.Recipient.Contact
        legacyGroupId: bytes
        groupMasterKey: bytes
        def __init__(self, contact: _Optional[_Union[ChatFolderRecord.Recipient.Contact, _Mapping]] = ..., legacyGroupId: _Optional[bytes] = ..., groupMasterKey: _Optional[bytes] = ...) -> None: ...
    IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    POSITION_FIELD_NUMBER: _ClassVar[int]
    SHOWONLYUNREAD_FIELD_NUMBER: _ClassVar[int]
    SHOWMUTEDCHATS_FIELD_NUMBER: _ClassVar[int]
    INCLUDEALLINDIVIDUALCHATS_FIELD_NUMBER: _ClassVar[int]
    INCLUDEALLGROUPCHATS_FIELD_NUMBER: _ClassVar[int]
    FOLDERTYPE_FIELD_NUMBER: _ClassVar[int]
    INCLUDEDRECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDEDRECIPIENTS_FIELD_NUMBER: _ClassVar[int]
    DELETEDATTIMESTAMPMS_FIELD_NUMBER: _ClassVar[int]
    identifier: bytes
    name: str
    position: int
    showOnlyUnread: bool
    showMutedChats: bool
    includeAllIndividualChats: bool
    includeAllGroupChats: bool
    folderType: ChatFolderRecord.FolderType
    includedRecipients: _containers.RepeatedCompositeFieldContainer[ChatFolderRecord.Recipient]
    excludedRecipients: _containers.RepeatedCompositeFieldContainer[ChatFolderRecord.Recipient]
    deletedAtTimestampMs: int
    def __init__(self, identifier: _Optional[bytes] = ..., name: _Optional[str] = ..., position: _Optional[int] = ..., showOnlyUnread: bool = ..., showMutedChats: bool = ..., includeAllIndividualChats: bool = ..., includeAllGroupChats: bool = ..., folderType: _Optional[_Union[ChatFolderRecord.FolderType, str]] = ..., includedRecipients: _Optional[_Iterable[_Union[ChatFolderRecord.Recipient, _Mapping]]] = ..., excludedRecipients: _Optional[_Iterable[_Union[ChatFolderRecord.Recipient, _Mapping]]] = ..., deletedAtTimestampMs: _Optional[int] = ...) -> None: ...
