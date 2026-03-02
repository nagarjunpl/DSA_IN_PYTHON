# Function to check if string starts and ends with 'gfg'

def gfg(S):
    b = S.lower()
    
    if b.startswith("gfg") and b.endswith("gfg"):
        print("Yes")
    else:
        print("No")

S1 = "gfgHelloWorldgfg"
S2 = "gfgpython"
gfg(S1) # Output: Yes
gfg(S2) # Output: No
