# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from proto import messages_pb2 as proto_dot_messages__pb2
from proto.services import user_pb2 as proto_dot_services_dot_user__pb2


class UserStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Stream = channel.unary_stream(
        '/user.User/Stream',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=proto_dot_messages__pb2.Message.FromString,
        )
    self.Mission = channel.unary_unary(
        '/user.User/Mission',
        request_serializer=proto_dot_services_dot_user__pb2.MissionRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Action = channel.unary_unary(
        '/user.User/Action',
        request_serializer=proto_dot_services_dot_user__pb2.ActionRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Control = channel.unary_unary(
        '/user.User/Control',
        request_serializer=proto_dot_services_dot_user__pb2.ControlRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )
    self.Command = channel.unary_unary(
        '/user.User/Command',
        request_serializer=proto_dot_services_dot_user__pb2.CommandRequest.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
        )


class UserServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Stream(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Mission(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Action(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Control(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Command(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_UserServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Stream': grpc.unary_stream_rpc_method_handler(
          servicer.Stream,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=proto_dot_messages__pb2.Message.SerializeToString,
      ),
      'Mission': grpc.unary_unary_rpc_method_handler(
          servicer.Mission,
          request_deserializer=proto_dot_services_dot_user__pb2.MissionRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Action': grpc.unary_unary_rpc_method_handler(
          servicer.Action,
          request_deserializer=proto_dot_services_dot_user__pb2.ActionRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Control': grpc.unary_unary_rpc_method_handler(
          servicer.Control,
          request_deserializer=proto_dot_services_dot_user__pb2.ControlRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
      'Command': grpc.unary_unary_rpc_method_handler(
          servicer.Command,
          request_deserializer=proto_dot_services_dot_user__pb2.CommandRequest.FromString,
          response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'user.User', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))