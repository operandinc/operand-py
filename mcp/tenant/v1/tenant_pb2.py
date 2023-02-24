# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tenant/v1/tenant.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16tenant/v1/tenant.proto\x12\ttenant.v1\x1a\x1fgoogle/protobuf/timestamp.proto\"\x17\n\x15\x41uthorizedUserRequest\"=\n\x16\x41uthorizedUserResponse\x12#\n\x04user\x18\x01 \x01(\x0b\x32\x0f.tenant.v1.UserR\x04user\"\xa5\x01\n\x0bUserProfile\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12#\n\remail_address\x18\x02 \x01(\tR\x0c\x65mailAddress\x12\"\n\nfirst_name\x18\x03 \x01(\tH\x00R\tfirstName\x88\x01\x01\x12 \n\tlast_name\x18\x04 \x01(\tH\x01R\x08lastName\x88\x01\x01\x42\r\n\x0b_first_nameB\x0c\n\n_last_name\"\xfc\x01\n\x04User\x12\x30\n\x07profile\x18\x01 \x01(\x0b\x32\x16.tenant.v1.UserProfileR\x07profile\x12\x39\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12\x1c\n\tdeveloper\x18\x03 \x01(\x08R\tdeveloper\x12H\n\x11subscription_plan\x18\x04 \x01(\x0e\x32\x1b.tenant.v1.SubscriptionPlanR\x10subscriptionPlan\x12\x1f\n\x0busage_addon\x18\x05 \x01(\x08R\nusageAddon\")\n\x13\x43reateAPIKeyRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\"\xa2\x01\n\x06\x41PIKey\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x39\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\x12\x14\n\x04\x66ull\x18\x04 \x01(\tH\x00R\x04\x66ull\x12\x1a\n\x07partial\x18\x05 \x01(\tH\x00R\x07partialB\x07\n\x05token\";\n\x14\x43reateAPIKeyResponse\x12#\n\x03key\x18\x01 \x01(\x0b\x32\x11.tenant.v1.APIKeyR\x03key\"\x14\n\x12ListAPIKeysRequest\"<\n\x13ListAPIKeysResponse\x12%\n\x04keys\x18\x01 \x03(\x0b\x32\x11.tenant.v1.APIKeyR\x04keys\"%\n\x13\x44\x65leteAPIKeyRequest\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\"\x16\n\x14\x44\x65leteAPIKeyResponse\"\xa7\x01\n\x11UpdateUserRequest\x12\"\n\nfirst_name\x18\x01 \x01(\tH\x00R\tfirstName\x88\x01\x01\x12 \n\tlast_name\x18\x02 \x01(\tH\x01R\x08lastName\x88\x01\x01\x12!\n\tdeveloper\x18\x03 \x01(\x08H\x02R\tdeveloper\x88\x01\x01\x42\r\n\x0b_first_nameB\x0c\n\n_last_nameB\x0c\n\n_developer\"9\n\x12UpdateUserResponse\x12#\n\x04user\x18\x01 \x01(\x0b\x32\x0f.tenant.v1.UserR\x04user\"2\n\x0cGroupProfile\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x12\n\x04name\x18\x02 \x01(\tR\x04name\"u\n\x05Group\x12\x31\n\x07profile\x18\x01 \x01(\x0b\x32\x17.tenant.v1.GroupProfileR\x07profile\x12\x39\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\"k\n\x10OAuthLinkRequest\x12\x34\n\x08provider\x18\x01 \x01(\x0e\x32\x18.tenant.v1.OAuthProviderR\x08provider\x12!\n\x0credirect_url\x18\x02 \x01(\tR\x0bredirectUrl\"\xaf\x01\n\tOAuthLink\x12\x0e\n\x02id\x18\x01 \x01(\tR\x02id\x12\x39\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12\x34\n\x08provider\x18\x03 \x01(\x0e\x32\x18.tenant.v1.OAuthProviderR\x08provider\x12!\n\x0c\x61\x63\x63\x65ss_token\x18\x04 \x01(\tR\x0b\x61\x63\x63\x65ssToken\"l\n\x11OAuthLinkResponse\x12\x1d\n\tsetup_url\x18\x01 \x01(\tH\x00R\x08setupUrl\x12,\n\x05state\x18\x02 \x01(\x0b\x32\x14.tenant.v1.OAuthLinkH\x00R\x05stateB\n\n\x08response\"\x0e\n\x0cUsageRequest\"\xd7\x01\n\rUsageResponse\x12\x39\n\x07records\x18\x01 \x03(\x0b\x32\x1f.tenant.v1.UsageResponse.RecordR\x07records\x1a\x8a\x01\n\x06Record\x12.\n\x04kind\x18\x01 \x01(\x0e\x32\x1a.tenant.v1.UsageRecordKindR\x04kind\x12#\n\rcurrent_value\x18\x02 \x01(\x03R\x0c\x63urrentValue\x12+\n\x11\x61\x63\x63umulated_cents\x18\x03 \x01(\x03R\x10\x61\x63\x63umulatedCents\"\xf6\x01\n\x19UpdateSubscriptionRequest\x12/\n\x04plan\x18\x01 \x01(\x0e\x32\x1b.tenant.v1.SubscriptionPlanR\x04plan\x12\x1f\n\x0busage_addon\x18\x02 \x01(\x08R\nusageAddon\x12\x35\n\x14\x66orce_billing_portal\x18\x03 \x01(\x08H\x00R\x12\x66orceBillingPortal\x88\x01\x01\x12&\n\x0credirect_url\x18\x04 \x01(\tH\x01R\x0bredirectUrl\x88\x01\x01\x42\x17\n\x15_force_billing_portalB\x0f\n\r_redirect_url\"\xc5\x01\n\x1aUpdateSubscriptionResponse\x12@\n\x04none\x18\x01 \x01(\x0b\x32*.tenant.v1.UpdateSubscriptionResponse.NoneH\x00R\x04none\x12#\n\x0c\x63heckout_url\x18\x02 \x01(\tH\x00R\x0b\x63heckoutUrl\x12.\n\x12\x62illing_portal_url\x18\x03 \x01(\tH\x00R\x10\x62illingPortalUrl\x1a\x06\n\x04NoneB\x08\n\x06\x61\x63tion*l\n\x10SubscriptionPlan\x12!\n\x1dSUBSCRIPTION_PLAN_UNSPECIFIED\x10\x00\x12\x1a\n\x16SUBSCRIPTION_PLAN_FREE\x10\x01\x12\x19\n\x15SUBSCRIPTION_PLAN_PRO\x10\x02*L\n\rOAuthProvider\x12\x1f\n\x1bO_AUTH_PROVIDER_UNSPECIFIED\x10\x00\x12\x1a\n\x16O_AUTH_PROVIDER_GITHUB\x10\x01*\xce\x01\n\x0fUsageRecordKind\x12!\n\x1dUSAGE_RECORD_KIND_UNSPECIFIED\x10\x00\x12\'\n#USAGE_RECORD_KIND_RAW_STORAGE_BYTES\x10\x01\x12)\n%USAGE_RECORD_KIND_INDEX_STORAGE_BYTES\x10\x02\x12$\n USAGE_RECORD_KIND_SEARCH_QUERIES\x10\x03\x12\x1e\n\x1aUSAGE_RECORD_KIND_CONVERSE\x10\x04\x32\x98\x05\n\rTenantService\x12W\n\x0e\x41uthorizedUser\x12 .tenant.v1.AuthorizedUserRequest\x1a!.tenant.v1.AuthorizedUserResponse\"\x00\x12Q\n\x0c\x43reateAPIKey\x12\x1e.tenant.v1.CreateAPIKeyRequest\x1a\x1f.tenant.v1.CreateAPIKeyResponse\"\x00\x12N\n\x0bListAPIKeys\x12\x1d.tenant.v1.ListAPIKeysRequest\x1a\x1e.tenant.v1.ListAPIKeysResponse\"\x00\x12Q\n\x0c\x44\x65leteAPIKey\x12\x1e.tenant.v1.DeleteAPIKeyRequest\x1a\x1f.tenant.v1.DeleteAPIKeyResponse\"\x00\x12H\n\tOAuthLink\x12\x1b.tenant.v1.OAuthLinkRequest\x1a\x1c.tenant.v1.OAuthLinkResponse\"\x00\x12K\n\nUpdateUser\x12\x1c.tenant.v1.UpdateUserRequest\x1a\x1d.tenant.v1.UpdateUserResponse\"\x00\x12<\n\x05Usage\x12\x17.tenant.v1.UsageRequest\x1a\x18.tenant.v1.UsageResponse\"\x00\x12\x63\n\x12UpdateSubscription\x12$.tenant.v1.UpdateSubscriptionRequest\x1a%.tenant.v1.UpdateSubscriptionResponse\"\x00\x42\x8e\x01\n\rcom.tenant.v1B\x0bTenantProtoP\x01Z+mcp.operand.ai/gen/proto/tenant/v1;tenantv1\xa2\x02\x03TXX\xaa\x02\tTenant.V1\xca\x02\tTenant\\V1\xe2\x02\x15Tenant\\V1\\GPBMetadata\xea\x02\nTenant::V1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tenant.v1.tenant_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\rcom.tenant.v1B\013TenantProtoP\001Z+mcp.operand.ai/gen/proto/tenant/v1;tenantv1\242\002\003TXX\252\002\tTenant.V1\312\002\tTenant\\V1\342\002\025Tenant\\V1\\GPBMetadata\352\002\nTenant::V1'
  _globals['_SUBSCRIPTIONPLAN']._serialized_start=2477
  _globals['_SUBSCRIPTIONPLAN']._serialized_end=2585
  _globals['_OAUTHPROVIDER']._serialized_start=2587
  _globals['_OAUTHPROVIDER']._serialized_end=2663
  _globals['_USAGERECORDKIND']._serialized_start=2666
  _globals['_USAGERECORDKIND']._serialized_end=2872
  _globals['_AUTHORIZEDUSERREQUEST']._serialized_start=70
  _globals['_AUTHORIZEDUSERREQUEST']._serialized_end=93
  _globals['_AUTHORIZEDUSERRESPONSE']._serialized_start=95
  _globals['_AUTHORIZEDUSERRESPONSE']._serialized_end=156
  _globals['_USERPROFILE']._serialized_start=159
  _globals['_USERPROFILE']._serialized_end=324
  _globals['_USER']._serialized_start=327
  _globals['_USER']._serialized_end=579
  _globals['_CREATEAPIKEYREQUEST']._serialized_start=581
  _globals['_CREATEAPIKEYREQUEST']._serialized_end=622
  _globals['_APIKEY']._serialized_start=625
  _globals['_APIKEY']._serialized_end=787
  _globals['_CREATEAPIKEYRESPONSE']._serialized_start=789
  _globals['_CREATEAPIKEYRESPONSE']._serialized_end=848
  _globals['_LISTAPIKEYSREQUEST']._serialized_start=850
  _globals['_LISTAPIKEYSREQUEST']._serialized_end=870
  _globals['_LISTAPIKEYSRESPONSE']._serialized_start=872
  _globals['_LISTAPIKEYSRESPONSE']._serialized_end=932
  _globals['_DELETEAPIKEYREQUEST']._serialized_start=934
  _globals['_DELETEAPIKEYREQUEST']._serialized_end=971
  _globals['_DELETEAPIKEYRESPONSE']._serialized_start=973
  _globals['_DELETEAPIKEYRESPONSE']._serialized_end=995
  _globals['_UPDATEUSERREQUEST']._serialized_start=998
  _globals['_UPDATEUSERREQUEST']._serialized_end=1165
  _globals['_UPDATEUSERRESPONSE']._serialized_start=1167
  _globals['_UPDATEUSERRESPONSE']._serialized_end=1224
  _globals['_GROUPPROFILE']._serialized_start=1226
  _globals['_GROUPPROFILE']._serialized_end=1276
  _globals['_GROUP']._serialized_start=1278
  _globals['_GROUP']._serialized_end=1395
  _globals['_OAUTHLINKREQUEST']._serialized_start=1397
  _globals['_OAUTHLINKREQUEST']._serialized_end=1504
  _globals['_OAUTHLINK']._serialized_start=1507
  _globals['_OAUTHLINK']._serialized_end=1682
  _globals['_OAUTHLINKRESPONSE']._serialized_start=1684
  _globals['_OAUTHLINKRESPONSE']._serialized_end=1792
  _globals['_USAGEREQUEST']._serialized_start=1794
  _globals['_USAGEREQUEST']._serialized_end=1808
  _globals['_USAGERESPONSE']._serialized_start=1811
  _globals['_USAGERESPONSE']._serialized_end=2026
  _globals['_USAGERESPONSE_RECORD']._serialized_start=1888
  _globals['_USAGERESPONSE_RECORD']._serialized_end=2026
  _globals['_UPDATESUBSCRIPTIONREQUEST']._serialized_start=2029
  _globals['_UPDATESUBSCRIPTIONREQUEST']._serialized_end=2275
  _globals['_UPDATESUBSCRIPTIONRESPONSE']._serialized_start=2278
  _globals['_UPDATESUBSCRIPTIONRESPONSE']._serialized_end=2475
  _globals['_UPDATESUBSCRIPTIONRESPONSE_NONE']._serialized_start=2459
  _globals['_UPDATESUBSCRIPTIONRESPONSE_NONE']._serialized_end=2465
  _globals['_TENANTSERVICE']._serialized_start=2875
  _globals['_TENANTSERVICE']._serialized_end=3539
# @@protoc_insertion_point(module_scope)
