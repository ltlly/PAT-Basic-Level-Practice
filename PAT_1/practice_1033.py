import re
error_key=input()
want=input()
if error_key=="":
    print(want)
else:
    out=re.sub(f"[f{error_key.upper()}]|[f{error_key.lower()}]","",want)
    if "+" in error_key:
        out=re.sub("[A-Z]","",out)
    print(out)
