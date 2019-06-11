# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/services/drone.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from dmc.proto.models import models_pb2 as proto_dot_models_dot_models__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/services/drone.proto',
  package='drone',
  syntax='proto3',
  serialized_options=_b('Z7github.com/tobiasfriden/dmc-server/services/drone/proto'),
  serialized_pb=_b('\n\x1aproto/services/drone.proto\x12\x05\x64rone\x1a\x1bgoogle/protobuf/empty.proto\x1a\x19proto/models/models.proto\"<\n\x0b\x41uthRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0f\n\x07\x64roneId\x18\x02 \x01(\t\x12\r\n\x05orgId\x18\x03 \x01(\t\"\x1f\n\x0c\x41uthResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"/\n\x0cGetIDRequest\x12\x0f\n\x07\x64roneId\x18\x01 \x01(\t\x12\x0e\n\x06\x66ields\x18\x02 \x03(\t\".\n\rGetIDResponse\x12\x1d\n\x06result\x18\x01 \x01(\x0b\x32\r.models.Drone\"1\n\x0fRegisterRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"#\n\x10RegisterResponse\x12\x0f\n\x07\x64roneId\x18\x01 \x01(\t\"/\n\x0eSetImsiRequest\x12\x0f\n\x07\x64roneId\x18\x01 \x01(\t\x12\x0c\n\x04imsi\x18\x02 \x01(\t\"\"\n\x0fSetImsiResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"3\n\x12\x46indDronesResponse\x12\x1d\n\x06\x64rones\x18\x01 \x03(\x0b\x32\r.models.Drone\"6\n\x12UpdateDroneRequest\x12 \n\tdroneData\x18\x01 \x01(\x0b\x32\r.models.Drone\"&\n\x13UpdateDroneResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x1f\n\x0fGetKeysResponse\x12\x0c\n\x04keys\x18\x01 \x01(\t\" \n\rDeleteRequest\x12\x0f\n\x07\x64roneId\x18\x01 \x01(\t\"!\n\x0e\x44\x65leteResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x32\xe6\x02\n\x05\x44rone\x12\x36\n\tAuthorize\x12\x12.drone.AuthRequest\x1a\x13.drone.AuthResponse\"\x00\x12\x34\n\x05GetID\x12\x13.drone.GetIDRequest\x1a\x14.drone.GetIDResponse\"\x00\x12=\n\x08Register\x12\x16.drone.RegisterRequest\x1a\x17.drone.RegisterResponse\"\x00\x12:\n\x07SetIMSI\x12\x15.drone.SetImsiRequest\x1a\x16.drone.SetImsiResponse\"\x00\x12;\n\x04\x46ind\x12\x16.google.protobuf.Empty\x1a\x19.drone.FindDronesResponse\"\x00\x12\x37\n\x06\x44\x65lete\x12\x14.drone.DeleteRequest\x1a\x15.drone.DeleteResponse\"\x00\x42\x39Z7github.com/tobiasfriden/dmc-server/services/drone/protob\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,proto_dot_models_dot_models__pb2.DESCRIPTOR,])




_AUTHREQUEST = _descriptor.Descriptor(
  name='AuthRequest',
  full_name='drone.AuthRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token', full_name='drone.AuthRequest.token', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='droneId', full_name='drone.AuthRequest.droneId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orgId', full_name='drone.AuthRequest.orgId', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=93,
  serialized_end=153,
)


_AUTHRESPONSE = _descriptor.Descriptor(
  name='AuthResponse',
  full_name='drone.AuthResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='drone.AuthResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=155,
  serialized_end=186,
)


_GETIDREQUEST = _descriptor.Descriptor(
  name='GetIDRequest',
  full_name='drone.GetIDRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='droneId', full_name='drone.GetIDRequest.droneId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='drone.GetIDRequest.fields', index=1,
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
  serialized_start=188,
  serialized_end=235,
)


_GETIDRESPONSE = _descriptor.Descriptor(
  name='GetIDResponse',
  full_name='drone.GetIDResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='drone.GetIDResponse.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=237,
  serialized_end=283,
)


_REGISTERREQUEST = _descriptor.Descriptor(
  name='RegisterRequest',
  full_name='drone.RegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='drone.RegisterRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='password', full_name='drone.RegisterRequest.password', index=1,
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
  serialized_start=285,
  serialized_end=334,
)


_REGISTERRESPONSE = _descriptor.Descriptor(
  name='RegisterResponse',
  full_name='drone.RegisterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='droneId', full_name='drone.RegisterResponse.droneId', index=0,
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
  serialized_start=336,
  serialized_end=371,
)


_SETIMSIREQUEST = _descriptor.Descriptor(
  name='SetImsiRequest',
  full_name='drone.SetImsiRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='droneId', full_name='drone.SetImsiRequest.droneId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imsi', full_name='drone.SetImsiRequest.imsi', index=1,
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
  serialized_start=373,
  serialized_end=420,
)


_SETIMSIRESPONSE = _descriptor.Descriptor(
  name='SetImsiResponse',
  full_name='drone.SetImsiResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='drone.SetImsiResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=422,
  serialized_end=456,
)


_FINDDRONESRESPONSE = _descriptor.Descriptor(
  name='FindDronesResponse',
  full_name='drone.FindDronesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='drones', full_name='drone.FindDronesResponse.drones', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=458,
  serialized_end=509,
)


_UPDATEDRONEREQUEST = _descriptor.Descriptor(
  name='UpdateDroneRequest',
  full_name='drone.UpdateDroneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='droneData', full_name='drone.UpdateDroneRequest.droneData', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=511,
  serialized_end=565,
)


_UPDATEDRONERESPONSE = _descriptor.Descriptor(
  name='UpdateDroneResponse',
  full_name='drone.UpdateDroneResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='drone.UpdateDroneResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=567,
  serialized_end=605,
)


_GETKEYSRESPONSE = _descriptor.Descriptor(
  name='GetKeysResponse',
  full_name='drone.GetKeysResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='drone.GetKeysResponse.keys', index=0,
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
  serialized_start=607,
  serialized_end=638,
)


_DELETEREQUEST = _descriptor.Descriptor(
  name='DeleteRequest',
  full_name='drone.DeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='droneId', full_name='drone.DeleteRequest.droneId', index=0,
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
  serialized_start=640,
  serialized_end=672,
)


_DELETERESPONSE = _descriptor.Descriptor(
  name='DeleteResponse',
  full_name='drone.DeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='success', full_name='drone.DeleteResponse.success', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=674,
  serialized_end=707,
)

_GETIDRESPONSE.fields_by_name['result'].message_type = proto_dot_models_dot_models__pb2._DRONE
_FINDDRONESRESPONSE.fields_by_name['drones'].message_type = proto_dot_models_dot_models__pb2._DRONE
_UPDATEDRONEREQUEST.fields_by_name['droneData'].message_type = proto_dot_models_dot_models__pb2._DRONE
DESCRIPTOR.message_types_by_name['AuthRequest'] = _AUTHREQUEST
DESCRIPTOR.message_types_by_name['AuthResponse'] = _AUTHRESPONSE
DESCRIPTOR.message_types_by_name['GetIDRequest'] = _GETIDREQUEST
DESCRIPTOR.message_types_by_name['GetIDResponse'] = _GETIDRESPONSE
DESCRIPTOR.message_types_by_name['RegisterRequest'] = _REGISTERREQUEST
DESCRIPTOR.message_types_by_name['RegisterResponse'] = _REGISTERRESPONSE
DESCRIPTOR.message_types_by_name['SetImsiRequest'] = _SETIMSIREQUEST
DESCRIPTOR.message_types_by_name['SetImsiResponse'] = _SETIMSIRESPONSE
DESCRIPTOR.message_types_by_name['FindDronesResponse'] = _FINDDRONESRESPONSE
DESCRIPTOR.message_types_by_name['UpdateDroneRequest'] = _UPDATEDRONEREQUEST
DESCRIPTOR.message_types_by_name['UpdateDroneResponse'] = _UPDATEDRONERESPONSE
DESCRIPTOR.message_types_by_name['GetKeysResponse'] = _GETKEYSRESPONSE
DESCRIPTOR.message_types_by_name['DeleteRequest'] = _DELETEREQUEST
DESCRIPTOR.message_types_by_name['DeleteResponse'] = _DELETERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AuthRequest = _reflection.GeneratedProtocolMessageType('AuthRequest', (_message.Message,), dict(
  DESCRIPTOR = _AUTHREQUEST,
  __module__ = 'proto.services.drone_pb2'
  # @@protoc_insertion_point(class_scope:drone.AuthRequest)
  ))
_sym_db.RegisterMessage(AuthRequest)

AuthResponse = _reflection.GeneratedProtocolMessageType('AuthResponse', (_message.Message,), dict(
  DESCRIPTOR = _AUTHRESPONSE,
  __module__ = 'proto.services.drone_pb2'
  # @@protoc_insertion_point(class_scope:drone.AuthResponse)
  ))
_sym_db.RegisterMessage(AuthResponse)

GetIDRequest = _reflection.GeneratedProtocolMessageType('GetIDRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETIDREQUEST,
  __module__ = 'proto.services.drone_pb2'
  # @@protoc_insertion_point(class_scope:drone.GetIDRequest)
  ))
