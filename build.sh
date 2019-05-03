#bin/bash

rm -f myimage.tar
cd tornado
docker build -t localhost:32000/localk8s .
docker push localhost:32000/localk8s

# docker save mynginx > myimage.tar
# microk8s.ctr -n k8s.io image import myimage.tar