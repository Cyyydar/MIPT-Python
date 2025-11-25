from encoder import NpyHistogram, TxtHistogram

def save_histogram(strategy, img, path):
    strategy.save(img, path)

def load_histogram(strategy, path):
    return strategy.load(path)
