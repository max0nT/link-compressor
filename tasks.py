import invoke

import invocations

ns = invoke.Collection(
    invocations.db,
    invocations.app,
    invocations.tests
)
