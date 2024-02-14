import csv

with open("game.txt",encoding="utf8") as file, open("game_new.csv","w",encoding="utf8") as f:
    reader = csv.DictReader(file,delimiter="$")
    writer =csv.writer(f)
    writer.writerow(["GameName", "characters", "nameError", "date"])
    for line in reader:
        gamen=line["GameName"]
        character=line["characters"]
        date = line["date"]
        eror=line["nameError"]
        if "55" in eror:
            print(f"у персонажа {character} в игре  {gamen} нашлась ошибка с кодом {eror}. Дата фиксации {date}")
            date="0000-00-00"
            eror="Done"
        else:
            eror = line["nameError"]
            date = line["date"]
        writer.writerow([line["GameName"],line["characters"],eror,date])