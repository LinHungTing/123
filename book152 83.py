mixed = ["Broccoli V" , "Lily F" , "Cucumber V" , "Rose F" , "LotusF"\
     , "Cabbage V" , "Onion V" , "Anemone F" , "Aster F"]
Vegetables = []
Flowers = []
for i in mixed:
    if i[-1] == "V":
        Vegetables.append(i[:-2])
    else:
        Flowers.append(i[:-2])
print("Vegetables:" , ", ".join(Vegetables))
print("Flowers:" , ", ".join(Flowers))