# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: DecryptedGroups.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Groups_pb2 as Groups__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x44\x65\x63ryptedGroups.proto\x1a\x0cGroups.proto\"\x7f\n\x0f\x44\x65\x63ryptedMember\x12\x10\n\x08\x61\x63iBytes\x18\x01 \x01(\x0c\x12\x1a\n\x04role\x18\x02 \x01(\x0e\x32\x0c.Member.Role\x12\x12\n\nprofileKey\x18\x03 \x01(\x0c\x12\x18\n\x10joinedAtRevision\x18\x05 \x01(\r\x12\x10\n\x08pniBytes\x18\x06 \x01(\x0c\"\x90\x01\n\x16\x44\x65\x63ryptedPendingMember\x12\x16\n\x0eserviceIdBytes\x18\x01 \x01(\x0c\x12\x1a\n\x04role\x18\x02 \x01(\x0e\x32\x0c.Member.Role\x12\x12\n\naddedByAci\x18\x03 \x01(\x0c\x12\x11\n\ttimestamp\x18\x04 \x01(\x04\x12\x1b\n\x13serviceIdCipherText\x18\x05 \x01(\x0c\"T\n\x19\x44\x65\x63ryptedRequestingMember\x12\x10\n\x08\x61\x63iBytes\x18\x01 \x01(\x0c\x12\x12\n\nprofileKey\x18\x02 \x01(\x0c\x12\x11\n\ttimestamp\x18\x04 \x01(\x04\"B\n\x15\x44\x65\x63ryptedBannedMember\x12\x16\n\x0eserviceIdBytes\x18\x01 \x01(\x0c\x12\x11\n\ttimestamp\x18\x02 \x01(\x04\"T\n\x1d\x44\x65\x63ryptedPendingMemberRemoval\x12\x16\n\x0eserviceIdBytes\x18\x01 \x01(\x0c\x12\x1b\n\x13serviceIdCipherText\x18\x02 \x01(\x0c\"F\n\x16\x44\x65\x63ryptedApproveMember\x12\x10\n\x08\x61\x63iBytes\x18\x01 \x01(\x0c\x12\x1a\n\x04role\x18\x02 \x01(\x0e\x32\x0c.Member.Role\"I\n\x19\x44\x65\x63ryptedModifyMemberRole\x12\x10\n\x08\x61\x63iBytes\x18\x01 \x01(\x0c\x12\x1a\n\x04role\x18\x02 \x01(\x0e\x32\x0c.Member.Role\"\xb3\x03\n\x0e\x44\x65\x63ryptedGroup\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x03 \x01(\t\x12\x32\n\x19\x64isappearingMessagesTimer\x18\x04 \x01(\x0b\x32\x0f.DecryptedTimer\x12%\n\raccessControl\x18\x05 \x01(\x0b\x32\x0e.AccessControl\x12\x10\n\x08revision\x18\x06 \x01(\r\x12!\n\x07members\x18\x07 \x03(\x0b\x32\x10.DecryptedMember\x12/\n\x0ependingMembers\x18\x08 \x03(\x0b\x32\x17.DecryptedPendingMember\x12\x35\n\x11requestingMembers\x18\t \x03(\x0b\x32\x1a.DecryptedRequestingMember\x12\x1a\n\x12inviteLinkPassword\x18\n \x01(\x0c\x12\x13\n\x0b\x64\x65scription\x18\x0b \x01(\t\x12*\n\x13isAnnouncementGroup\x18\x0c \x01(\x0e\x32\r.EnabledState\x12-\n\rbannedMembers\x18\r \x03(\x0b\x32\x16.DecryptedBannedMember\"\xd3\x08\n\x14\x44\x65\x63ryptedGroupChange\x12\x1c\n\x14\x65\x64itorServiceIdBytes\x18\x01 \x01(\x0c\x12\x10\n\x08revision\x18\x02 \x01(\r\x12$\n\nnewMembers\x18\x03 \x03(\x0b\x32\x10.DecryptedMember\x12\x15\n\rdeleteMembers\x18\x04 \x03(\x0c\x12\x35\n\x11modifyMemberRoles\x18\x05 \x03(\x0b\x32\x1a.DecryptedModifyMemberRole\x12-\n\x13modifiedProfileKeys\x18\x06 \x03(\x0b\x32\x10.DecryptedMember\x12\x32\n\x11newPendingMembers\x18\x07 \x03(\x0b\x32\x17.DecryptedPendingMember\x12<\n\x14\x64\x65letePendingMembers\x18\x08 \x03(\x0b\x32\x1e.DecryptedPendingMemberRemoval\x12/\n\x15promotePendingMembers\x18\t \x03(\x0b\x32\x10.DecryptedMember\x12\"\n\x08newTitle\x18\n \x01(\x0b\x32\x10.DecryptedString\x12#\n\tnewAvatar\x18\x0b \x01(\x0b\x32\x10.DecryptedString\x12!\n\x08newTimer\x18\x0c \x01(\x0b\x32\x0f.DecryptedTimer\x12\x39\n\x12newAttributeAccess\x18\r \x01(\x0e\x32\x1d.AccessControl.AccessRequired\x12\x36\n\x0fnewMemberAccess\x18\x0e \x01(\x0e\x32\x1d.AccessControl.AccessRequired\x12:\n\x13newInviteLinkAccess\x18\x0f \x01(\x0e\x32\x1d.AccessControl.AccessRequired\x12\x38\n\x14newRequestingMembers\x18\x10 \x03(\x0b\x32\x1a.DecryptedRequestingMember\x12\x1f\n\x17\x64\x65leteRequestingMembers\x18\x11 \x03(\x0c\x12\x39\n\x18promoteRequestingMembers\x18\x12 \x03(\x0b\x32\x17.DecryptedApproveMember\x12\x1d\n\x15newInviteLinkPassword\x18\x13 \x01(\x0c\x12(\n\x0enewDescription\x18\x14 \x01(\x0b\x32\x10.DecryptedString\x12-\n\x16newIsAnnouncementGroup\x18\x15 \x01(\x0e\x32\r.EnabledState\x12\x30\n\x10newBannedMembers\x18\x16 \x03(\x0b\x32\x16.DecryptedBannedMember\x12\x33\n\x13\x64\x65leteBannedMembers\x18\x17 \x03(\x0b\x32\x16.DecryptedBannedMember\x12\x35\n\x1bpromotePendingPniAciMembers\x18\x18 \x03(\x0b\x32\x10.DecryptedMember\" \n\x0f\x44\x65\x63ryptedString\x12\r\n\x05value\x18\x01 \x01(\t\"\"\n\x0e\x44\x65\x63ryptedTimer\x12\x10\n\x08\x64uration\x18\x01 \x01(\r\"\xe8\x01\n\x16\x44\x65\x63ryptedGroupJoinInfo\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x03 \x01(\t\x12\x13\n\x0bmemberCount\x18\x04 \x01(\r\x12\x38\n\x11\x61\x64\x64\x46romInviteLink\x18\x05 \x01(\x0e\x32\x1d.AccessControl.AccessRequired\x12\x10\n\x08revision\x18\x06 \x01(\r\x12\x1c\n\x14pendingAdminApproval\x18\x07 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t\x12\x1b\n\x13isAnnouncementGroup\x18\t \x01(\x08*6\n\x0c\x45nabledState\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07\x45NABLED\x10\x01\x12\x0c\n\x08\x44ISABLED\x10\x02\x42\x31\n-org.signal.storageservice.protos.groups.localP\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'DecryptedGroups_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n-org.signal.storageservice.protos.groups.localP\001'
  _globals['_ENABLEDSTATE']._serialized_start=2555
  _globals['_ENABLEDSTATE']._serialized_end=2609
  _globals['_DECRYPTEDMEMBER']._serialized_start=39
  _globals['_DECRYPTEDMEMBER']._serialized_end=166
  _globals['_DECRYPTEDPENDINGMEMBER']._serialized_start=169
  _globals['_DECRYPTEDPENDINGMEMBER']._serialized_end=313
  _globals['_DECRYPTEDREQUESTINGMEMBER']._serialized_start=315
  _globals['_DECRYPTEDREQUESTINGMEMBER']._serialized_end=399
  _globals['_DECRYPTEDBANNEDMEMBER']._serialized_start=401
  _globals['_DECRYPTEDBANNEDMEMBER']._serialized_end=467
  _globals['_DECRYPTEDPENDINGMEMBERREMOVAL']._serialized_start=469
  _globals['_DECRYPTEDPENDINGMEMBERREMOVAL']._serialized_end=553
  _globals['_DECRYPTEDAPPROVEMEMBER']._serialized_start=555
  _globals['_DECRYPTEDAPPROVEMEMBER']._serialized_end=625
  _globals['_DECRYPTEDMODIFYMEMBERROLE']._serialized_start=627
  _globals['_DECRYPTEDMODIFYMEMBERROLE']._serialized_end=700
  _globals['_DECRYPTEDGROUP']._serialized_start=703
  _globals['_DECRYPTEDGROUP']._serialized_end=1138
  _globals['_DECRYPTEDGROUPCHANGE']._serialized_start=1141
  _globals['_DECRYPTEDGROUPCHANGE']._serialized_end=2248
  _globals['_DECRYPTEDSTRING']._serialized_start=2250
  _globals['_DECRYPTEDSTRING']._serialized_end=2282
  _globals['_DECRYPTEDTIMER']._serialized_start=2284
  _globals['_DECRYPTEDTIMER']._serialized_end=2318
  _globals['_DECRYPTEDGROUPJOININFO']._serialized_start=2321
  _globals['_DECRYPTEDGROUPJOININFO']._serialized_end=2553
# @@protoc_insertion_point(module_scope)
