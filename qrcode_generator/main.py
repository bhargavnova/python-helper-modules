import qrcode_generator
if __name__ == "__main__":

    data = input("Digite o link para criar o qrcode:")

    qrcode_generator.qrcode_conv(data)

