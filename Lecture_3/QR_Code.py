import qrcode
import os

folder_name = "my QR code"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

data = ("AP ko pata ha ya jo Hannan ha na is ka real name kasi ko ni pata is ka real name pata ha kay.\n"
        "Ma bata the ho is ka real name (Anik Wala Jin 👻👻) or ya name is na kasi ko ni bata ya.\n"
        "🥸🥸🥸🥸🥸🥸🥸ma na be tab suna tha jb is ka ghr wala is ko jin jin bola raha tha.\n"
        "or ha ya raz ki bat ha kasi ko na bata na ko.")

qr = qrcode.make(data)
file_path = os.path.join(folder_name, "husnena_qr.png")
qr.save(file_path)

print(f"✅ QR Code ban gaya aur save hua: {file_path}")