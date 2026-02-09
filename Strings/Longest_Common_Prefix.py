
def longestCommonPrefix(st):
    pre = st[0]

    for s in st[1:]:
        while not s.startswith(pre):
            pre = pre[:-1]
            if pre == "":
                return ""

    return pre

st1 = ["dog", "cat", "animal", "monkey"]
st2 = ["flowers", "flow", "fly", "flight"]
print(longestCommonPrefix(st1))
print(longestCommonPrefix(st2))
