# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sdv/databroker/v1/broker.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sdv.databroker.v1 import types_pb2 as sdv_dot_databroker_dot_v1_dot_types__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esdv/databroker/v1/broker.proto\x12\x11sdv.databroker.v1\x1a\x1dsdv/databroker/v1/types.proto\"*\n\x14GetDatapointsRequest\x12\x12\n\ndatapoints\x18\x01 \x03(\t\"\xb0\x01\n\x12GetDatapointsReply\x12I\n\ndatapoints\x18\x01 \x03(\x0b\x32\x35.sdv.databroker.v1.GetDatapointsReply.DatapointsEntry\x1aO\n\x0f\x44\x61tapointsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.sdv.databroker.v1.Datapoint:\x02\x38\x01\"!\n\x10SubscribeRequest\x12\r\n\x05query\x18\x02 \x01(\t\"\x9c\x01\n\x0eSubscribeReply\x12=\n\x06\x66ields\x18\x01 \x03(\x0b\x32-.sdv.databroker.v1.SubscribeReply.FieldsEntry\x1aK\n\x0b\x46ieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.sdv.databroker.v1.Datapoint:\x02\x38\x01\"#\n\x12GetMetadataRequest\x12\r\n\x05names\x18\x01 \x03(\t\"=\n\x10GetMetadataReply\x12)\n\x04list\x18\x01 \x03(\x0b\x32\x1b.sdv.databroker.v1.Metadata2\x9b\x02\n\x06\x42roker\x12_\n\rGetDatapoints\x12\'.sdv.databroker.v1.GetDatapointsRequest\x1a%.sdv.databroker.v1.GetDatapointsReply\x12U\n\tSubscribe\x12#.sdv.databroker.v1.SubscribeRequest\x1a!.sdv.databroker.v1.SubscribeReply0\x01\x12Y\n\x0bGetMetadata\x12%.sdv.databroker.v1.GetMetadataRequest\x1a#.sdv.databroker.v1.GetMetadataReplyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sdv.databroker.v1.broker_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETDATAPOINTSREPLY_DATAPOINTSENTRY._options = None
  _GETDATAPOINTSREPLY_DATAPOINTSENTRY._serialized_options = b'8\001'
  _SUBSCRIBEREPLY_FIELDSENTRY._options = None
  _SUBSCRIBEREPLY_FIELDSENTRY._serialized_options = b'8\001'
  _GETDATAPOINTSREQUEST._serialized_start=84
  _GETDATAPOINTSREQUEST._serialized_end=126
  _GETDATAPOINTSREPLY._serialized_start=129
  _GETDATAPOINTSREPLY._serialized_end=305
  _GETDATAPOINTSREPLY_DATAPOINTSENTRY._serialized_start=226
  _GETDATAPOINTSREPLY_DATAPOINTSENTRY._serialized_end=305
  _SUBSCRIBEREQUEST._serialized_start=307
  _SUBSCRIBEREQUEST._serialized_end=340
  _SUBSCRIBEREPLY._serialized_start=343
  _SUBSCRIBEREPLY._serialized_end=499
  _SUBSCRIBEREPLY_FIELDSENTRY._serialized_start=424
  _SUBSCRIBEREPLY_FIELDSENTRY._serialized_end=499
  _GETMETADATAREQUEST._serialized_start=501
  _GETMETADATAREQUEST._serialized_end=536
  _GETMETADATAREPLY._serialized_start=538
  _GETMETADATAREPLY._serialized_end=599
  _BROKER._serialized_start=602
  _BROKER._serialized_end=885
# @@protoc_insertion_point(module_scope)
