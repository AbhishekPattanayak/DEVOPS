1. Lets say you have two containers which uses each other, then the containers would have to be in the same network. 

2. docker network ls -> lists out all the network that is created. 

3. docker network create <NETWORK_NAME>  -> Creates a network. 

4. So there are two types of Networking inside a container
    4.1 Host networking -> This is where the application uses the port from the machine and the application can be accessed using the host-machine IP add and port
    4.2 Problem with this type of networking is that the other containers can-not use the same port again as the port is already in use. 
    4.3 Bridge Networking -> This is where the containers have different IP and can consume same port as the IP add is different. 
    4.4 In this network the containers can talk with each other as they are on the same network. 