from typing import Optional, TypedDict
import json


class BlockList(TypedDict):
    email_address: str
    days_to_expire: Optional[int]


a = BlockList(email_address="a")

print(a)
print(json.dumps(a))
