# Goopall Cookies
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

1. ****
   Karakter utama yang dapat dikendalikan oleh pemain.

   ![](https://github.com/Cookies/Tugas-Besar-PBO/assets/167991243/bd7c011a-7515-4642-9a8b-bb325a94d776)


3. **Prob**
   Jenis musuh yang paling dasar. Menyerang  dengan terbang langsung ke arahnya.

   
   ![prob](https://github.com/Cookies/Tugas-Besar-PBO/assets/167991243/5c5a659b-cf10-46ab-8b2e-94570f8ef742)


5. **MultiMonster**
   Musuh. Terbang langsung ke arah . Lebih lambat daripada Prob.

   
   ![MultiMonster](https://github.com/Cookies/Tugas-Besar-PBO/assets/167991243/1705cc8d-175e-4f92-904f-69773dea5f02)


7. **Koko Jumbo**
   Jenis musuh lainnya. Menembakkan laser merah ke arah .

   
![koko](https://github.com/Cookies/Tugas-Besar-PBO/assets/167991243/9c8529d8-e6c6-4f02-9c5f-407b515030c6)

   
8. **Adudu**
   Jenis musuh yang paling sulit. Memiliki health terbanyak. Terbang menuju  tetapi sangat lambat. Ketika mati, dia berubah menjadi banyak slime hijau.
   
![adudu](https://github.com/Cookies/Tugas-Besar-PBO/assets/167991243/2cb43173-8929-408a-a8ca-533d83241854)


## Mekanisme
### Pemain mengontrol 
Pemain menggerakan kursor maka karakter  akan bergerak sesuai arah kursor.

###  menembak Cookie
Ketika pemain menekan tombol **space**, Gopal akan menembakkan cookies ke arah musuh.

![WhatsApp Image 2024-05-21 at 08 48 49_cb7a9fd9](https://github.com/GopalCookies/Tugas-Besar-PBO/assets/167991243/71333dd1-2f3a-4d2f-9a36-c0f1ca31b50e)


### Cookie mengenai musuh
Ketika objek Cookies bertabrakan dengan objek Enemy, musuh akan terhapuskan dan pemain akan mendapatkan skor. 

**KHUSUS UNTUK BOSS ENEMY**:
- Ketika cookies mengenai Adudu, Adudu akan berubah menjadi slime.
- Jika slime mengenai pemain, skor akan berkurang.

![WhatsApp Image 2024-05-21 at 08 58 19_1dc3c016](https://github.com/GopalCookies/Tugas-Besar-PBO/assets/167991243/74764a06-6633-4445-9fba-a4ea0daee799)


### Musuh bergerak dan menembak
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
