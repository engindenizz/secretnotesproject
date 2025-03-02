The project saved your notes # 📝 Secret Notes - Şifrelenmiş Not Defteri

**Secret Notes**, kullanıcıların notlarını güvenli bir şekilde şifreleyerek saklamasını ve gerektiğinde şifreyi çözerek görüntülemesini sağlayan bir Python uygulamasıdır. **AES tabanlı Fernet şifreleme yöntemi** kullanılarak, notların güvenliği sağlanır.

## 🚀 Özellikler
✅ **Güvenli Not Saklama** → Kullanıcı notlarını şifreleyerek saklayabilir.  
✅ **Şifre Çözme** → Kullanıcı doğru şifreleme anahtarı ve başlığı girerek notları çözebilir.  
✅ **Dosya İçinde Güvenli Saklama** → Notlar, `secret_notes.txt` içinde şifrelenmiş olarak saklanır.  
✅ **Kullanıcı Dostu Arayüz** → **CustomTkinter** ile modern bir UI sağlanır.  
✅ **EXE Olarak Çalıştırılabilir** → PyInstaller ile `.exe` dosyasına dönüştürülebilir.

---
🔒 Kullanılan Kriptografi Yöntemi
Bu proje, cryptography kütüphanesindeki Fernet şifreleme algoritmasını kullanır.
Fernet, AES-128 (Advanced Encryption Standard) ile CBC (Cipher Block Chaining) modunu kullanarak veriyi şifreler.

📌 Şifreleme Süreci
Kullanıcının Girdiği Master Key: Kullanıcı, notları şifrelemek için bir şifreleme anahtarı girer.
PBKDF2 Kullanımı (Key Derivation Function): Master key, PBKDF2 ile işlenerek 256-bit AES anahtarına dönüştürülür.
AES-128 CBC ile Şifreleme: Mesaj AES-128-CBC algoritması ile şifrelenir.
Base64 ile Kodlama: Şifreli veri, Base64 formatına çevrilerek okunabilir hale getirilir.
Dosyaya Kaydetme: Şifrelenmiş mesaj secret_notes.txt içinde saklanır.
🔓 Deşifreleme Süreci:

Kullanıcı, doğru master key ve başlığı girer.
Program, ilgili başlığa sahip şifreli veriyi dosyadan bulur.
AES-128 CBC kullanılarak veri çözülür.
Not, GUI'deki giriş alanına yazdırılır.
🔐 Güvenlik Önlemleri
Bu projede aşağıdaki güvenlik önlemleri alınmıştır:

✅ AES-128 Şifreleme (Fernet)
AES-128 CBC (Cipher Block Chaining) kullanılır.
Şifreleme için rastgele IV (Initialization Vector) eklenir.
Şifreleme ve çözme işlemleri cryptography kütüphanesi ile güvenli bir şekilde yapılır.
✅ PBKDF2 (Key Derivation Function) Kullanımı
Kullanıcının master key'i, PBKDF2 algoritması ile hashlenir ve bir kriptografik anahtar haline getirilir.
100.000 iterasyon kullanılarak brute-force saldırılarına karşı korunma sağlanır.
✅ Dosya Güvenliği
Şifrelenmemiş veri asla dosyada saklanmaz.
Dosyadaki başlıklar şifrelenmez, ancak notların kendisi AES-128 ile korunur.
Kullanıcı yanlış başlık veya anahtar girerse, doğru veriye ulaşamaz.
✅ GUI Üzerinde Güvenlik Önlemleri
Şifreli veri girildiğinde GUI giriş alanı temizlenir.
Kullanıcıdan gelen giriş verileri .strip() ile temizlenir (yanlış girişleri önlemek için).
Dosya yoksa hata verilir ve program çökmez.
