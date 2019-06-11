# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto.services import layers_pb2 as proto_dot_services_dot_layers__pb2


class LayersStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetLayer = channel.unary_unary(
        '/layers.Layers/GetLayer',
        request_serializer=proto_dot_services_dot_layers__pb2.GetRequest.SerializeToString,
        response_deserializer=proto_dot_services_dot_layers__pb2.GetResponse.FromString,
        )
    self.GetInternal = channel.unary_unary(
        '/layers.Layers/GetInternal',
        request_serializer=proto_dot_services_dot_layers__pb2.GetInternalRequest.SerializeToString,
        response_deserializer=proto_dot_services_dot_layers__pb2.GetInternalResponse.FromString,
        )


class LayersServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetLayer(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetInternal(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LayersServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetLayer': grpc.unary_unary_rpc_method_handler(
          servicer.GetLayer,
          request_deserializer=proto_dot_services_dot_layers__pb2.GetRequest.FromString,
          response_serializer=proto_dot_services_dot_layers__pb2.GetResponse.SerializeToString,
      ),
      'GetInternal': grpc.unary_unary_rpc_method_handler(
          servicer.GetInternal,
          request_deserializer=proto_dot_services_dot_layers__pb2.GetInternalRequest.FromString,
          response_serializer=proto_dot_services_dot_layers__pb2.GetInternalResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'layers.Layers', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
