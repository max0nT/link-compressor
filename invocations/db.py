import invoke


@invoke.task
def init(context: invoke.context.Context):
    """Init db."""
    context.run(
        "sqlite3 database.db < create_table.sql"
    )
