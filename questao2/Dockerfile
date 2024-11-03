# Usando a imagem Ubuntu 22.04 (compatível com ROS 2 Humble)
FROM ubuntu:22.04

# Configurações de ambiente
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8

# Atualiza e instala dependências essenciais
RUN apt-get update && apt-get install -y \
    locales \
    curl \
    gnupg2 \
    lsb-release \
    && locale-gen en_US en_US.UTF-8 \
    && update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8

# Adiciona o repositório do ROS 2 Humble e a chave GPG
RUN apt update && apt install -y curl gnupg lsb-release
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | apt-key add -
RUN echo "deb [trusted=yes] https://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/ros2-latest.list

# Instala o ROS 2 Humble e ferramentas de desenvolvimento
RUN apt update && apt install -y \
    ros-humble-ros-base \
    python3-colcon-common-extensions \
    build-essential \
    python3-argcomplete \
    python3-pip \
    && rosdep init \
    && rosdep update

# Instala pacotes adicionais de mensagens e comunicação ROS 2
RUN apt install -y \
    ros-humble-rmw-fastrtps-cpp \
    ros-humble-rmw-cyclonedds-cpp \
    ros-humble-ros2launch

# Configura o ambiente ROS 2 no bash
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
SHELL ["/bin/bash", "-c"]

# Copia o workspace contendo os pacotes ROS 2 para o container
COPY workspace /workspace

# Define o diretório de trabalho para o workspace
WORKDIR /workspace

# Instala dependências dos pacotes (se houver)
RUN rosdep install --from-paths src --ignore-src -r -y

# Constrói o workspace com os pacotes
RUN source /opt/ros/humble/setup.bash && colcon build

# Seta o ambiente do ROS 2 para que o workspace seja incluído automaticamente ao iniciar o container
RUN echo "source /workspace/install/setup.bash" >> ~/.bashrc

# Define o ponto de entrada do container
CMD ["bash"]
