#!/usr/bin/env bash

deploy() {
    kubectl create -f ../deploy/kubernetes/csi-nvmesh-deployment.yaml
    kubectl create -f ../deploy/kubernetes/rbac-permissions.yaml
}

show_logs() {
    # wait for pod to start
    sleep 1

    kubectl logs nvmesh-csi-controller-0 -c nvmesh-csi-plugin --follow
}


### MAIN ###
############

./clear_old_deployment.sh
cd ../
./docker_build.sh
deploy
#show_logs
