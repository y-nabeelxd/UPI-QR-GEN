import qrcode
import os
import platform

def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

name = input("Enter your name: ")
upi_id = input("Enter your UPI ID: ")
remarks = input("Enter remarks (optional): ")
amount = input("Enter amount (optional): ")

upi_url = f"upi://pay?pa={upi_id}&pn={name}"
if amount:
    upi_url += f"&am={amount}"
if remarks:
    upi_url += f"&tn={remarks}"

clear_screen()

print("QR CODE Type:\n1. Print in Screen\n2. Save as Photo (png)")
choice = input("Enter your choice (1 or 2): ")

qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(upi_url)
qr.make(fit=True)

if choice == "1":
    qr.print_ascii()
elif choice == "2":
    img = qr.make_image(fill_color="black", back_color="white")
    filename = f"{name.replace(' ', '_')}_upi_qr.png"
    img.save(filename)
    print(f"QR Code saved as {filename}")
else:
    print("Invalid choice.")
