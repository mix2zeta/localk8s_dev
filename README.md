## Require

https://microk8s.io/
docker

## build and push

You need `microk8s.enable registry` to push into `localhost:32000`
then microk8s will find images when run
you can check how many images with command `microk8s.ctl -n k8s.io images ls` (so yes they just put it in `k8s.io` namespace)


## Mount Volume

you can mount just fine but template can't handle relative path, To used it you need helm.
```
volumeMounts:
    - mountPath: /usr/src
    name: kubetest-volume
volumes:
- name: kubetest-volume
hostPath:
    path: /home/miz/Project/localk8s_dev/tornado
    type: Directory
```

## Debug

to run like `docker run --rm` 
```
mk8s run -i --tty --rm debug --image=localhost:32000/localk8s:latest --restart=Never -- python /usr/src/hello.py
```

for long run service you need to enable tty when create pod  so you put this option in template
```
tty: true
stdin: true
```

then you can attach to it with
```
mk8s attach localk8s-deployment-78b94c757-k4w9b -it
```