# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/datacatalog_v1beta1/proto/search.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.cloud.datacatalog_v1beta1.proto import (
    common_pb2 as google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_common__pb2,
)
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="google/cloud/datacatalog_v1beta1/proto/search.proto",
    package="google.cloud.datacatalog.v1beta1",
    syntax="proto3",
    serialized_options=b"\n$com.google.cloud.datacatalog.v1beta1P\001ZKgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1beta1;datacatalog\370\001\001\252\002 Google.Cloud.DataCatalog.V1Beta1\312\002 Google\\Cloud\\DataCatalog\\V1beta1\352\002#Google::Cloud::DataCatalog::V1beta1",
    serialized_pb=b'\n3google/cloud/datacatalog_v1beta1/proto/search.proto\x12 google.cloud.datacatalog.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x33google/cloud/datacatalog_v1beta1/proto/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbd\x01\n\x13SearchCatalogResult\x12N\n\x12search_result_type\x18\x01 \x01(\x0e\x32\x32.google.cloud.datacatalog.v1beta1.SearchResultType\x12\x1d\n\x15search_result_subtype\x18\x02 \x01(\t\x12\x1e\n\x16relative_resource_name\x18\x03 \x01(\t\x12\x17\n\x0flinked_resource\x18\x04 \x01(\t*d\n\x10SearchResultType\x12"\n\x1eSEARCH_RESULT_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05\x45NTRY\x10\x01\x12\x10\n\x0cTAG_TEMPLATE\x10\x02\x12\x0f\n\x0b\x45NTRY_GROUP\x10\x03\x42\xe4\x01\n$com.google.cloud.datacatalog.v1beta1P\x01ZKgoogle.golang.org/genproto/googleapis/cloud/datacatalog/v1beta1;datacatalog\xf8\x01\x01\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1b\x06proto3',
    dependencies=[
        google_dot_api_dot_field__behavior__pb2.DESCRIPTOR,
        google_dot_cloud_dot_datacatalog__v1beta1_dot_proto_dot_common__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,
    ],
)

_SEARCHRESULTTYPE = _descriptor.EnumDescriptor(
    name="SearchResultType",
    full_name="google.cloud.datacatalog.v1beta1.SearchResultType",
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name="SEARCH_RESULT_TYPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name="ENTRY", index=1, number=1, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="TAG_TEMPLATE", index=2, number=2, serialized_options=None, type=None
        ),
        _descriptor.EnumValueDescriptor(
            name="ENTRY_GROUP", index=3, number=3, serialized_options=None, type=None
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=400,
    serialized_end=500,
)
_sym_db.RegisterEnumDescriptor(_SEARCHRESULTTYPE)

SearchResultType = enum_type_wrapper.EnumTypeWrapper(_SEARCHRESULTTYPE)
SEARCH_RESULT_TYPE_UNSPECIFIED = 0
ENTRY = 1
TAG_TEMPLATE = 2
ENTRY_GROUP = 3


_SEARCHCATALOGRESULT = _descriptor.Descriptor(
    name="SearchCatalogResult",
    full_name="google.cloud.datacatalog.v1beta1.SearchCatalogResult",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="search_result_type",
            full_name="google.cloud.datacatalog.v1beta1.SearchCatalogResult.search_result_type",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="search_result_subtype",
            full_name="google.cloud.datacatalog.v1beta1.SearchCatalogResult.search_result_subtype",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="relative_resource_name",
            full_name="google.cloud.datacatalog.v1beta1.SearchCatalogResult.relative_resource_name",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="linked_resource",
            full_name="google.cloud.datacatalog.v1beta1.SearchCatalogResult.linked_resource",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=209,
    serialized_end=398,
)

_SEARCHCATALOGRESULT.fields_by_name["search_result_type"].enum_type = _SEARCHRESULTTYPE
DESCRIPTOR.message_types_by_name["SearchCatalogResult"] = _SEARCHCATALOGRESULT
DESCRIPTOR.enum_types_by_name["SearchResultType"] = _SEARCHRESULTTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SearchCatalogResult = _reflection.GeneratedProtocolMessageType(
    "SearchCatalogResult",
    (_message.Message,),
    {
        "DESCRIPTOR": _SEARCHCATALOGRESULT,
        "__module__": "google.cloud.datacatalog_v1beta1.proto.search_pb2",
        "__doc__": """A result that appears in the response of a search request. Each result
  captures details of one entry that matches the search.
  Attributes:
      search_result_type:
          Type of the search result. This field can be used to determine
          which Get method to call to fetch the full resource.
      search_result_subtype:
          Sub-type of the search result. This is a dot-delimited
          description of the resource’s full type, and is the same as
          the value callers would provide in the “type” search facet.
          Examples: ``entry.table``, ``entry.dataStream``,
          ``tagTemplate``.
      relative_resource_name:
          The relative resource name of the resource in URL format.
          Examples:  -  ``projects/{project_id}/locations/{location_id}/
          entryGroups/{entry_group_id}/entries/{entry_id}`` -
          ``projects/{project_id}/tagTemplates/{tag_template_id}``
      linked_resource:
          The full name of the cloud resource the entry belongs to. See:
          https://cloud.google.com/apis/design/resource_names#full_resou
          rce_name. Example:  -  ``//bigquery.googleapis.com/projects/pr
          ojectId/datasets/datasetId/tables/tableId``
  """,
        # @@protoc_insertion_point(class_scope:google.cloud.datacatalog.v1beta1.SearchCatalogResult)
    },
)
_sym_db.RegisterMessage(SearchCatalogResult)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
