# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/services/layers.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/services/layers.proto',
  package='layers',
  syntax='proto3',
  serialized_options=_b('Z8github.com/tobiasfriden/dmc-server/services/layers/proto'),
  serialized_pb=_b('\n\x1bproto/services/layers.proto\x12\x06layers\"*\n\nGetRequest\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0f\n\x07refresh\x18\x02 \x01(\x05\"\x1e\n\x0bGetResponse\x12\x0f\n\x07\x65ncoded\x18\x01 \x01(\x0c\"1\n\x12GetInternalRequest\x12\r\n\x05orgId\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x03(\t\"}\n\x13GetInternalResponse\x12\x37\n\x06result\x18\x01 \x03(\x0b\x32\'.layers.GetInternalResponse.ResultEntry\x1a-\n\x0bResultEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x32\x89\x01\n\x06Layers\x12\x35\n\x08GetLayer\x12\x12.layers.GetRequest\x1a\x13.layers.GetResponse\"\x00\x12H\n\x0bGetInternal\x12\x1a.layers.GetInternalRequest\x1a\x1b.layers.GetInternalResponse\"\x00\x42:Z8github.com/tobiasfriden/dmc-server/services/layers/protob\x06proto3')
)




_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='layers.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uri', full_name='layers.GetRequest.uri', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='refresh', full_name='layers.GetRequest.refresh', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=81,
)


_GETRESPONSE = _descriptor.Descriptor(
  name='GetResponse',
  full_name='layers.GetResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='encoded', full_name='layers.GetResponse.encoded', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=113,
)


_GETINTERNALREQUEST = _descriptor.Descriptor(
  name='GetInternalRequest',
  full_name='layers.GetInternalRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='orgId', full_name='layers.GetInternalRequest.orgId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='layers.GetInternalRequest.name', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=115,
  serialized_end=164,
)


_GETINTERNALRESPONSE_RESULTENTRY = _descriptor.Descriptor(
  name='ResultEntry',
  full_name='layers.GetInternalResponse.ResultEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='layers.GetInternalResponse.ResultEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='layers.GetInternalResponse.ResultEntry.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=246,
  serialized_end=291,
)

_GETINTERNALRESPONSE = _descriptor.Descriptor(
  name='GetInternalResponse',
  full_name='layers.GetInternalResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='layers.GetInternalResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_GETINTERNALRESPONSE_RESULTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=166,
  serialized_end=291,
)

_GETINTERNALRESPONSE_RESULTENTRY.containing_type = _GETINTERNALRESPONSE
_GETINTERNALRESPONSE.fields_by_name['result'].message_type = _GETINTERNALRESPONSE_RESULTENTRY
DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['GetResponse'] = _GETRESPONSE
DESCRIPTOR.message_types_by_name['GetInternalRequest'] = _GETINTERNALREQUEST
DESCRIPTOR.message_types_by_name['GetInternalResponse'] = _GETINTERNALRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREQUEST,
  __module__ = 'proto.services.layers_pb2'
  # @@protoc_insertion_point(class_scope:layers.GetRequest)
  ))
_sym_db.RegisterMessage(GetRequest)

GetResponse = _reflection.GeneratedProtocolMessageType('GetResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETRESPONSE,
  __module__ = 'proto.services.layers_pb2'
  # @@protoc_insertion_point(class_scope:layers.GetResponse)
  ))
_sym_db.RegisterMessage(GetResponse)

GetInternalRequest = _reflection.GeneratedProtocolMessageType('GetInternalRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETINTERNALREQUEST,
  __module__ = 'proto.services.layers_pb2'
  # @@protoc_insertion_point(class_scope:layers.GetInternalRequest)
  ))
_sym_db.RegisterMessage(GetInternalRequest)

GetInternalResponse = _reflection.GeneratedProtocolMessageType('GetInternalResponse', (_message.Message,), dict(

  ResultEntry = _reflection.GeneratedProtocolMessageType('ResultEntry', (_message.Message,), dict(
    DESCRIPTOR = _GETINTERNALRESPONSE_RESULTENTRY,
    __module__ = 'proto.services.layers_pb2'
    # @@protoc_insertion_point(class_scope:layers.GetInternalResponse.ResultEntry)
    ))
  ,
  DESCRIPTOR = _GETINTERNALRESPONSE,
  __module__ = 'proto.services.layers_pb2'
  # @@protoc_insertion_point(class_scope:layers.GetInternalResponse)
  ))
_sym_db.RegisterMessage(GetInternalResponse)
_sym_db.RegisterMessage(GetInternalResponse.ResultEntry)


DESCRIPTOR._options = None
_GETINTERNALRESPONSE_RESULTENTRY._options = None

_LAYERS = _descriptor.ServiceDescriptor(
  name='Layers',
  full_name='layers.Layers',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=294,
  serialized_end=431,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetLayer',
    full_name='layers.Layers.GetLayer',
    index=0,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_GETRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetInternal',
    full_name='layers.Layers.GetInternal',
    index=1,
    containing_service=None,
    input_type=_GETINTERNALREQUEST,
    output_type=_GETINTERNALRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_LAYERS)

DESCRIPTOR.services_by_name['Layers'] = _LAYERS

# @@protoc_insertion_point(module_scope)
