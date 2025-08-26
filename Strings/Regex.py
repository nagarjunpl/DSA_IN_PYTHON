# Function to check if string
# starts and ends with 'gfg'

def gfg(S):
    b = S.lower()
  
    if (b[:3] == b[-3:]):
        print("Yes")
      
    else:
        print("No")
