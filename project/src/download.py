import os
import urllib.request

def download_online_retail(save_dir="../data/raw"):

    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, "OnlineRetail.xlsx")

    if not os.path.exists(save_path):
        print(f"Downloading dataset from {url}...")
        urllib.request.urlretrieve(url, save_path)
        print(f" Dataset saved to {save_path}")
    else:
        print(f" File already exists at {save_path}")

    return save_path

if __name__ == "__main__":
    path = download_online_retail()
    print("Finished. Data available at:", path)
