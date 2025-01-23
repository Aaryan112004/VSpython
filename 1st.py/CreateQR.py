import qrcode
import qrcode.constants

def ABC_qr(link, file_name):                                   #......ABC_qr is function
    
    qr = qrcode.QRCode(
        version=1,                                             # size  QR
        error_correction=qrcode.constants.ERROR_CORRECT_H ,    # Ooooptional...its for run program smoothly
        box_size=15,                                           # box ni size in QR
        border=1                                               # border ni Thickness
    )
    
    qr.add_data(link)
    qr.make(fit=True)                                          #Ooooptional chhe fit. just data(version,...) ne perfect banave

    img = qr.make_image(fill_color="white", back_color="black")# Create QR code image

    img.save(file_name)                                        # Save image
    print(f"QR code saved as {file_name}")

print(ABC_qr("https://www.youtube.com/", "youtube123_qr.png"))