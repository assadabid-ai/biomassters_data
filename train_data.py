import os
import requests
import zipfile

# Define the list of URLs for the train features and AGBM data
urls = [
    "https://huggingface.co/datasets/nascetti-a/BioMassters/resolve/main/train_features.z01?download=true",
    "https://huggingface.co/datasets/nascetti-a/BioMassters/resolve/main/train_features.z02?download=true",
    "https://huggingface.co/datasets/nascetti-a/BioMassters/resolve/main/train_features.z03?download=true",
    "https://huggingface.co/datasets/nascetti-a/BioMassters/resolve/main/train_features.z04?download=true",
    "https://huggingface.co/datasets/nascetti-a/BioMassters/resolve/main/train_features.z05?download=true",
    "https://huggingface.co/datasets/nascetti-a/BioMassters/resolve/main/train_features.z06?download=true",
    "https://huggingface.co/datasets/nascetti-a/BioMassters/resolve/main/train_features.z07?download=true",
    "https://huggingface.co/datasets/nascetti-a/BioMassters/resolve/main/train_features.z08?download=true",
    "https://huggingface.co/datasets/nascetti-a/BioMassters/resolve/main/train_features.z09?download=true",
    "https://huggingface.co/datasets/nascetti-a/BioMassters/resolve/main/train_features.z10?download=true",
    "https://huggingface.co/datasets/nascetti-a/BioMassters/resolve/main/train_features.z11?download=true",
    "https://huggingface.co/datasets/nascetti-a/BioMassters/resolve/main/train_features.z12?download=true",
    "https://huggingface.co/datasets/nascetti-a/BioMassters/resolve/main/train_features.z13?download=true",
    "https://huggingface.co/datasets/nascetti-a/BioMassters/resolve/main/train_features.zip?download=true",
    "https://huggingface.co/datasets/nascetti-a/BioMassters/resolve/main/train_agbm.zip?download=true"
]

# Function to download a file from the URL
def download_file(url, save_path):
    print(f"Downloading {url}...")
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {url} to {save_path}")

# Download all the parts of the zip files
# Use the current working directory to save the files
downloaded_files = []  # To keep track of downloaded files
for url in urls:
    filename = url.split("/")[-1].split("?")[0]  # Extract filename from URL
    file_path = filename  # Save to the current working directory
    download_file(url, file_path)
    downloaded_files.append(file_path)  # Store the path for later deletion

# Function to unzip a zip file
def unzip_file(zip_file_path, extract_to_dir):
    print(f"Unzipping {zip_file_path}...")
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_dir)
    print(f"Unzipped {zip_file_path} to {extract_to_dir}")

# Unzip train_features.zip and train_agbm.zip (assuming they are in the current working directory)
train_features_zip_path = "train_features.zip"
train_agbm_zip_path = "train_agbm.zip"

# Check if the files exist and unzip
if os.path.exists(train_features_zip_path):
    unzip_file(train_features_zip_path, "train_features")

if os.path.exists(train_agbm_zip_path):
    unzip_file(train_agbm_zip_path, "train_agbm")

# Delete the downloaded files after unzipping
for file in downloaded_files:
    if os.path.exists(file):
        os.remove(file)
        print(f"Deleted {file}")
