# Dockerfile
FROM ubuntu:trusty

RUN apt-get update
RUN apt-get install -y \
    build-essential \
    fakeroot \
    gcc-arm-linux-gnueabi \
    g++-arm-linux-gnueabi \
    python

# additional packages useful for debugging
# RUN apt-get install -y \
#     tmux \
#     vim

COPY ./entrypoint.py /tmp/
ENTRYPOINT ["/tmp/entrypoint.py"]

# CMD ["/bin/bash"]
CMD ["--help"]
