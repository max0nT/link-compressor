import invoke

@invoke.task
def run(context: invoke.context.Context):
    """Run tests."""
    context.run
    context.run(
        "sqlite3 test.db < create_table.sql &&"
        " pytest ./src/tests; "
        " rm -f test.db"
    )

