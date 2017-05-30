import percentage.txt

more, less = 0, 0

ps = open('percents.txt').readlines()

ps

ratios = [float(x.split('=>')[-1].strip()) for x in ps]

ratios

more, less = 0, 0

for r in ratios:
    if r >= 0.9:
        more += 1
    else: 
        less += 1

more

less

