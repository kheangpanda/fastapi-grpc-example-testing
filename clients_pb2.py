# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: clients.proto
# Protobuf Python Version: 5.27.2
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
    2,
    '',
    'clients.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rclients.proto\x12\x07\x63lients\"A\n\nAddRequest\x12\x11\n\tfirstName\x18\x01 \x01(\t\x12\x10\n\x08lastName\x18\x02 \x01(\t\x12\x0e\n\x06gender\x18\x03 \x01(\t\"\x1f\n\x0b\x41\x64\x64Response\x12\x10\n\x08\x66ullname\x18\x01 \x01(\t2;\n\x07\x43lients\x12\x30\n\x03\x41\x64\x64\x12\x13.clients.AddRequest\x1a\x14.clients.AddResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'clients_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ADDREQUEST']._serialized_start=26
  _globals['_ADDREQUEST']._serialized_end=91
  _globals['_ADDRESPONSE']._serialized_start=93
  _globals['_ADDRESPONSE']._serialized_end=124
  _globals['_CLIENTS']._serialized_start=126
  _globals['_CLIENTS']._serialized_end=185
# @@protoc_insertion_point(module_scope)
