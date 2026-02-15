from rembg import remove
input_path="images.jpeg" #eger farklı bir klasörde olsaydı onun adresini yazardık
output_path="output.png" #png verme sebebimiz doğru çalıssın diye

with open(input_path, "rb") as file: #rb read ve binary açılımıdır
    with open(output_path, "wb") as outfile: #wb ise write ve binary
        input_file=file.read()
        output=remove(input_file)
        outfile.write(output)
