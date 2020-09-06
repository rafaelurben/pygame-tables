# pygame-tables

You need to create tables in pygame?

Then this might help you!

## Usage

```python

rows = [
    ("Rafael", 16, "Switzerland"),
    ("Someone", 100, "Germany")
]

settings = [
    ("Name",    20, False),
    ("Age",      3, True),
    ("Country", 15, False),
    # (title, max_length, align (right: True, left: False))
]

table = Table(rows, settings)
#table.draw(<Pygame Surface object>, x, y)

```
