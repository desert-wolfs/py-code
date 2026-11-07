
import json
from pathlib import Path


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
    "usage": {"prompt_tokens": 10, "completion_tokens": 8},
}

content=response["choices"][0]["message"]["content"]
print("content:",content)

usage = response["usage"]
print("usage:",usage)

apg = response.get("apg", "未返回")
print("apg:",apg)

total=response["usage"]["completion_tokens"] + response["usage"]["prompt_tokens"]
print("total:",total)

if "usage" in response:
    total1 = response["usage"]["prompt_tokens"] + response["usage"]["completion_tokens"]
    print("total1:",total1)

messages = [
    {"role": "system", "content": "你是助手"},
    {"role": "user", "content": "问题1"},
    {"role": "assistant", "content": "回答1"},
    {"role": "user", "content": "问题2"},
]

# 最后2条
m1=[m["content"] for m in messages[-2:]]
print(m1)
# 跳过第1条
m2=[m["content"] for m in messages[1:]]
print(m2)
# 倒序
m3=[m["content"] for m in messages[::-1]]
print(m3)
m4=[m["content"] for m in messages[:-1]]
print(m4)

m5=[m["content"] for m in messages[:-1][-1:]]
print(m5)

recent = messages[-3:]
print("   只保留最近 3 条:", [m["role"] for m in recent])

user_content=[m["content"] for m in messages if m["role"] == "user"]
print(user_content)

count_map={}
for m in messages:
    role=m["role"]
    count_map[role]=count_map.get(role,0)+1
print(count_map)

jsonStr=json.dumps(response, ensure_ascii=False, indent=2)
print(jsonStr)
print(len(jsonStr))

response2=json.loads(jsonStr)
print("是否相等", response==response2)
print("是否相等", len(response2))

out=Path("day01_test.json")
out.write_text(jsonStr, encoding="utf-8")
reLoad=json.loads(out.read_text(encoding="utf-8"))
print(reLoad)
print("重新加载",len(reLoad)  )
print("文件：", out.resolve())