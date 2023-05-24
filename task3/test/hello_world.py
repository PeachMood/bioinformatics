from dagster import job, op

@op
def print_hello_world(context):
    context.log.info('Hello, world!')

@job
def test_dagster():
    print_hello_world()
