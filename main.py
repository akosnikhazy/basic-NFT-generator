# Nikházy Ákos 2022

# WHAT IS THIS?
# Simple NFT maker, so you see how easy it is to make NFT collections.
# With this you can make NFTs randomly from layers. You just have
# to put the layers in the NFTparts "layerX" folders. 0 is the background.
# The layer images have to be the same size for simplicity sake. For
# example, if you have a 630x630 background, than you have to make a
# 630x630 character too, as a transparent PNG, so you can put it on it.

# HOW?
# this is a fully dynamic one. You just have to tell the script how many
# layers you have. From there it counts the parts in every layer, tells
# you how many possible images you can generate and let you generate
# as many or less. Only rule is your have to name the parts by number
# starting from 0, without gaps.

# EXAMPLE?
# In the example folders inside the NFTparts folder you find
# 6 backgrounds, 6 bodies, 5 body clothing, 4 eyes, 2 mouths and
# 6 hats. That is 8640 combinations. I spent about 15 minutes with them.
# you can call it Crappy Ape Toilet Club.

# The point is: with minimal time you can do 10000s of pieces of unique apes.

# WHY?
# I seen this video: https://www.youtube.com/watch?v=je5jSl3Fixc
# so I decided to make my own from scratch. But as I rarely use python
# this code is what it is. A good practice to code while shitting on NFTs.

# PLEASE
# Please do not mint NFTs really. You can just upload your PNGs to deviantart
# or some other site and sell them there for real money. Without the unnecessary
# blockchain element.

# Seriously: you can even watermark them and sell the watermarkless download on your
# own website. Or whatever. If people really need this shit they would buy it normally
# without the hype.

import random
from PIL import Image
import os, os.path


class NFT:
    alreadyGenerated = []

    def __init__(self, layers=6, folder="NFTs"):

        self.layers = layers  # if you need more layers make more layer folders in the NFTparts folder
        self.folder = folder
        self.max = 0
        print(
            "WELCOME to this crappy NFT art generator! Please do not make NFTs. They are stupid. This software took me 1 hour to make... with the example images")
        print(
            "Generating random images is as old as programming. It has nothing artistic in it. The results are cheap and lazy. Like this Python script.")
        print("------------------------------------------------------")

    def calculateMaxImages(self):
        for x in range(self.layers):
            DIR = "NFTparts/layer" + str(x)
            if self.max == 0:
                self.max = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
            else:
                self.max = self.max * len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

        print("You have " + str(self.max) + " possible \"art\" pieces")
        print("------------------------------------------------------")
        return self.max

    def getLayerCounts(self):
        layers = []
        for x in range(self.layers):
            DIR = "NFTparts/layer" + str(x)

            layers.append(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

        return layers

    def generateNFT(self, NFTnum=0):
        limit = self.calculateMaxImages()

        if NFTnum < 1:
            howMany = input("How many random NFTs you want to generate (type a number equal or less than the limit)?\n")

            if int(howMany) > limit:
                print("------------------------------------------------------")
                print(
                    "You have not got enough parts to generate " + str(howMany) + " images. You limit is " + str(limit))
                print("done")
                return
        else:
            howMany = NFTnum

        print("------------------------------------------------------")
        x = 0
        layers = self.getLayerCounts()

        # a lazy loop, also slow and it gets slower as it depends on randomly generated images without
        # repeation. For this I check if one was already generated. The more images there is the more it
        # will stand in place to waste your precious time generating NFTs. I could have made it so
        # I generate them in an intelligent way going through the image combinations. But I decided to
        # make this as stupid as possible. Feel free to make it good.
        while x < int(howMany):
            toCreate = []
            imageLayers = []
            createdString = ""
            for y in range(self.layers):
                toCreate.append(random.randint(0, layers[y] - 1))

            for y in range(len(toCreate)):
                createdString = createdString + str(toCreate[y])
                imageLayers.append(Image.open("NFTparts/layer" + str(y) + "/" + str(toCreate[y]) + ".png").convert("RGBA"))

            for y in range(len(imageLayers)):
                imageLayers[0].paste(imageLayers[y], (0, 0), imageLayers[y])

            if createdString in self.alreadyGenerated:
                continue

            self.alreadyGenerated.append(createdString)
            imageLayers[0].save(self.folder + "/" + createdString + ".png")
            x = x + 1
            print(str(round(x / (int(howMany) / 100), 2)) + "%")

        print("------------------------------------------------------")
        print("done")


# here you set up your NFT generation
# you can set up more layers and other output folder like yourNFT = NFT(10,"myFolder")
yourNFT = NFT()

# start. Also you can do it like this yourNFT.generateNFT(10) so it doesn't ask how many but generates 10
yourNFT.generateNFT() 
