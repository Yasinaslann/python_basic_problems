# Problem 1
# Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.
# Multiply the 3 numbers you received from the user and print them on the screen. Try to print to the screen using the format method.

# Kullanıcıdan üç sayı alınır
num_1 =float(input("Birinci Sayıyı Giriniz (Enter First  Number )" ))
num_2 =float(input("İkinci  Sayıyı Giriniz (Enter Second Number )" ))
num_3 =float(input("Üçüncü  Sayıyı Giriniz (Enter Third  Number )" ))

# Sayıların çarpımını hesapla
multip_nums = num_1 * num_2 * num_3

# Sonucu format metodu ile ekrana yazdır
print("Sayıların Çarpımı: {}".format(multip_nums))

# Kullanıcıdan 3 tane sayı alıyorsunuz (num_1, num_2, num_3).| You receive 3 numbers from the user (num_1, num_2, num_3).
# Bu 3 sayıyı çarpıyorsunuz ve sonucu multip_nums değişkenine atıyorsunuz.| You multiply these 3 numbers and assign the result to the multipl_nums variable.
# Son olarak, format metodu ile sonucu ekrana yazdırıyorsunuz.| Finally, you print the result to the screen with the format method.

###################################################################################################################################################################

# Problem 2
# Kullanıcıdan bilgi boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulunur.
# Beden Kitle İndeksi : Kilo / Boy(m) * Boy(m)
# The body mass index of the user is found according to the user's information height and weight values.
# Body Mass Index: Weight / Height(m) * Height(m)

def Body_Mass_Index():
    # Kullanıcıdan kilo bilgisini alıyoruz (kg cinsinden)
    Weight = float(input("Kilo Değerinizi Giriniz (kg) (Enter Weight Value): "))

    # Kullanıcıdan boy bilgisini alıyoruz (metre cinsinden)
    Height = float(input("Boy Değerinizi Giriniz (m) (Enter Height Value): "))

    # Eğer boy sıfır girilmişse, hata mesajı veriyoruz
    if Height == 0:
        print("Boy Değeri Sıfır Olamaz (Height value cannot be zero).")
    else:
        # Beden Kitle İndeksi (BMI) hesaplanıyor. Formül: Kilo / Boy^2
        bmi = (Weight / (Height * Height))  # BMI formula (kg/m²)

        # BMI'yi iki ondalıklı sayıya yuvarlayarak ekrana yazdırıyoruz
        print("Beden Kitle İndeksiniz: {:.2f} kg/m²".format(bmi))  # # 2 ondalıklı formatla yazdırıyoruz | Rounded to 2 decimal places

# Programı çalıştırmak için fonksiyonu çağırıyoruz
Body_Mass_Index()

###################################################################################################################################################################


# Problem 3
# Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
# Get information about how much fuel a vehicle consumes per kilometer and how many kilometers it travels, and calculate how much the driver should pay in total.

def total_fuel_pay():
    # Kullanıcıdan kilometrede tüketilen yakıt miktarını (litre) alıyoruz
    fuel_per_km = float(input("Kilometrede araç ne kadar yakıyor? (Litre cinsinden, Enter How much fuel a vehicle consumes per kilometer in liters): "))

    # Kullanıcıdan toplam yolculuk mesafesini (kilometre) alıyoruz
    total_km = float(input("Kaç kilometre yol yaptığınızı giriniz (Enter the total distance traveled in kilometers): "))

    # Ödemenin hesaplanması: Kilometredeki yakıt tüketimi * toplam mesafe
    payment = fuel_per_km * total_km

    # Ödemeyi ekrana yazdırıyoruz
    print("Ödemeniz gereken toplam yakıt ücreti: {:.2f} TL".format(payment))  # Sonucu 2 ondalıklı olarak yazdırıyoruz

# Fonksiyonu çalıştırarak işlem başlatıyoruz
total_fuel_pay()


###################################################################################################################################################################


# Problem 4
# Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.
# Get the name, surname and number information from the user and print them on the screen, one under the other.

def print_underone():
    # Kullanıcıdan ad bilgisini alıyoruz
    name = input("Adınızı Giriniz (Enter your name)")

    # Kullanıcıdan soyad bilgisini alıyoruz
    surname = input ("Soyadınızı Giriniz (Enter your surname)")

    # Kullanıcıdan numara bilgisini alıyoruz (Telefon numarası gibi)
    info_num = input("Numara bilginizi giriniz (Enter your number)")

    # Kullanıcının bilgilerini alt alta yazdırıyoruz
    print("Adınız: {}\nSoyadınız: {}\nNumaranız: {}".format(name,surname,info_num))


# Fonksiyonu çağırarak işlem başlatıyoruz
print_underone()

###################################################################################################################################################################


# Problem 5
# Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.
# Ask the user for two numbers and replace the values ​​of these numbers with each other.

def change_value():
    # Kullanıcıdan iki sayı alıyoruz
    first_number = float(input("Birinci Sayıyı Giriniz (Enter first number)"))
    second_number = float(input("İkinci Sayıyı Giriniz (Enter second number)"))

    # Sayıları takas ediyoruz
    first_number,second_number = second_number,first_number

    # Sonuçları ekrana yazdırıyoruz
    print("Birinci Sayı: {}\nİkinci Sayı: {}".format(first_number,second_number))

# Fonksiyonu çağırıyoruz
change_value()






