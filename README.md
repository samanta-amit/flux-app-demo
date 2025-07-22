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

Error
```
root@flux-sample-0:/opt/stream# flux run -N 1 hostname
0.377s: flux-shell[0]: ERROR: plugin 'oom': shell.init failed
0.377s: flux-shell[0]: FATAL: shell_init
0.378s: job.exception type=exec severity=0 shell_init
flux-job: task(s) exited with exit code 1
```
