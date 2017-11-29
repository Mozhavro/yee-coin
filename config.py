# A list of rules that block hash should follow to be considered as 
# valid. Each rule should be a callable that return bool value.
VALIDATION_RULES = (
    lambda x: x.startswith("1337"),
    lambda x: x.endswith("1"),
)