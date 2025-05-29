import docker

def start(port: int = 2222) -> docker.models.containers.Container:
    client = docker.from_env()
    return client.containers.run(
        "cowrie/cowrie", 
        name="cowrie", 
        detach=True, 
        ports={"2222/tcp": 2222}
    )

def stop() -> None:
    container = clients.containers.get("cowrie")
    container.stop()
    container.remove()

