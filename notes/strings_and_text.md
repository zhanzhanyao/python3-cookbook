#### Strings and Text
Split Strings   

    import re  
    re.split(r"[;,\s]\s*", line)  
Match Strings   

    filename.endswith(".txt")
    filename.startswith(".txt")

    from fnmatch import fnmatch, fnmatchcase

    fnmatch("foo.txt", "*.txt")
    fnmatchcase("foo.txt", "*.TXT")

    text.find("no")
    datepat.findall(text)
    datepat.finditer(text1)

    import re  
    re.Match(r"\d+/\d+/\d+", text1)
    datepat = re.compile(r"\d+/\d+/\d+")
    datepat.match(text1)

    re.findall(r"python", text, flags=re.IGNORECASE)

Replace Strings  

    text.replace("yeah", "yep") 
    import re
    re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)  

    datepat = re.compile(r"(\d+)/(\d+)/(\d+)")
    datepat.sub(r"\3-\1-\2", text)  # 'Today is 2012-11-27. PyCon starts 2013-3-13.'


Delete unwanted characters  

    s.strip() 
    s.lstrip() 
    s.rstrip()
    t.strip("-=")

    import re
    r = re.sub(r"\s+", " ", r) 
Combine strings  

    " ".join(parts)
    a + " " + b
    a = "xiao" "Gou"
    print(a, b, sep=":")
Insert varibles in string

    s = "{name} has {n} messages."
    s.format(name="xiaoming", n=7)

    a = Info("xiaoming", 7)
    s.format_map(vars(a))


