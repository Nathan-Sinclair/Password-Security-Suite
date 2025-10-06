# docker/Dockerfile
FROM python:3.8-slim

ARG BUILD_JOHN=yes
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    wget \
    unzip \
    p7zip-full \
    zip \
    unrar \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    liblzma-dev \
    perl \
    pkg-config \
    python3-dev \
    libgmp-dev \
    jq \
  && rm -rf /var/lib/apt/lists/*

RUN if [ "${BUILD_JOHN}" = "yes" ]; then \
      git clone https://github.com/openwall/john.git /tmp/john && \
      cd /tmp/john/src && \
      ./configure --enable-plugins && make -s -j"$(nproc)" && \
      cp -r /tmp/john /opt/john && rm -rf /tmp/john ; \
    fi

ENV PATH="/opt/john/run:${PATH}"

COPY . /app

RUN pip install --no-cache-dir \
    requests \
    pwinput \
    bcrypt \
    argon2-cffi \
    scrypt

ENTRYPOINT ["python", "main.py"]
