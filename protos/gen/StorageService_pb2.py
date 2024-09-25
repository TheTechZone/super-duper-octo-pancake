# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: StorageService.proto
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
    'StorageService.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14StorageService.proto\x12\rsignalservice\"1\n\x0fStorageManifest\x12\x0f\n\x07version\x18\x01 \x01(\x04\x12\r\n\x05value\x18\x02 \x01(\x0c\")\n\x0bStorageItem\x12\x0b\n\x03key\x18\x01 \x01(\x0c\x12\r\n\x05value\x18\x02 \x01(\x0c\"9\n\x0cStorageItems\x12)\n\x05items\x18\x01 \x03(\x0b\x32\x1a.signalservice.StorageItem\" \n\rReadOperation\x12\x0f\n\x07readKey\x18\x01 \x03(\x0c\"\x97\x01\n\x0eWriteOperation\x12\x30\n\x08manifest\x18\x01 \x01(\x0b\x32\x1e.signalservice.StorageManifest\x12.\n\ninsertItem\x18\x02 \x03(\x0b\x32\x1a.signalservice.StorageItem\x12\x11\n\tdeleteKey\x18\x03 \x03(\x0c\x12\x10\n\x08\x63learAll\x18\x04 \x01(\x08\"\xc4\x02\n\x0eManifestRecord\x12\x0f\n\x07version\x18\x01 \x01(\x04\x12\x14\n\x0csourceDevice\x18\x03 \x01(\r\x12=\n\x0bidentifiers\x18\x02 \x03(\x0b\x32(.signalservice.ManifestRecord.Identifier\x1a\xcb\x01\n\nIdentifier\x12\x0b\n\x03raw\x18\x01 \x01(\x0c\x12;\n\x04type\x18\x02 \x01(\x0e\x32-.signalservice.ManifestRecord.Identifier.Type\"s\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07\x43ONTACT\x10\x01\x12\x0b\n\x07GROUPV1\x10\x02\x12\x0b\n\x07GROUPV2\x10\x03\x12\x0b\n\x07\x41\x43\x43OUNT\x10\x04\x12\x1b\n\x17STORY_DISTRIBUTION_LIST\x10\x05\x12\r\n\tCALL_LINK\x10\x07\"\xdd\x02\n\rStorageRecord\x12/\n\x07\x63ontact\x18\x01 \x01(\x0b\x32\x1c.signalservice.ContactRecordH\x00\x12/\n\x07groupV1\x18\x02 \x01(\x0b\x32\x1c.signalservice.GroupV1RecordH\x00\x12/\n\x07groupV2\x18\x03 \x01(\x0b\x32\x1c.signalservice.GroupV2RecordH\x00\x12/\n\x07\x61\x63\x63ount\x18\x04 \x01(\x0b\x32\x1c.signalservice.AccountRecordH\x00\x12K\n\x15storyDistributionList\x18\x05 \x01(\x0b\x32*.signalservice.StoryDistributionListRecordH\x00\x12\x31\n\x08\x63\x61llLink\x18\x07 \x01(\x0b\x32\x1d.signalservice.CallLinkRecordH\x00\x42\x08\n\x06record\"\x9a\x05\n\rContactRecord\x12\x0b\n\x03\x61\x63i\x18\x01 \x01(\t\x12\x0c\n\x04\x65\x31\x36\x34\x18\x02 \x01(\t\x12\x0b\n\x03pni\x18\x0f \x01(\t\x12\x12\n\nprofileKey\x18\x03 \x01(\x0c\x12\x13\n\x0bidentityKey\x18\x04 \x01(\x0c\x12\x41\n\ridentityState\x18\x05 \x01(\x0e\x32*.signalservice.ContactRecord.IdentityState\x12\x11\n\tgivenName\x18\x06 \x01(\t\x12\x12\n\nfamilyName\x18\x07 \x01(\t\x12\x10\n\x08username\x18\x08 \x01(\t\x12\x0f\n\x07\x62locked\x18\t \x01(\x08\x12\x13\n\x0bwhitelisted\x18\n \x01(\x08\x12\x10\n\x08\x61rchived\x18\x0b \x01(\x08\x12\x14\n\x0cmarkedUnread\x18\x0c \x01(\x08\x12\x1b\n\x13mutedUntilTimestamp\x18\r \x01(\x04\x12\x11\n\thideStory\x18\x0e \x01(\x08\x12\x1f\n\x17unregisteredAtTimestamp\x18\x10 \x01(\x04\x12\x17\n\x0fsystemGivenName\x18\x11 \x01(\t\x12\x18\n\x10systemFamilyName\x18\x12 \x01(\t\x12\x16\n\x0esystemNickname\x18\x13 \x01(\t\x12\x0e\n\x06hidden\x18\x14 \x01(\x08\x12\x1c\n\x14pniSignatureVerified\x18\x15 \x01(\x08\x12\x33\n\x08nickname\x18\x16 \x01(\x0b\x32!.signalservice.ContactRecord.Name\x12\x0c\n\x04note\x18\x17 \x01(\t\x1a%\n\x04Name\x12\r\n\x05given\x18\x01 \x01(\t\x12\x0e\n\x06\x66\x61mily\x18\x02 \x01(\t\":\n\rIdentityState\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0c\n\x08VERIFIED\x10\x01\x12\x0e\n\nUNVERIFIED\x10\x02\"\x86\x01\n\rGroupV1Record\x12\n\n\x02id\x18\x01 \x01(\x0c\x12\x0f\n\x07\x62locked\x18\x02 \x01(\x08\x12\x13\n\x0bwhitelisted\x18\x03 \x01(\x08\x12\x10\n\x08\x61rchived\x18\x04 \x01(\x08\x12\x14\n\x0cmarkedUnread\x18\x05 \x01(\x08\x12\x1b\n\x13mutedUntilTimestamp\x18\x06 \x01(\x04\"\xc8\x02\n\rGroupV2Record\x12\x11\n\tmasterKey\x18\x01 \x01(\x0c\x12\x0f\n\x07\x62locked\x18\x02 \x01(\x08\x12\x13\n\x0bwhitelisted\x18\x03 \x01(\x08\x12\x10\n\x08\x61rchived\x18\x04 \x01(\x08\x12\x14\n\x0cmarkedUnread\x18\x05 \x01(\x08\x12\x1b\n\x13mutedUntilTimestamp\x18\x06 \x01(\x04\x12$\n\x1c\x64ontNotifyForMentionsIfMuted\x18\x07 \x01(\x08\x12\x11\n\thideStory\x18\x08 \x01(\x08\x12\x41\n\rstorySendMode\x18\n \x01(\x0e\x32*.signalservice.GroupV2Record.StorySendMode\"7\n\rStorySendMode\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x0c\n\x08\x44ISABLED\x10\x01\x12\x0b\n\x07\x45NABLED\x10\x02J\x04\x08\t\x10\n\",\n\x08Payments\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12\x0f\n\x07\x65ntropy\x18\x02 \x01(\x0c\"\xd1\x0c\n\rAccountRecord\x12\x12\n\nprofileKey\x18\x01 \x01(\x0c\x12\x11\n\tgivenName\x18\x02 \x01(\t\x12\x12\n\nfamilyName\x18\x03 \x01(\t\x12\x15\n\ravatarUrlPath\x18\x04 \x01(\t\x12\x1a\n\x12noteToSelfArchived\x18\x05 \x01(\x08\x12\x14\n\x0creadReceipts\x18\x06 \x01(\x08\x12\x1e\n\x16sealedSenderIndicators\x18\x07 \x01(\x08\x12\x18\n\x10typingIndicators\x18\x08 \x01(\x08\x12\x1e\n\x16noteToSelfMarkedUnread\x18\n \x01(\x08\x12\x14\n\x0clinkPreviews\x18\x0b \x01(\x08\x12S\n\x16phoneNumberSharingMode\x18\x0c \x01(\x0e\x32\x33.signalservice.AccountRecord.PhoneNumberSharingMode\x12\x1b\n\x13unlistedPhoneNumber\x18\r \x01(\x08\x12L\n\x13pinnedConversations\x18\x0e \x03(\x0b\x32/.signalservice.AccountRecord.PinnedConversation\x12\x1c\n\x14preferContactAvatars\x18\x0f \x01(\x08\x12)\n\x08payments\x18\x10 \x01(\x0b\x32\x17.signalservice.Payments\x12\x1c\n\x14universalExpireTimer\x18\x11 \x01(\r\x12\x17\n\x0fprimarySendsSms\x18\x12 \x01(\x08\x12\x0c\n\x04\x65\x31\x36\x34\x18\x13 \x01(\t\x12\x1e\n\x16preferredReactionEmoji\x18\x14 \x03(\t\x12\x14\n\x0csubscriberId\x18\x15 \x01(\x0c\x12\x1e\n\x16subscriberCurrencyCode\x18\x16 \x01(\t\x12\x1e\n\x16\x64isplayBadgesOnProfile\x18\x17 \x01(\x08\x12%\n\x1dsubscriptionManuallyCancelled\x18\x18 \x01(\x08\x12\x1e\n\x16keepMutedChatsArchived\x18\x19 \x01(\x08\x12\x1e\n\x16hasSetMyStoriesPrivacy\x18\x1a \x01(\x08\x12 \n\x18hasViewedOnboardingStory\x18\x1b \x01(\x08\x12\x17\n\x0fstoriesDisabled\x18\x1d \x01(\x08\x12=\n\x18storyViewReceiptsEnabled\x18\x1e \x01(\x0e\x32\x1b.signalservice.OptionalBool\x12\'\n\x1fhasSeenGroupStoryEducationSheet\x18  \x01(\x08\x12\x10\n\x08username\x18! \x01(\t\x12&\n\x1ehasCompletedUsernameOnboarding\x18\" \x01(\x08\x12?\n\x0cusernameLink\x18# \x01(\x0b\x32).signalservice.AccountRecord.UsernameLink\x1a\xcd\x01\n\x12PinnedConversation\x12J\n\x07\x63ontact\x18\x01 \x01(\x0b\x32\x37.signalservice.AccountRecord.PinnedConversation.ContactH\x00\x12\x17\n\rlegacyGroupId\x18\x03 \x01(\x0cH\x00\x12\x18\n\x0egroupMasterKey\x18\x04 \x01(\x0cH\x00\x1a*\n\x07\x43ontact\x12\x11\n\tserviceId\x18\x01 \x01(\t\x12\x0c\n\x04\x65\x31\x36\x34\x18\x02 \x01(\tB\x0c\n\nidentifier\x1a\xde\x01\n\x0cUsernameLink\x12\x0f\n\x07\x65ntropy\x18\x01 \x01(\x0c\x12\x10\n\x08serverId\x18\x02 \x01(\x0c\x12>\n\x05\x63olor\x18\x03 \x01(\x0e\x32/.signalservice.AccountRecord.UsernameLink.Color\"k\n\x05\x43olor\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x08\n\x04\x42LUE\x10\x01\x12\t\n\x05WHITE\x10\x02\x12\x08\n\x04GREY\x10\x03\x12\t\n\x05OLIVE\x10\x04\x12\t\n\x05GREEN\x10\x05\x12\n\n\x06ORANGE\x10\x06\x12\x08\n\x04PINK\x10\x07\x12\n\n\x06PURPLE\x10\x08\"@\n\x16PhoneNumberSharingMode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tEVERYBODY\x10\x01\x12\n\n\x06NOBODY\x10\x02J\x04\x08\t\x10\nJ\x04\x08\x1c\x10\x1dJ\x04\x08\x1f\x10 \"\xa4\x01\n\x1bStoryDistributionListRecord\x12\x12\n\nidentifier\x18\x01 \x01(\x0c\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x1b\n\x13recipientServiceIds\x18\x03 \x03(\t\x12\x1a\n\x12\x64\x65letedAtTimestamp\x18\x04 \x01(\x04\x12\x15\n\rallowsReplies\x18\x05 \x01(\x08\x12\x13\n\x0bisBlockList\x18\x06 \x01(\x08\"U\n\x0e\x43\x61llLinkRecord\x12\x0f\n\x07rootKey\x18\x01 \x01(\x0c\x12\x14\n\x0c\x61\x64minPasskey\x18\x02 \x01(\x0c\x12\x1c\n\x14\x64\x65letedAtTimestampMs\x18\x03 \x01(\x04*4\n\x0cOptionalBool\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\x42<\n8org.whispersystems.signalservice.internal.storage.protosP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'StorageService_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n8org.whispersystems.signalservice.internal.storage.protosP\001'
  _globals['_OPTIONALBOOL']._serialized_start=4116
  _globals['_OPTIONALBOOL']._serialized_end=4168
  _globals['_STORAGEMANIFEST']._serialized_start=39
  _globals['_STORAGEMANIFEST']._serialized_end=88
  _globals['_STORAGEITEM']._serialized_start=90
  _globals['_STORAGEITEM']._serialized_end=131
  _globals['_STORAGEITEMS']._serialized_start=133
  _globals['_STORAGEITEMS']._serialized_end=190
  _globals['_READOPERATION']._serialized_start=192
  _globals['_READOPERATION']._serialized_end=224
  _globals['_WRITEOPERATION']._serialized_start=227
  _globals['_WRITEOPERATION']._serialized_end=378
  _globals['_MANIFESTRECORD']._serialized_start=381
  _globals['_MANIFESTRECORD']._serialized_end=705
  _globals['_MANIFESTRECORD_IDENTIFIER']._serialized_start=502
  _globals['_MANIFESTRECORD_IDENTIFIER']._serialized_end=705
  _globals['_MANIFESTRECORD_IDENTIFIER_TYPE']._serialized_start=590
  _globals['_MANIFESTRECORD_IDENTIFIER_TYPE']._serialized_end=705
  _globals['_STORAGERECORD']._serialized_start=708
  _globals['_STORAGERECORD']._serialized_end=1057
  _globals['_CONTACTRECORD']._serialized_start=1060
  _globals['_CONTACTRECORD']._serialized_end=1726
  _globals['_CONTACTRECORD_NAME']._serialized_start=1629
  _globals['_CONTACTRECORD_NAME']._serialized_end=1666
  _globals['_CONTACTRECORD_IDENTITYSTATE']._serialized_start=1668
  _globals['_CONTACTRECORD_IDENTITYSTATE']._serialized_end=1726
  _globals['_GROUPV1RECORD']._serialized_start=1729
  _globals['_GROUPV1RECORD']._serialized_end=1863
  _globals['_GROUPV2RECORD']._serialized_start=1866
  _globals['_GROUPV2RECORD']._serialized_end=2194
  _globals['_GROUPV2RECORD_STORYSENDMODE']._serialized_start=2133
  _globals['_GROUPV2RECORD_STORYSENDMODE']._serialized_end=2188
  _globals['_PAYMENTS']._serialized_start=2196
  _globals['_PAYMENTS']._serialized_end=2240
  _globals['_ACCOUNTRECORD']._serialized_start=2243
  _globals['_ACCOUNTRECORD']._serialized_end=3860
  _globals['_ACCOUNTRECORD_PINNEDCONVERSATION']._serialized_start=3346
  _globals['_ACCOUNTRECORD_PINNEDCONVERSATION']._serialized_end=3551
  _globals['_ACCOUNTRECORD_PINNEDCONVERSATION_CONTACT']._serialized_start=3495
  _globals['_ACCOUNTRECORD_PINNEDCONVERSATION_CONTACT']._serialized_end=3537
  _globals['_ACCOUNTRECORD_USERNAMELINK']._serialized_start=3554
  _globals['_ACCOUNTRECORD_USERNAMELINK']._serialized_end=3776
  _globals['_ACCOUNTRECORD_USERNAMELINK_COLOR']._serialized_start=3669
  _globals['_ACCOUNTRECORD_USERNAMELINK_COLOR']._serialized_end=3776
  _globals['_ACCOUNTRECORD_PHONENUMBERSHARINGMODE']._serialized_start=3778
  _globals['_ACCOUNTRECORD_PHONENUMBERSHARINGMODE']._serialized_end=3842
  _globals['_STORYDISTRIBUTIONLISTRECORD']._serialized_start=3863
  _globals['_STORYDISTRIBUTIONLISTRECORD']._serialized_end=4027
  _globals['_CALLLINKRECORD']._serialized_start=4029
  _globals['_CALLLINKRECORD']._serialized_end=4114
# @@protoc_insertion_point(module_scope)
