## Docker commands — simple explanations

This cheat-sheet lists common Docker commands and important flags with short, easy explanations.

---

## Image commands
- docker pull <image[:tag]>
  - Download an image from a registry (default: Docker Hub). Add :tag to pick a version.
- docker images
  - Show images stored locally.
- docker rmi <image> [<image2>...]
  - Remove one or more local images. Images must not be in use by containers.
- docker tag <source> <target>
  - Give an image a new name (useful before docker push).
- docker push <image[:tag]>
  - Upload a tagged image to a registry.

## Container lifecycle
- docker run [flags] <image> [command]
  - Create and start a new container from an image. Common flags below.
- docker create [flags] <image> [command]
  - Create a container but do not start it (useful for configuring before starting).
- docker start <container>
  - Start a stopped container.
- docker stop <container>
  - Gracefully stop a running container (sends SIGTERM then SIGKILL after timeout).
- docker restart <container>
  - Stop and then start a container.
- docker kill <container>
  - Send SIGKILL to immediately stop a container.
- docker rm <container> [<container2>...]
  - Remove one or more stopped containers. Use -f to force remove running ones.
- docker ps
  - List running containers.
- docker ps -a
  - List all containers (running and stopped).

## Inspect & logs
- docker logs <container>
  - Show stdout/stderr of a container.
  - Flags: -f (follow), --tail N (last N lines).
- docker inspect <container|image>
  - Show low-level JSON details about an object.
- docker stats [container...]
  - Live resource usage (CPU/memory) for containers.
- docker top <container>
  - Show processes running inside the container.

## Execute / attach
- docker exec [flags] <container> <command>
  - Run a command inside a running container.
  - Common: -it to get an interactive shell (see flags).
- docker attach <container>
  - Attach your terminal to a running container's main process output.

## Build & Dockerfile
- docker build [flags] <path>
  - Build an image from a Dockerfile in <path>.
  - Common flags: -t <name:tag> (name the image), --no-cache, -f <Dockerfile>.
- docker save -o file.tar <image>
  - Export an image to a tar file.
- docker load -i file.tar
  - Load an image from a tar file.

## Volumes & files
- docker volume create <name>
  - Create a named volume.
- docker volume ls
  - List volumes.
- docker volume rm <name>
  - Remove volume.
- docker cp <src> <dest>
  - Copy files between host and container (or container->host).

## Networks
- docker network create <name>
  - Create a user-defined network.
- docker network ls
  - List networks.
- docker network inspect <name>
  - Show network details.
- docker network rm <name>
  - Remove a network.

## System & cleanup
- docker system df
  - Show disk usage by images, containers, and volumes.
- docker system prune
  - Remove unused containers, networks, images, and build cache (use with caution).
- docker image prune
  - Remove dangling images.
- docker container prune
  - Remove stopped containers.

## Compose (multi-container apps)
- docker compose up [--build] [-d]
  - Start services from docker-compose.yml (or compose.yaml). --build rebuilds images, -d detaches.
- docker compose down
  - Stop and remove containers, networks created by compose.
- docker compose logs [-f]
  - View logs for compose services.

---

## Important docker run flags (simple)
- -d, --detach
  - Run container in background (detached mode).
- -it
  - -i keeps STDIN open; -t allocates a pseudo-TTY. Commonly used together to get an interactive shell.
- --name <name>
  - Assign a custom name to the container.
- -p <host_port>:<container_port>
  - Map a host port to a container port (publish).
- -P (uppercase)
  - Publish all exposed ports to random host ports.
- --rm
  - Automatically remove container when it stops.
- -e KEY=val or --env KEY=val
  - Set environment variable inside container.
- --env-file <file>
  - Load environment variables from a file.
- -v <host_path>:<container_path> or --mount
  - Mount a host directory or named volume into the container (persist data).
- --network <network>
  - Connect the container to a specific Docker network.
- --restart <policy>
  - Restart policy: no, on-failure[:max-retries], always, unless-stopped.
- --cpus <value>, -m/--memory <value>
  - Limit CPU and memory the container can use.
- --user <uid[:gid]>
  - Run container process as a specific user id.
- --entrypoint <cmd>
  - Override the image entrypoint.
- --privileged
  - Give the container extended privileges (use sparingly).

## Security & troubleshooting
- docker inspect, docker logs, docker exec -it <container> /bin/sh
  - Common steps to debug containers.
- Avoid running unnecessary --privileged or mapping sensitive host paths.
- Use user namespaces, read-only mounts, and resource limits to reduce risk.

---

This file is a concise reference. For full details see `docker --help` and the official docs at https://docs.docker.com.