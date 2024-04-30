from prefect import flow, task
from prefect.deployments import DeploymentImage


@task(log_prints=True)
def return_hello():
    return "Hello"


@task(log_prints=True)
def return_world():
    return "world"


@task(log_prints=True)
def return_exclamation():
    return "!"


@flow(log_prints=True)
def print_hello_world():
    hello = return_hello()
    world = return_world()
    exclamation = return_exclamation()
    print(f"{hello} {world}{exclamation}")


if __name__ == "__main__":
    print_hello_world.deploy(
        name="my-deployment",
        work_pool_name="parsons-iac-demo-pool",
        cron="0 1 * * *",
        image=DeploymentImage(
            name="my-image:latest",
            platform="linux/amd64",
        ),
    )
