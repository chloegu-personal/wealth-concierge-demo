import qrcode

def generate_qr(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="navy", back_color="white")
    img.save(filename)
    print(f"QR Code generated: {filename}")

if __name__ == "__main__":
    repo_url = "https://github.com/chloegu-personal/wealth-concierge-demo"
    generate_qr(repo_url, "github_repo_qr.png")
