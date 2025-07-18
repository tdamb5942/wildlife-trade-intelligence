from dagster import asset


@asset
def hello_wtie():
    return "Hello from Wildlife Trade Intelligence"
