import cv2
import os

ds_dirname = "dataset"
COUNT = 3317
theshold = 100

def convert_to_canny_lines():
    for i in range(1, COUNT+1):
        fin_fn = str(f"{ds_dirname}/in/{i}.jpg")
        fout_fn = str(f"{ds_dirname}/out/{i}.txt")

        if not os.path.isfile(fin_fn):
            print('File not found')
            continue

        image = cv2.imread(fin_fn)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        th = theshold  # theshold
        image = cv2.Canny(image, th, th)
        cv2.imwrite(f"{ds_dirname}/in/{i}.jpg", image)
        print(f"Image {i} is converted")
DS_INDEX = 0
convert_to_canny_lines()
for i in range(1, COUNT+1):
    f = True
    fin_fn = str(f"{ds_dirname}/in/{i}.jpg")
    fout_fn = str(f"{ds_dirname}/out/{i}.txt")
    if not os.path.isfile(fin_fn):
        f = False
        if os.path.isfile(fout_fn):
            os.remove(fout_fn)
            print(f'{i} IS REMOVED!')

    if not os.path.isfile(fout_fn):
        f = False
        if os.path.isfile(fin_fn):
            os.remove(fin_fn)
            print(f'{i} IS REMOVED!')

    if f:
        os.rename(fin_fn, f"{ds_dirname}/in/{DS_INDEX}.jpg")
        os.rename(fout_fn, f"{ds_dirname}/out/{DS_INDEX}.txt")
        DS_INDEX += 1
