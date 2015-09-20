import click


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo('I was invoked without subcommand')
    else:
        click.echo('I am about to invoke %s' % ctx.invoked_subcommand)


@cli.command()
@click.option('--count', default=1, help='number of greetings')
# Boolean option with "/"
@click.option('--test/--no-test', default=False)
@click.argument('name')
def hello(count, test, name):
    if test:
        click.echo('Testing!')
    for x in range(count):
        click.echo('Hello %s!' % name)


@cli.command()
@click.option('--count', default=1, help='number of greetings')
# Boolean option with "/"
@click.option('--test/--no-test', default=False)
@click.argument('name')
def goodbye(count, test, name):
    if test:
        click.echo('Testing!')
    for x in range(count):
        click.echo('Goodbye %s!' % name)
