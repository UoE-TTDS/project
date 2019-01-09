from src.utils import get_dataset
from src.configuration import Configuration

dataset = get_dataset(Configuration.from_file('config.cfg'))

i = 0
for key in dataset.keys():
    song = dataset[key]
    if song.lyrics is not None:
        i += 1
print(i)