_sym_db.RegisterMessage(GetIDRequest)

GetIDResponse = _reflection.GeneratedProtocolMessageType('GetIDResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETIDRESPONSE,
  __module__ = 'proto.services.drone_pb2'
  # @@protoc_insertion_point(class_scope:drone.GetIDResponse)
  ))
_sym_db.RegisterMessage(GetIDResponse)

RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERREQUEST,
  __module__ = 'proto.services.drone_pb2'
  # @@protoc_insertion_point(class_scope:drone.RegisterRequest)
  ))
_sym_db.RegisterMessage(RegisterRequest)

RegisterResponse = _reflection.GeneratedProtocolMessageType('RegisterResponse', (_message.Message,), dict(
  DESCRIPTOR = _REGISTERRESPONSE,
  __module__ = 'proto.services.drone_pb2'
  # @@protoc_insertion_point(class_scope:drone.RegisterResponse)
  ))
_sym_db.RegisterMessage(RegisterResponse)

SetImsiRequest = _reflection.GeneratedProtocolMessageType('SetImsiRequest', (_message.Message,), dict(
  DESCRIPTOR = _SETIMSIREQUEST,
  __module__ = 'proto.services.drone_pb2'
  # @@protoc_insertion_point(class_scope:drone.SetImsiRequest)
  ))
