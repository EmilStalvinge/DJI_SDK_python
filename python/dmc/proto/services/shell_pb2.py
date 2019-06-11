# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/services/shell.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dmc.proto import messages_pb2 as proto_dot_messages__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/services/shell.proto',
  package='shell',
  syntax='proto3',
  serialized_options=_b('Z7github.com/tobiasfriden/dmc-server/services/shell/proto'),
  serialized_pb=_b('\n\x1aproto/services/shell.proto\x12\x05shell\x1a\x14proto/messages.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x19google/protobuf/any.proto\" \n\rStreamRequest\x12\x0f\n\x07\x64roneId\x18\x01 \x01(\t\"%\n\x04Line\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\x0f\n\x07\x64roneId\x18\x02 \x01(\t2\xb5\x01\n\x05Shell\x12\x37\n\x0bPilotStream\x12\x14.shell.StreamRequest\x1a\x0e.proto.Message\"\x00\x30\x01\x12\x32\n\tPilotLine\x12\x0b.shell.Line\x1a\x16.google.protobuf.Empty\"\x00\x12?\n\x0b\x44roneStream\x12\x14.google.protobuf.Any\x1a\x14.google.protobuf.Any\"\x00(\x01\x30\x01\x42\x39Z7github.com/tobiasfriden/dmc-server/services/shell/protob\x06proto3')
  ,
  dependencies=[proto_dot_messages__pb2.DESCRIPTOR,google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_STREAMREQUEST = _descriptor.Descriptor(
  name='StreamRequest',
  full_name='shell.StreamRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='droneId', full_name='shell.StreamRequest.droneId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_end=147,
)


_LINE = _descriptor.Descriptor(
  name='Line',
  full_name='shell.Line',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='shell.Line.data', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='droneId', full_name='shell.Line.droneId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=149,
  serialized_end=186,
)

DESCRIPTOR.message_types_by_name['StreamRequest'] = _STREAMREQUEST
DESCRIPTOR.message_types_by_name['Line'] = _LINE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StreamRequest = _reflection.GeneratedProtocolMessageType('StreamRequest', (_message.Message,), dict(
  DESCRIPTOR = _STREAMREQUEST,
  __module__ = 'proto.services.shell_pb2'
  # @@protoc_insertion_point(class_scope:shell.StreamRequest)
  ))
_sym_db.RegisterMessage(StreamRequest)

Line = _reflection.GeneratedProtocolMessageType('Line', (_message.Message,), dict(
  DESCRIPTOR = _LINE,
  __module__ = 'proto.services.shell_pb2'
  # @@protoc_insertion_point(class_scope:shell.Line)
  ))
_sym_db.RegisterMessage(Line)


DESCRIPTOR._options = None

_SHELL = _descriptor.ServiceDescriptor(
  name='Shell',
  full_name='shell.Shell',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=189,
  serialized_end=370,
  methods=[
  _descriptor.MethodDescriptor(
    name='PilotStream',
    full_name='shell.Shell.PilotStream',
    index=0,
    containing_service=None,
    input_type=_STREAMREQUEST,
    output_type=proto_dot_messages__pb2._MESSAGE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='PilotLine',
    full_name='shell.Shell.PilotLine',
    index=1,
    containing_service=None,
    input_type=_LINE,
    output_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DroneStream',
    full_name='shell.Shell.DroneStream',
    index=2,
    containing_service=None,
    input_type=google_dot_protobuf_dot_any__pb2._ANY,
    output_type=google_dot_protobuf_dot_any__pb2._ANY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SHELL)

DESCRIPTOR.services_by_name['Shell'] = _SHELL

# @@protoc_insertion_point(module_scope)
