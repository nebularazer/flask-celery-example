import sys
import os

from click import echo

from example import create_app

app = create_app('development')


@app.cli.command('urlmap')
def urlmap():
    """Prints out all routes"""
    echo("{:50s} {:40s} {}".format('Endpoint', 'Methods', 'Route'))
    for route in app.url_map.iter_rules():
        methods = ','.join(route.methods)
        echo("{:50s} {:40s} {}".format(route.endpoint, methods, route))


@app.cli.command('ipython')
def ipython():
    """Runs a ipython shell in the app context."""
    try:
        import IPython
    except ImportError:
        echo("IPython not found. Install with: 'pip install ipython'")
        return
    from flask.globals import _app_ctx_stack
    app = _app_ctx_stack.top.app
    banner = 'Python %s on %s\nIPython: %s\nApp: %s%s\nInstance: %s\n' % (
        sys.version,
        sys.platform,
        IPython.__version__,
        app.import_name,
        app.debug and ' [debug]' or '',
        app.instance_path,
    )

    ctx = {}

    # Support the regular Python interpreter startup script if someone
    # is using it.
    startup = os.environ.get('PYTHONSTARTUP')
    if startup and os.path.isfile(startup):
        with open(startup, 'r') as f:
            eval(compile(f.read(), startup, 'exec'), ctx)

    ctx.update(app.make_shell_context())

    IPython.embed(banner1=banner, user_ns=ctx)
