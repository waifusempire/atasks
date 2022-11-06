# Examples

```py
# Example 1
from atasks import Tasks

async with Tasks() as tasks:
    tasks.sleep(2)
    tasks.sleep(2)

print(tasks.results)
```

```py
# Example 1
from atasks import Tasks

tasks = Tasks()
tasks.sleep(2)
tasks.sleep(2)
await tasks.resolve()

print(tasks.results)
```
