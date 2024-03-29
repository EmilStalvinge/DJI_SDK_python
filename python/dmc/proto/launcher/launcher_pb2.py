# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/launcher/launcher.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dmc.proto.telemetry import telemetry_pb2 as proto_dot_telemetry_dot_telemetry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/launcher/launcher.proto',
  package='launcher',
  syntax='proto3',
  serialized_options=_b('Z1github.com/tobiasfriden/dmc-server/proto/launcher'),
  serialized_pb=_b('\n\x1dproto/launcher/launcher.proto\x12\x08launcher\x1a\x1fproto/telemetry/telemetry.proto\"\x89\x01\n\x07\x43ommand\x12$\n\x04type\x18\x01 \x01(\x0e\x32\x16.launcher.Command.Type\x12\x0c\n\x04meta\x18\x02 \x01(\x0c\"J\n\x04Type\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07STANDBY\x10\x01\x12\t\n\x05READY\x10\x02\x12\n\n\x06LAUNCH\x10\x03\x12\n\n\x06\x43USTOM\x10\x04\x12\x08\n\x04\x46\x41IL\x10\x05\"\xc7\x01\n\x07Payload\x12$\n\x04mode\x18\x01 \x01(\x0e\x32\x16.launcher.Payload.Mode\x12%\n\x08position\x18\x02 \x01(\x0b\x32\x13.telemetry.Position\x12#\n\x07heading\x18\x03 \x01(\x0b\x32\x12.telemetry.Heading\"J\n\x04Mode\x12\x0b\n\x07OFFLINE\x10\x00\x12\x0c\n\x08INACTIVE\x10\x01\x12\x0b\n\x07STANDBY\x10\x02\x12\x0c\n\x08PREPARED\x10\x03\x12\x0c\n\x08LAUNCHED\x10\x04\x42\x33Z1github.com/tobiasfriden/dmc-server/proto/launcherb\x06proto3')
  ,
  dependencies=[proto_dot_telemetry_dot_telemetry__pb2.DESCRIPTOR,])



_COMMAND_TYPE = _descriptor.EnumDescriptor(
  name='Type',
  full_name='launcher.Command.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STANDBY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='READY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAUNCH', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUSTOM', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAIL', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=140,
  serialized_end=214,
)
_sym_db.RegisterEnumDescriptor(_COMMAND_TYPE)

_PAYLOAD_MODE = _descriptor.EnumDescriptor(
  name='Mode',
  full_name='launcher.Payload.Mode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OFFLINE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INACTIVE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STANDBY', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREPARED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LAUNCHED', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=342,
  serialized_end=416,
)
_sym_db.RegisterEnumDescriptor(_PAYLOAD_MODE)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='launcher.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='launcher.Command.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meta', full_name='launcher.Command.meta', index=1,
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
    _COMMAND_TYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=214,
)


_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='launcher.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='launcher.Payload.mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='launcher.Payload.position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='heading', full_name='launcher.Payload.heading', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PAYLOAD_MODE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=217,
  serialized_end=416,
)

_COMMAND.fields_by_name['type'].enum_type = _COMMAND_TYPE
_COMMAND_TYPE.containing_type = _COMMAND
_PAYLOAD.fields_by_name['mode'].enum_type = _PAYLOAD_MODE
_PAYLOAD.fields_by_name['position'].message_type = proto_dot_telemetry_dot_telemetry__pb2._POSITION
_PAYLOAD.fields_by_name['heading'].message_type = proto_dot_telemetry_dot_telemetry__pb2._HEADING
_PAYLOAD_MODE.containing_type = _PAYLOAD
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.message_types_by_name['Payload'] = _PAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), dict(
  DESCRIPTOR = _COMMAND,
  __module__ = 'proto.launcher.launcher_pb2'
  # @@protoc_insertion_point(class_scope:launcher.Command)
  ))
_sym_db.RegisterMessage(Command)

Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), dict(
  DESCRIPTOR = _PAYLOAD,
  __module__ = 'proto.launcher.launcher_pb2'
  # @@protoc_insertion_point(class_scope:launcher.Payload)
  ))
_sym_db.RegisterMessage(Payload)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
