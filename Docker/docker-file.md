1. FROM

Purpose: Defines the base image for your Docker image.

Example:

FROM ubuntu:20.04


Explanation: Every Docker image starts from a base image (like Ubuntu, Debian, Alpine, or even scratch for empty).

2. RUN

Purpose: Executes commands inside the image during build time.

Example:

RUN apt-get update && apt-get install -y python3


Explanation: Used to install packages, update files, or configure the environment. Each RUN creates a new layer in the image.

3. CMD

Purpose: Specifies the default command to run when a container starts.

Example:

CMD ["python3", "app.py"]


Explanation: Unlike RUN, CMD executes at container runtime, not during build. A Dockerfile can only have one CMD (last one overrides previous).

4. ENTRYPOINT

Purpose: Configures a container to run as an executable.

Example:

ENTRYPOINT ["python3", "app.py"]


Explanation: Similar to CMD but harder to override. Often used for apps where the container should always run a specific process.

5. COPY

Purpose: Copies files from your local machine into the image.

Example:

COPY ./app /usr/src/app


Explanation: Used for application source code or config files.

6. ADD

Purpose: Similar to COPY, but also supports URLs and automatic extraction of compressed files.

Example:

ADD app.tar.gz /usr/src/app/


Explanation: Generally, COPY is preferred unless you specifically need ADD features.

7. WORKDIR

Purpose: Sets the working directory for subsequent instructions.

Example:

WORKDIR /usr/src/app


Explanation: Instead of writing full paths everywhere, this changes the "current directory".

8. EXPOSE

Purpose: Informs Docker that the container listens on specific ports.

Example:

EXPOSE 5000


Explanation: This does not publish the port; it’s just documentation. Use -p with docker run to expose ports outside.

9. ENV

Purpose: Sets environment variables.

Example:

ENV APP_ENV=production


Explanation: Useful for configuration values or secrets (though sensitive secrets are better with Docker secrets).

10. VOLUME

Purpose: Defines mount points for external volumes.

Example:

VOLUME ["/data"]


Explanation: Persists data even if the container is deleted.

11. ARG

Purpose: Defines build-time variables.

Example:

ARG VERSION=1.0
RUN echo "Building version $VERSION"


Explanation: Unlike ENV, ARG values are only available while building, not at runtime.

12. LABEL

Purpose: Adds metadata to the image.

Example:

LABEL maintainer="you@example.com"


Explanation: Useful for documentation, versioning, ownership, etc.

13. Command to build the docker image: docker build -t testapp:1.0  -> -t meaning tags, we are specifying the tags of the docker image