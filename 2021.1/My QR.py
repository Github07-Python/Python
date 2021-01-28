from MyQR import myqr
import os
version, level, qr_name = myqr.run(
    words="Marvel",
    version=1,
    level='H',
    picture="3.gif",
    colorized=True,
    contrast=1.0,
    brightness=1.0,
    save_name="3.gif",
    save_dir=os.getcwd()
)