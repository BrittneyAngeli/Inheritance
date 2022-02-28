import a_PlantClass as pc

primrose = pc.Plant("Green")

sunflower = pc.Flower("Yellow", 12)         # This will produce an error if you put just "Yellow"

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())


#print(primrose.get_petals())
#This print won't work, because plant wouldn't be able to access the flower attributes
