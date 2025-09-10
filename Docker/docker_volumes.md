1. Volumes are persistent data stores for containers. 

2. We can allocate a part of the storage from the host machine which is managed by the docker. The docker stores all the data in those volumes. Whenever the container is restarted it doesnt lose its data. 

3. You can map multiple containers with the same volume. 

4. Command to attach a volume to the container/. 

docker run -it -v /Users/whatever/data:/test/data ubuntu  

-> The first path is the absolute path of the host machine and the second is the relative path of the container. 

5. docker volumes command:
    - docker volumes ls  -> lIST OUT ALL THE VOLUMES
    - docker volume create VOL_NAME -> CREATE A CUSTOM VOLUME
    - docker volume rm VOL_NAME  -> Removes a volume. 