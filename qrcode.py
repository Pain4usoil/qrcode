import qrcode

def generate_qr_code(data, file_name):
    # Создаем объект QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    # Добавляем данные для кодирования
    qr.add_data(data)
    qr.make(fit=True)

    # Создаем изображение QR-кода
    img = qr.make_image(fill_color="black", back_color="white")

    # Сохраняем изображение в файл
    img.save(file_name)

if __name__ == "__main__":
    # Вводим данные для кодирования
    data = input("Введите данные для кодирования в QR-код: ")
    # Вводим имя файла для сохранения QR-кода
    file_name = input("Введите имя файла для сохранения QR-кода (с расширением .png): ")

    # Генерируем QR-код
    generate_qr_code(data, file_name)
    print(f"QR-код успешно создан и сохранен в файле: {file_name}")
