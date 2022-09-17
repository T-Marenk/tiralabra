from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/index.py",  pty=True)

@task
def ratkoja(ctx):
    ctx.run("python3 src/index_ratkoja.py", pty=True)

@task
def coverage_report(ctx):
    ctx.run("coverage report -m")

@task
def test(ctx):
    ctx.run("pytest src")