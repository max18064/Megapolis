import csv
def hash(s):
    p=65
    alp = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789:-"
    d={l:i for i,l in enumerate(alp,1)}
    p=65
    m=10**9+9
    hash=0
    for i in range(0,len(s)):
        hash=hash+(d[s[i]]*p**i)%m
    return str(hash)



with open("game.txt",encoding="utf8") as file, open("game_new.csv6","w",encoding="utf8") as f:
    reader = csv.DictReader(file,delimiter="$")
    d=[]
    writer =csv.writer(f)
    writer.writerow(["Hash","GameName", "characters", "nameError", "date"])
    for line in reader:
        name=line["GameName"]
        name=name.replace(" ","")
        name = name.replace(".", "")
        name = name.replace("'", "")
        character=line["characters"]
        a=name+character
        a=hash(a)
        print(a)
        writer.writerow([a,line["GameName"],line["characters"],line["nameError"],line["date"]])