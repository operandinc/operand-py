# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: operand/v1/index.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from operand.v1 import object_pb2 as operand_dot_v1_dot_object__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16operand/v1/index.proto\x12\noperand.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17operand/v1/object.proto\"\xd7\x01\n\x0cIndexOptions\x12(\n\rinclude_owner\x18\x01 \x01(\x08H\x00R\x0cincludeOwner\x88\x01\x01\x12\x36\n\x14include_subscription\x18\x02 \x01(\x08H\x01R\x13includeSubscription\x88\x01\x01\x12(\n\rinclude_stats\x18\x03 \x01(\x08H\x02R\x0cincludeStats\x88\x01\x01\x42\x10\n\x0e_include_ownerB\x17\n\x15_include_subscriptionB\x10\n\x0e_include_stats\"\xd7\x01\n\x12\x43reateIndexRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x16\n\x06public\x18\x03 \x01(\x08R\x06public\x12\x37\n\x07options\x18\x04 \x01(\x0b\x32\x18.operand.v1.IndexOptionsH\x00R\x07options\x88\x01\x01\x12 \n\timage_url\x18\x05 \x01(\tH\x01R\x08imageUrl\x88\x01\x01\x42\n\n\x08_optionsB\x0c\n\n_image_url\"o\n\x0cSubscription\x12\x39\n\ncreated_at\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12$\n\rnotifications\x18\x02 \x01(\x08R\rnotifications\".\n\nIndexStats\x12 \n\x0bsubscribers\x18\x01 \x01(\x05R\x0bsubscribers\"\xa6\x02\n\x0bUserProfile\x12\x1b\n\tpublic_id\x18\x01 \x01(\tR\x08publicId\x12\x19\n\x05\x65mail\x18\x02 \x01(\tH\x00R\x05\x65mail\x88\x01\x01\x12\x1b\n\x06handle\x18\x03 \x01(\tH\x01R\x06handle\x88\x01\x01\x12\x39\n\ncreated_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12\x17\n\x04name\x18\x05 \x01(\tH\x02R\x04name\x88\x01\x01\x12\x15\n\x03\x62io\x18\x06 \x01(\tH\x03R\x03\x62io\x88\x01\x01\x12\"\n\navatar_url\x18\x07 \x01(\tH\x04R\tavatarUrl\x88\x01\x01\x42\x08\n\x06_emailB\t\n\x07_handleB\x07\n\x05_nameB\x06\n\x04_bioB\r\n\x0b_avatar_url\"\xac\x03\n\x05Index\x12\x1b\n\tpublic_id\x18\x01 \x01(\tR\x08publicId\x12\x32\n\x05owner\x18\x02 \x01(\x0b\x32\x17.operand.v1.UserProfileH\x00R\x05owner\x88\x01\x01\x12\x39\n\ncreated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12\x16\n\x06public\x18\x04 \x01(\x08R\x06public\x12\x12\n\x04name\x18\x05 \x01(\tR\x04name\x12 \n\x0b\x64\x65scription\x18\x06 \x01(\tR\x0b\x64\x65scription\x12\x41\n\x0csubscription\x18\x07 \x01(\x0b\x32\x18.operand.v1.SubscriptionH\x01R\x0csubscription\x88\x01\x01\x12\x31\n\x05stats\x18\x08 \x01(\x0b\x32\x16.operand.v1.IndexStatsH\x02R\x05stats\x88\x01\x01\x12 \n\timage_url\x18\t \x01(\tH\x03R\x08imageUrl\x88\x01\x01\x42\x08\n\x06_ownerB\x0f\n\r_subscriptionB\x08\n\x06_statsB\x0c\n\n_image_url\">\n\x13\x43reateIndexResponse\x12\'\n\x05index\x18\x01 \x01(\x0b\x32\x11.operand.v1.IndexR\x05index\"\x94\x01\n\x12ListIndexesRequest\x12\'\n\rowned_by_user\x18\x01 \x01(\tH\x00R\x0bownedByUser\x88\x01\x01\x12\x37\n\x07options\x18\x02 \x01(\x0b\x32\x18.operand.v1.IndexOptionsH\x01R\x07options\x88\x01\x01\x42\x10\n\x0e_owned_by_userB\n\n\x08_options\"B\n\x13ListIndexesResponse\x12+\n\x07indexes\x18\x01 \x03(\x0b\x32\x11.operand.v1.IndexR\x07indexes\"s\n\x0fGetIndexRequest\x12\x1b\n\tpublic_id\x18\x01 \x01(\tR\x08publicId\x12\x37\n\x07options\x18\x02 \x01(\x0b\x32\x18.operand.v1.IndexOptionsH\x00R\x07options\x88\x01\x01\x42\n\n\x08_options\";\n\x10GetIndexResponse\x12\'\n\x05index\x18\x01 \x01(\x0b\x32\x11.operand.v1.IndexR\x05index\"\xa7\x02\n\x12UpdateIndexRequest\x12\x1b\n\tpublic_id\x18\x01 \x01(\tR\x08publicId\x12\x17\n\x04name\x18\x02 \x01(\tH\x00R\x04name\x88\x01\x01\x12%\n\x0b\x64\x65scription\x18\x03 \x01(\tH\x01R\x0b\x64\x65scription\x88\x01\x01\x12\x1b\n\x06public\x18\x04 \x01(\x08H\x02R\x06public\x88\x01\x01\x12\x37\n\x07options\x18\x05 \x01(\x0b\x32\x18.operand.v1.IndexOptionsH\x03R\x07options\x88\x01\x01\x12 \n\timage_url\x18\x06 \x01(\tH\x04R\x08imageUrl\x88\x01\x01\x42\x07\n\x05_nameB\x0e\n\x0c_descriptionB\t\n\x07_publicB\n\n\x08_optionsB\x0c\n\n_image_url\">\n\x13UpdateIndexResponse\x12\'\n\x05index\x18\x01 \x01(\x0b\x32\x11.operand.v1.IndexR\x05index\"1\n\x12\x44\x65leteIndexRequest\x12\x1b\n\tpublic_id\x18\x01 \x01(\tR\x08publicId\"\x15\n\x13\x44\x65leteIndexResponse\"\x85\x01\n\x14SubscriptionsRequest\x12\x1c\n\x07user_id\x18\x01 \x01(\tH\x00R\x06userId\x88\x01\x01\x12\x37\n\x07options\x18\x02 \x01(\x0b\x32\x18.operand.v1.IndexOptionsH\x01R\x07options\x88\x01\x01\x42\n\n\x08_user_idB\n\n\x08_options\"D\n\x15SubscriptionsResponse\x12+\n\x07indexes\x18\x01 \x03(\x0b\x32\x11.operand.v1.IndexR\x07indexes\"l\n\x10SubscribeRequest\x12\x1b\n\tpublic_id\x18\x01 \x01(\tR\x08publicId\x12)\n\rnotifications\x18\x02 \x01(\x08H\x00R\rnotifications\x88\x01\x01\x42\x10\n\x0e_notifications\"Q\n\x11SubscribeResponse\x12<\n\x0csubscription\x18\x01 \x01(\x0b\x32\x18.operand.v1.SubscriptionR\x0csubscription\"1\n\x12UnsubscribeRequest\x12\x1b\n\tpublic_id\x18\x01 \x01(\tR\x08publicId\"\x15\n\x13UnsubscribeResponse\"3\n\x14SubscribersOfRequest\x12\x1b\n\tpublic_id\x18\x01 \x01(\tR\x08publicId\"R\n\x15SubscribersOfResponse\x12\x39\n\x0bsubscribers\x18\x01 \x03(\x0b\x32\x17.operand.v1.UserProfileR\x0bsubscribers\"9\n\x1c\x41vailableExplorationsRequest\x12\x19\n\x08index_id\x18\x01 \x01(\tR\x07indexId\"R\n\x1d\x41vailableExplorationsResponse\x12\x31\n\x05kinds\x18\x01 \x03(\x0e\x32\x1b.operand.v1.ExplorationKindR\x05kinds\"h\n\x15\x45xplorationParameters\x12G\n\x08\x63oncepts\x18\x01 \x01(\x0b\x32).operand.v1.ConceptsExplorationParametersH\x00R\x08\x63onceptsB\x06\n\x04kind\"\xbf\x02\n\x1d\x43onceptsExplorationParameters\x12\x1f\n\x0btarget_size\x18\x01 \x01(\x05R\ntargetSize\x12Z\n\rsummary_kinds\x18\x02 \x03(\x0e\x32\x35.operand.v1.ConceptsExplorationParameters.SummaryKindR\x0csummaryKinds\x12/\n\x06\x66ilter\x18\x03 \x01(\x0b\x32\x12.operand.v1.FilterH\x00R\x06\x66ilter\x88\x01\x01\"e\n\x0bSummaryKind\x12\x1c\n\x18SUMMARY_KIND_UNSPECIFIED\x10\x00\x12\x1d\n\x19SUMMARY_KIND_TOPIC_STRING\x10\x01\x12\x19\n\x15SUMMARY_KIND_MARKDOWN\x10\x02\x42\t\n\x07_filter\"\\\n\x0f\x45xplorationData\x12\x41\n\x08\x63oncepts\x18\x01 \x01(\x0b\x32#.operand.v1.ConceptsExplorationDataH\x00R\x08\x63onceptsB\x06\n\x04kind\"\xb8\x04\n\x17\x43onceptsExplorationData\x12G\n\x08\x63oncepts\x18\x01 \x03(\x0b\x32+.operand.v1.ConceptsExplorationData.ConceptR\x08\x63oncepts\x1a:\n\x07Snippet\x12\x12\n\x04text\x18\x01 \x01(\tR\x04text\x12\x1b\n\tobject_id\x18\x02 \x01(\tR\x08objectId\x1aT\n\x07Summary\x12#\n\x0ctopic_string\x18\x01 \x01(\tH\x00R\x0btopicString\x12\x1c\n\x08markdown\x18\x02 \x01(\tH\x00R\x08markdownB\x06\n\x04kind\x1a\xc1\x02\n\x07\x43oncept\x12G\n\x08snippets\x18\x01 \x03(\x0b\x32+.operand.v1.ConceptsExplorationData.SnippetR\x08snippets\x12R\n\x07objects\x18\x02 \x03(\x0b\x32\x38.operand.v1.ConceptsExplorationData.Concept.ObjectsEntryR\x07objects\x12I\n\tsummaries\x18\x03 \x03(\x0b\x32+.operand.v1.ConceptsExplorationData.SummaryR\tsummaries\x1aN\n\x0cObjectsEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12(\n\x05value\x18\x02 \x01(\x0b\x32\x12.operand.v1.ObjectR\x05value:\x02\x38\x01\"\xda\x03\n\x0b\x45xploration\x12\x1b\n\tpublic_id\x18\x01 \x01(\tR\x08publicId\x12\x39\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.TimestampR\tcreatedAt\x12>\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.TimestampH\x00R\tupdatedAt\x88\x01\x01\x12/\n\x04kind\x18\x04 \x01(\x0e\x32\x1b.operand.v1.ExplorationKindR\x04kind\x12\x41\n\nparameters\x18\x05 \x01(\x0b\x32!.operand.v1.ExplorationParametersR\nparameters\x12\x35\n\x06status\x18\x06 \x01(\x0e\x32\x1d.operand.v1.ExplorationStatusR\x06status\x12\x34\n\x04\x64\x61ta\x18\x07 \x01(\x0b\x32\x1b.operand.v1.ExplorationDataH\x01R\x04\x64\x61ta\x88\x01\x01\x12(\n\rerror_message\x18\x08 \x01(\tH\x02R\x0c\x65rrorMessage\x88\x01\x01\x42\r\n\x0b_updated_atB\x07\n\x05_dataB\x10\n\x0e_error_message\"M\n\x12\x45xplorationOptions\x12&\n\x0cinclude_data\x18\x01 \x01(\x08H\x00R\x0bincludeData\x88\x01\x01\x42\x0f\n\r_include_data\"\xf4\x01\n\x18\x43reateExplorationRequest\x12\x19\n\x08index_id\x18\x01 \x01(\tR\x07indexId\x12/\n\x04kind\x18\x02 \x01(\x0e\x32\x1b.operand.v1.ExplorationKindR\x04kind\x12\x41\n\nparameters\x18\x03 \x01(\x0b\x32!.operand.v1.ExplorationParametersR\nparameters\x12=\n\x07options\x18\x04 \x01(\x0b\x32\x1e.operand.v1.ExplorationOptionsH\x00R\x07options\x88\x01\x01\x42\n\n\x08_options\"V\n\x19\x43reateExplorationResponse\x12\x39\n\x0b\x65xploration\x18\x01 \x01(\x0b\x32\x17.operand.v1.ExplorationR\x0b\x65xploration\"7\n\x18\x44\x65leteExplorationRequest\x12\x1b\n\tpublic_id\x18\x01 \x01(\tR\x08publicId\"\x1b\n\x19\x44\x65leteExplorationResponse\"\xbd\x01\n\x17ListExplorationsRequest\x12\x19\n\x08index_id\x18\x01 \x01(\tR\x07indexId\x12\x14\n\x05limit\x18\x02 \x01(\x05R\x05limit\x12\x1b\n\x06offset\x18\x03 \x01(\x05H\x00R\x06offset\x88\x01\x01\x12=\n\x07options\x18\x04 \x01(\x0b\x32\x1e.operand.v1.ExplorationOptionsH\x01R\x07options\x88\x01\x01\x42\t\n\x07_offsetB\n\n\x08_options\"W\n\x18ListExplorationsResponse\x12;\n\x0c\x65xplorations\x18\x01 \x03(\x0b\x32\x17.operand.v1.ExplorationR\x0c\x65xplorations\"\x7f\n\x15GetExplorationRequest\x12\x1b\n\tpublic_id\x18\x01 \x01(\tR\x08publicId\x12=\n\x07options\x18\x02 \x01(\x0b\x32\x1e.operand.v1.ExplorationOptionsH\x00R\x07options\x88\x01\x01\x42\n\n\x08_options\"S\n\x16GetExplorationResponse\x12\x39\n\x0b\x65xploration\x18\x01 \x01(\x0b\x32\x17.operand.v1.ExplorationR\x0b\x65xploration*R\n\x0f\x45xplorationKind\x12 \n\x1c\x45XPLORATION_KIND_UNSPECIFIED\x10\x00\x12\x1d\n\x19\x45XPLORATION_KIND_CONCEPTS\x10\x01*\xb8\x01\n\x11\x45xplorationStatus\x12\"\n\x1e\x45XPLORATION_STATUS_UNSPECIFIED\x10\x00\x12\x1e\n\x1a\x45XPLORATION_STATUS_PENDING\x10\x01\x12\x1e\n\x1a\x45XPLORATION_STATUS_RUNNING\x10\x02\x12 \n\x1c\x45XPLORATION_STATUS_COMPLETED\x10\x03\x12\x1d\n\x19\x45XPLORATION_STATUS_FAILED\x10\x04\x32\xe1\t\n\x0cIndexService\x12P\n\x0b\x43reateIndex\x12\x1e.operand.v1.CreateIndexRequest\x1a\x1f.operand.v1.CreateIndexResponse\"\x00\x12P\n\x0bListIndexes\x12\x1e.operand.v1.ListIndexesRequest\x1a\x1f.operand.v1.ListIndexesResponse\"\x00\x12G\n\x08GetIndex\x12\x1b.operand.v1.GetIndexRequest\x1a\x1c.operand.v1.GetIndexResponse\"\x00\x12P\n\x0bUpdateIndex\x12\x1e.operand.v1.UpdateIndexRequest\x1a\x1f.operand.v1.UpdateIndexResponse\"\x00\x12P\n\x0b\x44\x65leteIndex\x12\x1e.operand.v1.DeleteIndexRequest\x1a\x1f.operand.v1.DeleteIndexResponse\"\x00\x12V\n\rSubscriptions\x12 .operand.v1.SubscriptionsRequest\x1a!.operand.v1.SubscriptionsResponse\"\x00\x12J\n\tSubscribe\x12\x1c.operand.v1.SubscribeRequest\x1a\x1d.operand.v1.SubscribeResponse\"\x00\x12P\n\x0bUnsubscribe\x12\x1e.operand.v1.UnsubscribeRequest\x1a\x1f.operand.v1.UnsubscribeResponse\"\x00\x12V\n\rSubscribersOf\x12 .operand.v1.SubscribersOfRequest\x1a!.operand.v1.SubscribersOfResponse\"\x00\x12n\n\x15\x41vailableExplorations\x12(.operand.v1.AvailableExplorationsRequest\x1a).operand.v1.AvailableExplorationsResponse\"\x00\x12\x62\n\x11\x43reateExploration\x12$.operand.v1.CreateExplorationRequest\x1a%.operand.v1.CreateExplorationResponse\"\x00\x12\x62\n\x11\x44\x65leteExploration\x12$.operand.v1.DeleteExplorationRequest\x1a%.operand.v1.DeleteExplorationResponse\"\x00\x12_\n\x10ListExplorations\x12#.operand.v1.ListExplorationsRequest\x1a$.operand.v1.ListExplorationsResponse\"\x00\x12Y\n\x0eGetExploration\x12!.operand.v1.GetExplorationRequest\x1a\".operand.v1.GetExplorationResponse\"\x00\x42\x8a\x01\n\x0e\x63om.operand.v1B\nIndexProtoP\x01Z#operand.ai/gen/operand/v1;operandv1\xa2\x02\x03OXX\xaa\x02\nOperand.V1\xca\x02\nOperand\\V1\xe2\x02\x16Operand\\V1\\GPBMetadata\xea\x02\x0bOperand::V1b\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'operand.v1.index_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016com.operand.v1B\nIndexProtoP\001Z#operand.ai/gen/operand/v1;operandv1\242\002\003OXX\252\002\nOperand.V1\312\002\nOperand\\V1\342\002\026Operand\\V1\\GPBMetadata\352\002\013Operand::V1'
  _CONCEPTSEXPLORATIONDATA_CONCEPT_OBJECTSENTRY._options = None
  _CONCEPTSEXPLORATIONDATA_CONCEPT_OBJECTSENTRY._serialized_options = b'8\001'
  _EXPLORATIONKIND._serialized_start=5636
  _EXPLORATIONKIND._serialized_end=5718
  _EXPLORATIONSTATUS._serialized_start=5721
  _EXPLORATIONSTATUS._serialized_end=5905
  _INDEXOPTIONS._serialized_start=97
  _INDEXOPTIONS._serialized_end=312
  _CREATEINDEXREQUEST._serialized_start=315
  _CREATEINDEXREQUEST._serialized_end=530
  _SUBSCRIPTION._serialized_start=532
  _SUBSCRIPTION._serialized_end=643
  _INDEXSTATS._serialized_start=645
  _INDEXSTATS._serialized_end=691
  _USERPROFILE._serialized_start=694
  _USERPROFILE._serialized_end=988
  _INDEX._serialized_start=991
  _INDEX._serialized_end=1419
  _CREATEINDEXRESPONSE._serialized_start=1421
  _CREATEINDEXRESPONSE._serialized_end=1483
  _LISTINDEXESREQUEST._serialized_start=1486
  _LISTINDEXESREQUEST._serialized_end=1634
  _LISTINDEXESRESPONSE._serialized_start=1636
  _LISTINDEXESRESPONSE._serialized_end=1702
  _GETINDEXREQUEST._serialized_start=1704
  _GETINDEXREQUEST._serialized_end=1819
  _GETINDEXRESPONSE._serialized_start=1821
  _GETINDEXRESPONSE._serialized_end=1880
  _UPDATEINDEXREQUEST._serialized_start=1883
  _UPDATEINDEXREQUEST._serialized_end=2178
  _UPDATEINDEXRESPONSE._serialized_start=2180
  _UPDATEINDEXRESPONSE._serialized_end=2242
  _DELETEINDEXREQUEST._serialized_start=2244
  _DELETEINDEXREQUEST._serialized_end=2293
  _DELETEINDEXRESPONSE._serialized_start=2295
  _DELETEINDEXRESPONSE._serialized_end=2316
  _SUBSCRIPTIONSREQUEST._serialized_start=2319
  _SUBSCRIPTIONSREQUEST._serialized_end=2452
  _SUBSCRIPTIONSRESPONSE._serialized_start=2454
  _SUBSCRIPTIONSRESPONSE._serialized_end=2522
  _SUBSCRIBEREQUEST._serialized_start=2524
  _SUBSCRIBEREQUEST._serialized_end=2632
  _SUBSCRIBERESPONSE._serialized_start=2634
  _SUBSCRIBERESPONSE._serialized_end=2715
  _UNSUBSCRIBEREQUEST._serialized_start=2717
  _UNSUBSCRIBEREQUEST._serialized_end=2766
  _UNSUBSCRIBERESPONSE._serialized_start=2768
  _UNSUBSCRIBERESPONSE._serialized_end=2789
  _SUBSCRIBERSOFREQUEST._serialized_start=2791
  _SUBSCRIBERSOFREQUEST._serialized_end=2842
  _SUBSCRIBERSOFRESPONSE._serialized_start=2844
  _SUBSCRIBERSOFRESPONSE._serialized_end=2926
  _AVAILABLEEXPLORATIONSREQUEST._serialized_start=2928
  _AVAILABLEEXPLORATIONSREQUEST._serialized_end=2985
  _AVAILABLEEXPLORATIONSRESPONSE._serialized_start=2987
  _AVAILABLEEXPLORATIONSRESPONSE._serialized_end=3069
  _EXPLORATIONPARAMETERS._serialized_start=3071
  _EXPLORATIONPARAMETERS._serialized_end=3175
  _CONCEPTSEXPLORATIONPARAMETERS._serialized_start=3178
  _CONCEPTSEXPLORATIONPARAMETERS._serialized_end=3497
  _CONCEPTSEXPLORATIONPARAMETERS_SUMMARYKIND._serialized_start=3385
  _CONCEPTSEXPLORATIONPARAMETERS_SUMMARYKIND._serialized_end=3486
  _EXPLORATIONDATA._serialized_start=3499
  _EXPLORATIONDATA._serialized_end=3591
  _CONCEPTSEXPLORATIONDATA._serialized_start=3594
  _CONCEPTSEXPLORATIONDATA._serialized_end=4162
  _CONCEPTSEXPLORATIONDATA_SNIPPET._serialized_start=3694
  _CONCEPTSEXPLORATIONDATA_SNIPPET._serialized_end=3752
  _CONCEPTSEXPLORATIONDATA_SUMMARY._serialized_start=3754
  _CONCEPTSEXPLORATIONDATA_SUMMARY._serialized_end=3838
  _CONCEPTSEXPLORATIONDATA_CONCEPT._serialized_start=3841
  _CONCEPTSEXPLORATIONDATA_CONCEPT._serialized_end=4162
  _CONCEPTSEXPLORATIONDATA_CONCEPT_OBJECTSENTRY._serialized_start=4084
  _CONCEPTSEXPLORATIONDATA_CONCEPT_OBJECTSENTRY._serialized_end=4162
  _EXPLORATION._serialized_start=4165
  _EXPLORATION._serialized_end=4639
  _EXPLORATIONOPTIONS._serialized_start=4641
  _EXPLORATIONOPTIONS._serialized_end=4718
  _CREATEEXPLORATIONREQUEST._serialized_start=4721
  _CREATEEXPLORATIONREQUEST._serialized_end=4965
  _CREATEEXPLORATIONRESPONSE._serialized_start=4967
  _CREATEEXPLORATIONRESPONSE._serialized_end=5053
  _DELETEEXPLORATIONREQUEST._serialized_start=5055
  _DELETEEXPLORATIONREQUEST._serialized_end=5110
  _DELETEEXPLORATIONRESPONSE._serialized_start=5112
  _DELETEEXPLORATIONRESPONSE._serialized_end=5139
  _LISTEXPLORATIONSREQUEST._serialized_start=5142
  _LISTEXPLORATIONSREQUEST._serialized_end=5331
  _LISTEXPLORATIONSRESPONSE._serialized_start=5333
  _LISTEXPLORATIONSRESPONSE._serialized_end=5420
  _GETEXPLORATIONREQUEST._serialized_start=5422
  _GETEXPLORATIONREQUEST._serialized_end=5549
  _GETEXPLORATIONRESPONSE._serialized_start=5551
  _GETEXPLORATIONRESPONSE._serialized_end=5634
  _INDEXSERVICE._serialized_start=5908
  _INDEXSERVICE._serialized_end=7157
# @@protoc_insertion_point(module_scope)
