text="Python is programming language .python"
pattern="[Pp]ython"
match=re.findall(pattern,text)
if match:
    print(match)