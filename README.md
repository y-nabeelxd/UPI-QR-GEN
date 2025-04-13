# UPI-QR-GEN

**by [y-nabeelxd](https://github.com/y-nabeelxd)**

## Why this?

Sometimes you just want to generate a simple UPI QR code — fast, offline, and without sharing your UPI ID to any random site or app. Whether you're a developer, freelancer, shop owner, or just someone who loves terminal tools, this tool helps you generate a UPI QR code within seconds.

## What this will help you with?

- Generate UPI QR codes on the fly.
- No internet connection or browser needed.
- Fully offline and privacy-friendly.
- Choose to **print** in terminal or **save** as a PNG file.
- Super useful for developers, creators, and small business owners.

## What is this?

This is a Python script that takes your UPI details and generates a clean, scannable UPI QR code. You can either display it directly in the terminal (for demo or CLI fans) or save it as a PNG file to share or print.

---

## Run the code

**Step 1: Clone the repository**
```
git clone https://github.com/y-nabeelxd/UPI-QR-GEN.git
cd UPI-QR-GEN
```

**Step 2: Install requirements**
```
pip install qrcode[pil]
```

**Step 3: Run the script**
```
python qr.py
```

It will ask you for:
- Name
- UPI ID
- Remarks (optional)
- Amount (optional)

Then lets you choose:
- Print QR in terminal
- Save as PNG image

---

**License:** MIT

---
Made with pure Python.
