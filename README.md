w# Goopall Cookies
![title](https://github.com/GopalCookies/Tugas-Besar-PBO/assets/167991243/e8e6b57d-b6e9-4bb1-bbaf-6992eaee6b17)


## Description
**Goopall-Cookies** adalah game menembak monster yang terinspirasi dari kartun **Boboiboy**. Pemain akan berperan sebagai Gopal, pahlawan super dengan kekuatan super untuk mengubah benda menjadi makanan. Tugas pemain adalah menembakkan cookies pada monster bernama Koko Jumbo, Multi Monster, Prob, dan Adudu.

## Libraries
- **Pygame**
- **Moderngl**
- **NumPy**
- **Pillow**

## Installation
1. Download file di GitHub sebagai zip.
2. Ekstrak zip lalu jalankan:
    ```bash
    pip install -r requirements.txt
    ```
3. Lalu jalankan:
    ```bash
    python main.py
    ```

## Karakter

### **Gopal**
   Karakter utama yang dapat dikontrol oleh pemain. Bisa menembakkan cookies ke arah musuh.
   
   ![gopal](https://github.com/GopalCookies/Tugas-Besar-PBO/assets/167991243/3e033bff-ed59-4284-8e87-82edda0269bb)

### **Prob**
   Tipe musuh paling dasar. Menyerang gopal dengan terbang langsung ke arahnya.
   
   ![prob](https://github.com/GopalCookies/Tugas-Besar-PBO/assets/167991243/72d8f8df-2ed5-46d7-a9c4-81da64eaf39e)

### **MultiMonster**
   Tipe musuh selanjutnya. Terbang langsung ke gopal namun Lebih lambat dari prob.
   
   ![MultiMonster](https://github.com/GopalCookies/Tugas-Besar-PBO/assets/167991243/5a30e645-a810-4a77-8b3e-d020608fe929)

### **Koko Jumbo**
   Tipe musuh selanjutnya. Koko jumbo bisa menembakkan laser merah ke arah gopal.
   
   ![koko](https://github.com/GopalCookies/Tugas-Besar-PBO/assets/167991243/ad9461cb-93d3-47c4-8079-430fadfed1c3)

### **Adudu**
   Tipe musuh yang paling sulit. Memiliki health terbanyak. Terbang menuju Gopal tetapi sangat lambat. Saat health nya habis, dia hancur menjadi slime hijau.
   
   ![adudu](https://github.com/GopalCookies/Tugas-Besar-PBO/assets/167991243/4d52275e-e954-43d4-96c2-c388903ef4e7)


## Mekanisme
### Kontrol Pemain 
Ketika pemain menekan tombol kontrol kursor di keyboard, maka karakter Gopal akan bergerak sesuai arah kursor.

###  Menembak Cookies
Ketika pemain menekan tombol **space** atau **klik kiri** di mouse, Gopal akan menembakkan cookies. Arah cookies yang ditembakkan bisa diatur dengan cara menggerakkan **kursor** dengan mouse atau trackpad.

![WhatsApp Image 2024-05-21 at 08 48 49_cb7a9fd9](https://github.com/GopalCookies/Tugas-Besar-PBO/assets/167991243/71333dd1-2f3a-4d2f-9a36-c0f1ca31b50e)


### Cookie mengenai musuh
Ketika objek Cookies bertabrakan dengan objek Enemy, musuh akan hilang dan pemain akan mendapatkan skor. 

**KHUSUS UNTUK BOSS ENEMY**:
- Ketika cookies mengenai Adudu, Adudu akan berubah menjadi slime.
- Jika slime mengenai pemain, skor akan berkurang.

![WhatsApp Image 2024-05-21 at 08 58 19_1dc3c016](https://github.com/GopalCookies/Tugas-Besar-PBO/assets/167991243/74764a06-6633-4445-9fba-a4ea0daee799)


### Musuh bergerak
Musuh akan terus datang dan bergerak secara **RANDOM**. 

**UNTUK ENEMY KOKO JUMBO**:
- Ia bisa menembakkan laser yang bisa mengurangi skor pemain.

### Laser mengenai pemain
Ketika objek Laser bertabrakan dengan objek Gopal, pemain akan kehilangan **HEALTH**. Game akan berakhir jika **HEALTH** mencapai 0.

![WhatsApp Image 2024-05-21 at 08 49 12_39c01b6e](https://github.com/GopalCookies/Tugas-Besar-PBO/assets/167991243/266f99e1-c318-4fec-b035-9ceae21f29d1)


## UML Diagram
![WhatsApp Image 2024-05-21 at 08 53 58_24b3fca9](https://github.com/GopalCookies/Tugas-Besar-PBO/assets/167991243/5e185e23-4ef1-4aaa-822f-bdbad5024326)

## Demo Game Goopall Cookies!
https://youtu.be/u0X7fLTj-r4 

## Credits
| Nama | NIM | Kontribusi |
|---|---|---|
| Bulan Nindya Sapta Saputri | 120140231 | - |
| Cindy Nadila Putri | 122140002 | Programmer |
| Muhammad Rafif Vivaldi | 122140026 | Programmer |
| Amanda Istiazah | 122140081 | Aset dan Dokumentasi |
| Giulia Puspo Negoro | 122140084 | Aset dan Dokumentasi |
| Hijrah Fahrezi H.L.T | 122140175 | Programmer |
