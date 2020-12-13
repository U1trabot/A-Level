import re
string = ["gold saucer",
"chocobo ranch",
"mideel",
"gongaga village",
"corel prison",
"great glacier",
"costa del sol",
"mount nibel",
"cactuar island",
"city of the ancients",
"fort condor",
"nibelheim",
"cosmo canyon",
"ancient forest",
"wutai",
"kalm",
"rocket town",
"bone village"]
for line in string:
    if re.fullmatch('^[quit watching]*$', line) is not None:
        print(line)