import imageio
import os
images = []
names = []

path = os.path.dirname(os.path.abspath(__file__))
for i in range(1, 360):
    name = path + '\pngs\drawing_{}.png'.format(i)
    print("Leggo drawings_{}.png".format(i))
    images.append(imageio.imread(name))

print("Creo gif...")
imageio.mimsave('fract_movie.gif', images)
print("Fatto.")