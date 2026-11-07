import collections
import json
from collections import defaultdict
from pathlib import Path


# ---------------------------------------------------------------
# 练习（自己动手，先别看下面的答案思路）
# ---------------------------------------------------------------
# 1) 取出 response 里第一条 choice 的 finish_reason
# 2) 把 messages 里所有 role 为 "user" 的消息，改成 {"role": "user", "content": 大写}
#    提示：列表推导里直接构造新 dict
# 3) 安全取出 response["usage"]["completion_tokens"]，要求 usage 缺失时返回 0 而不是崩溃
# 4) 给定 tools = [{"name": "search"}, {"name": "calc"}, {"name": "search"}]
#    统计每个工具名出现的次数（用上面 role_count 的套路）
# 5) 把 messages 追加一条新消息后写回 JSON 文件，再读出来验证条数 +1
# ---------------------------------------------------------------


response = {
    "id": "chatcmpl-abc123",
    "model": "deepseek-chat",
    "choices": [
        {
            "index": 0,
            "message": {"role": "assistant", "content": "你好，我是 Agent"},
            "finish_reason": "stop",
        }
    ],
    "usage": {"prompt_tokens": 10, "completion_tokens": 8}
}

content=response["choices"][0]["message"]["content"]
print("content:",content)

finish_reason = response["choices"][0]["finish_reason"]
print("finish_reason:",finish_reason)

messages = [
    {"role": "system", "content": "你是助手"},
    {"role": "user", "content": "aa"},
    {"role": "assistant", "content": "回答1"},
    {"role": "user", "content": "问题2"},
]

upper_msg = []
for m in messages:
    if m["role"] == "user":
        upper_msg.append({**m, "content": m["content"].upper()})
    else:
        upper_msg.append(m)
print(upper_msg)
print(messages)

# total = 0
# if "usage" in response:
#     total = response["usage"]["completion_tokens"] + response["usage"]["prompt_tokens"]
#     print("total:",total)
usage=response.get("usage",{})
total = usage.get("completion_tokens",0) + usage.get("prompt_tokens",0)
print("total:",total)

tool_count={}
tools = [{"name": "search"}, {"name": "calc"}, {"name": "search"}]
for t in tools:
    map1 = t["name"]
    tool_count[map1] = tool_count.get(map1, 0) + 1
print(tool_count)

print(len(messages))
messages.append({"role": "user", "content": "问题3"})


out=Path("test.json")
out.write_text(json.dumps(messages, ensure_ascii=False, indent=2), encoding="utf-8")
finalMsg=json.loads(out.read_text(encoding="utf-8"))
out.resolve()
print(len(finalMsg))


##
to_lst=[m["name"] for m in tools]
aa= collections.Counter(to_lst)
print(aa)

tmplist=defaultdict(list)
for m in tools:
    tmplist["name"].append(m["name"])
print(dict(tmplist))
