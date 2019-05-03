## build and push

You need `microk8s.enable registry` to push into `localhost:32000`
then microk8s will find images when run
you can check how many images with command `microk8s.ctl -n k8s.io images ls` (so yes they just put it in `k8s.io` namespace)


## MountVolumn

you can mount just fine but template can't handle relative path ti used it you need helm


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