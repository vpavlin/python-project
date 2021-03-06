FROM fedora:22

MAINTAINER Vaclav Pavlin <vpavlin@redhat.com>

WORKDIR /opt/$PROJECT$

# add all of Atomic App's files to the container image
ADD $PROJECT$/ /opt/$PROJECT$/$PROJECT$/
ADD setup.py requirements.txt /opt/$PROJECT$/


# lets install pip, and gcc for the native extensions
# and remove all after use
RUN dnf install -y --setopt=tsflags=nodocs python-pip python-setuptools && \
    python setup.py install && \
    dnf remove -y python-pip && \
    dnf clean all


# the entrypoint
ENTRYPOINT ["/usr/bin/$PROJECT$"]
