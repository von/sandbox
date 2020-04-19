import click


@click.group(invoke_without_command=True)
# Boolean option with "/"
@click.option('--test/--no-test', default=False)
@click.pass_context
def cli(ctx, test):
    ctx.obj = {}
    ctx.obj["TEST"] = test
    if ctx.invoked_subcommand is None:
        click.echo('I was invoked without subcommand')
    else:
        click.echo('I am about to invoke %s' % ctx.invoked_subcommand)


@cli.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
@click.pass_obj
def hello(cfg, count, name):
    if cfg["TEST"]:
        click.echo('Testing!')
    for x in range(count):
        click.echo('Hello %s!' % name)


@cli.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
@click.pass_obj
def goodbye(cfg, count, name):
    if cfg["TEST"]:
        click.echo('Testing!')
    for x in range(count):
        click.echo('Goodbye %s!' % name)
