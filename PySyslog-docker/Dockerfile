FROM rockylinux/rockylinux:8

WORKDIR /usr/src/app

RUN dnf -y install python3 python3-pip && \
    dnf clean all && \
    rm -rf /var/cache/dnf


CMD ["python3", "pysyslog.py"]