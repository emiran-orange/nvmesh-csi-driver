#!/usr/bin/env python
from NVMeshSDK.Utils import Utils
from NVMeshSDK.Entities.Entity import Entity
from NVMeshSDK.Entities.TargetsStatus import TargetsStatus
from NVMeshSDK.Entities.ClientsStatus import ClientsStatus
from NVMeshSDK.Entities.AttributeRepresentation import AttributeRepresentation


class ClusterStatus(Entity):
    Targets = AttributeRepresentation(display='Targets', dbKey='servers', type=TargetsStatus)
    Clients = AttributeRepresentation(display='Clients', dbKey='clients', type=ClientsStatus)
    Volumes = AttributeRepresentation(display='Volumes', dbKey='volumes')
    TotalSpace = AttributeRepresentation(display='Total Space', dbKey='totalSpace')
    AllocatedSpace = AttributeRepresentation(display='Allocated Space', dbKey='allocatedSpace')
    FreeSpace = AttributeRepresentation(display='Free Space', dbKey='freeSpace')
    ManagementVersion = AttributeRepresentation(display='Management Version', dbKey='managementVersion')

    __objectsToInstantiate = ['Targets', 'Clients']

    @Utils.initializer
    def __init__(self, servers=None, clients=None, volumes=None, totalSpace=None, allocatedSpace=None, freeSpace=None,
                 errors=None, warnings=None, managementVersion=None):
            """**Initializes cluster status entity**

                :param servers: targets in the cluster, defaults to None
                :type servers: TargetsStatus, optional
                :param clients: clients in the cluster, defaults to None
                :type clients: ClientsStatus, optional
                :param volumes: volumes in the cluster, defaults to None
                :type volumes: dict, optional
                :param totalSpace: total space in the cluster, defaults to None
                :type totalSpace: int, optional
                :param allocatedSpace: allocated space in the cluster, defaults to None
                :type allocatedSpace: int, optional
                :param freeSpace: free space in the cluster, defaults to None
                :type freeSpace: int, optional
                :param errors: errors, defaults to None
                :type errors: list, optional
                :param warnings: warnings, defaults to None
                :type warnings: list, optional
                :param managementVersion: management version, defaults to None
                :type managementVersion: str, optional
            """
            pass

    def getObjectsToInstantiate(self):
        return ClusterStatus.__objectsToInstantiate
