# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import taskmanager_pb2 as taskmanager__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in taskmanager_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class TaskManagerStub(object):
    """TaskManager service handles task-related operations
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTask = channel.unary_unary(
                '/taskmanager.TaskManager/GetTask',
                request_serializer=taskmanager__pb2.TaskRequest.SerializeToString,
                response_deserializer=taskmanager__pb2.TaskResponse.FromString,
                _registered_method=True)
        self.AddTask = channel.unary_unary(
                '/taskmanager.TaskManager/AddTask',
                request_serializer=taskmanager__pb2.Task.SerializeToString,
                response_deserializer=taskmanager__pb2.TaskResponse.FromString,
                _registered_method=True)
        self.ListTasks = channel.unary_unary(
                '/taskmanager.TaskManager/ListTasks',
                request_serializer=taskmanager__pb2.Empty.SerializeToString,
                response_deserializer=taskmanager__pb2.TaskList.FromString,
                _registered_method=True)
        self.DeleteTask = channel.unary_unary(
                '/taskmanager.TaskManager/DeleteTask',
                request_serializer=taskmanager__pb2.TaskRequest.SerializeToString,
                response_deserializer=taskmanager__pb2.DeleteResponse.FromString,
                _registered_method=True)
        self.UpdateTask = channel.unary_unary(
                '/taskmanager.TaskManager/UpdateTask',
                request_serializer=taskmanager__pb2.UpdateTaskRequest.SerializeToString,
                response_deserializer=taskmanager__pb2.TaskResponse.FromString,
                _registered_method=True)


class TaskManagerServicer(object):
    """TaskManager service handles task-related operations
    """

    def GetTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTasks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TaskManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTask': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTask,
                    request_deserializer=taskmanager__pb2.TaskRequest.FromString,
                    response_serializer=taskmanager__pb2.TaskResponse.SerializeToString,
            ),
            'AddTask': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTask,
                    request_deserializer=taskmanager__pb2.Task.FromString,
                    response_serializer=taskmanager__pb2.TaskResponse.SerializeToString,
            ),
            'ListTasks': grpc.unary_unary_rpc_method_handler(
                    servicer.ListTasks,
                    request_deserializer=taskmanager__pb2.Empty.FromString,
                    response_serializer=taskmanager__pb2.TaskList.SerializeToString,
            ),
            'DeleteTask': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteTask,
                    request_deserializer=taskmanager__pb2.TaskRequest.FromString,
                    response_serializer=taskmanager__pb2.DeleteResponse.SerializeToString,
            ),
            'UpdateTask': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateTask,
                    request_deserializer=taskmanager__pb2.UpdateTaskRequest.FromString,
                    response_serializer=taskmanager__pb2.TaskResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'taskmanager.TaskManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('taskmanager.TaskManager', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class TaskManager(object):
    """TaskManager service handles task-related operations
    """

    @staticmethod
    def GetTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/taskmanager.TaskManager/GetTask',
            taskmanager__pb2.TaskRequest.SerializeToString,
            taskmanager__pb2.TaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/taskmanager.TaskManager/AddTask',
            taskmanager__pb2.Task.SerializeToString,
            taskmanager__pb2.TaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListTasks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/taskmanager.TaskManager/ListTasks',
            taskmanager__pb2.Empty.SerializeToString,
            taskmanager__pb2.TaskList.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/taskmanager.TaskManager/DeleteTask',
            taskmanager__pb2.TaskRequest.SerializeToString,
            taskmanager__pb2.DeleteResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateTask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/taskmanager.TaskManager/UpdateTask',
            taskmanager__pb2.UpdateTaskRequest.SerializeToString,
            taskmanager__pb2.TaskResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
