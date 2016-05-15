# Hita
Using Hitachi Content Platform like Amazon S3

Requirements:

Django==1.9.4
PyYAML==3.11
argparse==1.2.1
cffi==1.6.0
cryptography==1.3.2
django-rest-swagger==0.3.4
djangorestframework==3.3.3
enum34==1.1.5
idna==2.1
ipaddress==1.0.16
paypalrestsdk==1.11.5
pyOpenSSL==16.0.0
pyasn1==0.1.9
pycparser==2.14
pycurl==7.43.0
requests==2.9.1
six==1.10.0
wsgiref==0.1.2

To Setup:

 1. Hitachi Content Platform Must Be Ready
 2. Install requirements via "pip install -r requirements.txt"
 3. Login as root
 4. Run "python manage.py runserver"

Report Tasks:

 1. Abstract'ı ingilizceye çevir ve giriş gelişme sonuç yap
 2. Introduction'da abstract+birkaç paragraf kullan
 3. Amazon S3 , Openstack Swift , EMC's Atmos kısımlarını alıntıla
 4. Technical structre giriş paragrafı
 5. Defining a Pain and Product Development giriş paragrafı
 6. Project Analysis ve Workflowsa birşeyler karala
 7. Conclusion yaz
 8. Software developmenta birşeyler karala
 9. General Structre oturt
 10. To-Do List Yap

-------------------------------------------------------------------

Emergencies:

 1. Tenant Düzenleme
 2. Tenant Silme
 3. Namespace Düzenleme
 4. Namespace Silme
 6. Dosya Uploadda Update File
 7. Bir kullanıcı diğerinin dosyalarını göremesin
 8. Bir şekilde hesap aktifleştirmeyi yap

-------------------------------------------------------------------

 1. File görüntüleme
 2. User profile,Ödeme ve User Settings Page Design and DB Structre
 3. Modify tenant ve namespace de veri çek
 4. Namespace oluşturmadaki hataları gider
 5. Sistemi test et
 6. Buglistten devam et
 7. Future planning

-------------------------------------------------------------------

Tez kısmı:

 1. Sunum planlama
 2. Proje rapor kısmını kurallı taslağa oturtma (akademik)
 3. Hitachinin yazımı

-------------------------------------------------------------------

Pains:

 1. Security
 2. UI/UX
 3. Structre

-------------------------------------------------------------------

Bugs:

 1. Kredi kartı ve paypal ödeme hataları giderilecek
 2. Büyük boyutlu dosya indirmede gecikme var.
 3. Dosya ismi boşluklu ise upload etmiyor.
 4. Bir kullanıcı diğerinin dosyalarını görebiliyor.
 5. Create namespace ve tenant'ta eksik serializer alanları gider
 6. Forgot kısmı akışını tamamla
 7. Aktif olmayan hesap tenant/namespace açamasın test edilecek
 8. Register ve Forgot Maillerini Template Haline Getir
 9. Register Mailde Activation İstemeli

-------------------------------------------------------------------

Google Keep:

1. [URGENT] Namespaceleri listele
2. [URGENT] Tenantsız namespace
3. [URGENT] Namespace oluştur
5. [URGENT] Namespace altındaki dosyalar için CRUD
6. User tenant/namespace oluşturdukça ya da dosya ile ilgili işlem yapmaya kalktıkça HCP'ye request at ve gelecek yanıta göre dbde işlem yap
7. Yeni register olan kullanıcının hesabını pasif tut. Paypaldan 1$ çekince aktifleştir.