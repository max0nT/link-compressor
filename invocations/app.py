import invoke

@invoke.task
def run(context: invoke.context.Context):
    """Run fastapi app."""
    context.run(
        "python -m uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload",
    )
