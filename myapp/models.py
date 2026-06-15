from django.db import models

# Create your models here.
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100, verbose_name="Oda Adı")
    description = models.CharField(max_length=200, blank=True, verbose_name="Açıklama")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Fiyat (₺)")
    image = models.ImageField(upload_to='rooms/', verbose_name="Resim")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Oda"
        verbose_name_plural = "Odalar"

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/', verbose_name="Resim")
    caption = models.CharField(max_length=100, blank=True, verbose_name="Açıklama")

    def __str__(self):
        return self.caption or f"Galeri Resmi {self.id}"

    class Meta:
        verbose_name = "Galeri Resmi"
        verbose_name_plural = "Galeri Resimleri"

class Announcement(models.Model):
    title = models.CharField(max_length=200, verbose_name="Başlık")
    description = models.TextField(verbose_name="Açıklama")
    image = models.ImageField(upload_to='announcements/', verbose_name="Resim")
    date = models.DateField(auto_now_add=True, verbose_name="Tarih")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Duyuru"
        verbose_name_plural = "Duyurular"
        ordering = ['-date']

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('mains', 'Ana Yemek'),
        ('desserts', 'Tatlı'),
        ('drinks', 'İçecek'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="Kategori")
    name = models.CharField(max_length=100, verbose_name="Ürün Adı")
    description = models.TextField(verbose_name="Açıklama")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Fiyat (₺)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Menü Öğesi"
        verbose_name_plural = "Menü Öğeleri"

class HistoryEvent(models.Model):
    ICON_CHOICES = [
    ('ion-ios-star', 'Yıldız'),
    ('ion-ios-home', 'Ev'),
    ('ion-ios-location', 'Konum'),
    ('ion-ios-telephone', 'Telefon'),
    ('ion-ios-email', 'Email'),
    ('ion-ios-calendar', 'Takvim'),
    ('ion-ios-people', 'Kadro'),
    ('ion-ios-checkmark-circle', 'Onay'),
    ]

    year = models.CharField(max_length=20, verbose_name="Yıl")
    title = models.CharField(max_length=200, verbose_name="Başlık")
    description = models.TextField(verbose_name="Açıklama")
    icon = models.CharField(max_length=50, choices=ICON_CHOICES, default='ion-ios-star', verbose_name="İkon")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıra")

    def __str__(self):
        return f"{self.year} - {self.title}"

    class Meta:
        verbose_name = "Tarihçe Olayı"
        verbose_name_plural = "Tarihçe"
        ordering = ['order']
        
class RoomImage(models.Model):
    room = models.ForeignKey(Room, related_name='extra_images', on_delete=models.CASCADE, verbose_name="Oda")
    image = models.ImageField(upload_to='rooms/extra/', verbose_name="Resim")

    def __str__(self):
        return f"{self.room.name} - Resim {self.id}"

    class Meta:
        verbose_name = "Oda Resmi"
        verbose_name_plural = "Oda Resimleri",
        
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ad Soyad")
    phone = models.CharField(max_length=20, verbose_name="Telefon")
    email = models.EmailField(blank=True, verbose_name="E-posta")
    message = models.TextField(verbose_name="Mesaj")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Tarih")
    is_read = models.BooleanField(default=False, verbose_name="Okundu")

    def __str__(self):
        return f"{self.name} - {self.phone}"

    class Meta:
        verbose_name = "İletişim Mesajı"
        verbose_name_plural = "İletişim Mesajları"
        ordering = ['-created_at']
    
class HomePageContent(models.Model):
    hero_image = models.ImageField(upload_to='homepage/', verbose_name="Hero Arka Plan Resmi")
    hero_caption = models.CharField(max_length=100, default="YALVAÇ ÖĞRETMENEVİ", verbose_name="Üst Yazı")
    hero_title = models.CharField(max_length=200, default="Konforlu ve Güvenilir Konaklama", verbose_name="Başlık")

    welcome_image_1 = models.ImageField(upload_to='homepage/', verbose_name="Hoş Geldiniz Resmi 1 (büyük)")
    welcome_image_2 = models.ImageField(upload_to='homepage/', verbose_name="Hoş Geldiniz Resmi 2 (üstte)")
    welcome_title = models.CharField(max_length=200, default="Yalvaç Öğretmenevi'ne Hoş Geldiniz", verbose_name="Başlık")
    welcome_text = models.TextField(verbose_name="Açıklama Yazısı")

    def __str__(self):
        return "Anasayfa İçeriği"

    class Meta:
        verbose_name = "Anasayfa İçeriği"
        verbose_name_plural = "Anasayfa İçeriği"