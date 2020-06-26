import json
result = []
with open ("text_77.json", "w", encoding="utf-8") as jay:
    with open("text_7.txt", encoding="utf-8") as jay_2:
        profit = {}
        for line in jay_2:
            profit[line.split(' ')[0]] = int(line.split(' ')[2]) - int(line.split(' ')[3])
        average_profit = sum([int(i) for i in profit.values() if int(i)>0]) / len([int(i) for i in profit.values() if int(i)>0])
        result.append(profit)
        result.append({"average_profit": round(average_profit)})
    json.dump(result, jay)

