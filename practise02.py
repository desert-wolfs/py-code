from typing import Any


def call_llm(prompt: str, model:str = "deepseek-chat", temperature: float = 0.7) -> str:
    return f"[{model}] {prompt} (t={temperature})"

print(call_llm("你好"))
print(call_llm("你好", temperature=0.2))
print(call_llm(temperature=0.1, prompt="反过来传也行"))

def bad(items=[]):
    items.append(1)
    return items

print(bad())
print(bad())
print(bad())

def bad2(items=[]):
    items.append(1)
    return items
print("一次", bad2(), bad2(), bad2())

def good(items=None):
    items = items or []
    items.append(1)
    return items
print(good(), good(), good())

def total(*count:int) -> int:
    return sum(count)
print(total(10), total(10, 20, 30))

def call_tool(name:str, **params:Any) -> str:
    return f"[{name}] {params}"
print(call_tool("tool1", a=1, b=2))
print(call_tool("tool2", c=3, d=4))