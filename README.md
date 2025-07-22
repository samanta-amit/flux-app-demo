# Instructions

##
```
kind create cluster --config kind-config.yaml --name flux-cluster --loglevel debug
kubectl get nodes
kubectl apply -f flux-operator.yaml
kubectl get pods -n operator-system
kubectl apply -f stream.yaml
kubectl get pods -n default | grep flux-sample
kubectl exec -it -n default flux-sample-0-gscrb -c flux-sample -- bash
flux proxy local:///mnt/flux/view/run/flux/local bash
flux resource list
```
