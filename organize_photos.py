import os


def extract_place(filename):
    parts = filename.split("_")
    place_name = parts[1]
    return place_name


def make_place_diretories(places):
    for place in places:
        os.mkdir(place)


def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = []
    for filename in originals:
        place = extract_place(filename)
        if place not in places:
            places.append(place)

    make_place_diretories(places)

    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))


#organize_photos("Photos")
print("TEST")
