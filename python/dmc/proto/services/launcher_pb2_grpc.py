# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


class LauncherStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Stream = channel.stream_stream(
        '/launcher.Launcher/Stream',
        request_serializer=google_dot_protobuf_dot_any__pb2.Any.SerializeToString,
        response_deserializer=google_dot_protobuf_dot_any__pb2.Any.FromString,
        )


class LauncherServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Stream(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LauncherServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Stream': grpc.stream_stream_rpc_method_handler(
          servicer.Stream,
          request_deserializer=google_dot_protobuf_dot_any__pb2.Any.FromString,
          response_serializer=google_dot_protobuf_dot_any__pb2.Any.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'launcher.Launcher', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
