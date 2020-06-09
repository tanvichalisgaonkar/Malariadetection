import image_processing as ip
# import data_process as dt

if __name__ == "__main__":
    path = "H:\cell_images"
    file1 = "\Parasitized"
    file2 = "\\Uninfected"

    ip.image_preprocessing(path,file1)
    ip.image_preprocessing(path,file2) 

    # dt.data_processing()