_sym_db.RegisterMessage(SetImsiRequest)

SetImsiResponse = _reflection.GeneratedProtocolMessageType('SetImsiResponse', (_message.Message,), dict(
  DESCRIPTOR = _SETIMSIRESPONSE,
  __module__ = 'proto.services.drone_pb2'
  # @@protoc_insertion_point(class_scope:drone.SetImsiResponse)
  ))
_sym_db.RegisterMessage(SetImsiResponse)

FindDronesResponse = _reflection.GeneratedProtocolMessageType('FindDronesResponse', (_message.Message,), dict(
  DESCRIPTOR = _FINDDRONESRESPONSE,
  __module__ = 'proto.services.drone_pb2'
  # @@protoc_insertion_point(class_scope:drone.FindDronesResponse)
  ))
_sym_db.RegisterMessage(FindDronesResponse)

UpdateDroneRequest = _reflection.GeneratedProtocolMessageType('UpdateDroneRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEDRONEREQUEST,
  __module__ = 'proto.services.drone_pb2'
  # @@protoc_insertion_point(class_scope:drone.UpdateDroneRequest)
  ))
_sym_db.RegisterMessage(UpdateDroneRequest)

UpdateDroneResponse = _reflection.GeneratedProtocolMessageType('UpdateDroneResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEDRONERESPONSE,
  __module__ = 'proto.services.drone_pb2'
  # @@protoc_insertion_point(class_scope:drone.UpdateDroneResponse)
  ))
_sym_db.RegisterMessage(UpdateDroneResponse)

GetKeysResponse = _reflection.GeneratedProtocolMessageType('GetKeysResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETKEYSRESPONSE,
  __module__ = 'proto.services.drone_pb2'
  # @@protoc_insertion_point(class_scope:drone.GetKeysResponse)
  ))
_sym_db.RegisterMessage(GetKeysResponse)

DeleteRequest = _reflection.GeneratedProtocolMessageType('DeleteRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEREQUEST,
  __module__ = 'proto.services.drone_pb2'
  # @@protoc_insertion_point(class_scope:drone.DeleteRequest)
  ))
_sym_db.RegisterMessage(DeleteRequest)

DeleteResponse = _reflection.GeneratedProtocolMessageType('DeleteResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETERESPONSE,
  __module__ = 'proto.services.drone_pb2'
  # @@protoc_insertion_point(class_scope:drone.DeleteResponse)
  ))
_sym_db.RegisterMessage(DeleteResponse)


DESCRIPTOR._options = None

_DRONE = _descriptor.ServiceDescriptor(
  name='Drone',
  full_name='drone.Drone',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=710,
  serialized_end=1068,
  methods=[
  _descriptor.MethodDescriptor(
    name='Authorize',
    full_name='drone.Drone.Authorize',
    index=0,
    containing_service=None,
    input_type=_AUTHREQUEST,
    output_type=_AUTHRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetID',
    full_name='drone.Drone.GetID',
    index=1,
    containing_service=None,
    input_type=_GETIDREQUEST,
    output_type=_GETIDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Register',
    full_name='drone.Drone.Register',
    index=2,
    containing_service=None,
    input_type=_REGISTERREQUEST,
    output_type=_REGISTERRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SetIMSI',
    full_name='drone.Drone.SetIMSI',
    index=3,
    containing_service=None,
    input_type=_SETIMSIREQUEST,
    output_type=_SETIMSIRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Find',
    full_name='drone.Drone.Find',
    index=4,
    containing_service=None,
    input_type=google_dot_protobuf_dot_empty__pb2._EMPTY,
    output_type=_FINDDRONESRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='drone.Drone.Delete',
    index=5,
    containing_service=None,
    input_type=_DELETEREQUEST,
    output_type=_DELETERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DRONE)

DESCRIPTOR.services_by_name['Drone'] = _DRONE

# @@protoc_insertion_point(module_scope)
