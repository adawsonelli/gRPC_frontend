# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosine.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63osine.proto\x12\x06\x63osine\"<\n\nCosRequest\x12\x11\n\tamplitude\x18\x01 \x01(\x01\x12\x0c\n\x04\x66req\x18\x02 \x01(\x01\x12\r\n\x05phase\x18\x03 \x01(\x01\"\x18\n\x08\x43osReply\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x01\x32:\n\x06\x43osine\x12\x30\n\x06GetCos\x12\x12.cosine.CosRequest\x1a\x10.cosine.CosReply\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosine_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COSREQUEST._serialized_start=24
  _COSREQUEST._serialized_end=84
  _COSREPLY._serialized_start=86
  _COSREPLY._serialized_end=110
  _COSINE._serialized_start=112
  _COSINE._serialized_end=170
# @@protoc_insertion_point(module_scope)