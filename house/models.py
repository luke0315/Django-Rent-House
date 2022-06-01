from django.db import models

# Create your models here.


class City(models.TextChoices):
    
    Keelung='KLU','基隆市'
    NewTaipei='TPH','新北市'
    Taipei='TPE','臺北市'
    Taoyuan='TYC','桃園市'
    HsinchuCounty='HSH','新竹縣'
    Hsinchu='HSC','新竹市'
    Miaoli='MAC','苗栗市'
    MiaoliCounty='MAL','苗栗縣'
    Taichung='TXG','臺中市'
    ChanghuaCounty='CWH','彰化縣'
    Changhua='CWS','彰化市'
    Nantou='NTC','南投市'
    NantouCounty='NTO','南投縣'
    Yunlin='YLH','雲林縣'
    ChiayiCounty='CHY','嘉義縣'
    Chiayi='CYI','嘉義市'
    Tainan='TNN','臺南市'
    Kaohsiung='KHH','高雄市'
    PingtungCounty='IUH','屏東縣'
    Pingtung='PTS','屏東市'
    YilanCounty='ILN','宜蘭縣'
    Yilan='ILC','宜蘭市'
    HualienCounty='HWA','花蓮縣'
    Hualien='HWC','花蓮市'
    Taitung='TTC','臺東市'
    TaitungCounty='TTT','臺東縣'
    Penghu='PEH','澎湖縣'
    Green='GNI','綠島'
    Orchid='KYD','蘭嶼'
    Kinmen='KMN','金門縣'
    Matsu='MZW','馬祖'
    Lienchiang='LNN','連江縣'



class room(models.TextChoices):
    B1 = '1', '1室1廳'
    B2 = '2', '2室1廳'
    B3 = '3', '3室1廳'
    B4 = '4', '4室2廳'


class Area(models.TextChoices):
    A1 = '1', '<50坪'
    A2 = '2', '50-70坪'
    A3 = '3', '70-90坪'
    A4 = '4', '90-140坪'
    A5 = '5', '>140坪'


class Floor(models.TextChoices):
    LOW = 'l', '低樓層'
    MIDDLE = 'm', '中樓層'
    HIGH = 'h', '高樓層'


class Direction(models.TextChoices):
    EAST = 'e', '東'
    SOUTH = 's', '南'
    WEST = 'w', '西'
    NORTH = 'n', '北'


class Community(models.Model):
    name = models.CharField(max_length=60, verbose_name='縣市')
    city = models.CharField(max_length=5, choices=City.choices, verbose_name="城市")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="发布日期")
    mod_date = models.DateTimeField(auto_now=True, verbose_name="修改日期")

    class Meta:
        verbose_name = "縣市"
        verbose_name_plural = "縣市"

    def __str__(self):
        return self.name


class House(models.Model):
    description = models.CharField(max_length=108, verbose_name="描述")
    #city=models.CharField(max_length=10, choices=City.choices,null=True, verbose_name="城市")
    community = models.ForeignKey('Community', on_delete=models.CASCADE, verbose_name="縣市")
    address = models.CharField(max_length=30, verbose_name="地址") 
    phone = models.CharField(max_length=30 ,verbose_name="電話") 
    bedroom = models.CharField(max_length=1, choices=room.choices, verbose_name="房型")
    direction = models.CharField(max_length=2, choices=Direction.choices, verbose_name="朝向")
    floor = models.CharField(max_length=1, choices=Floor.choices, verbose_name="樓層")
    area = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="面積(平方米)")
    area_class = models.CharField(max_length=1, null=True, blank=True, choices=Area.choices, verbose_name="面積")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="月租")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="發布日期")
    mod_date = models.DateTimeField(auto_now=True, verbose_name="修改日期")

    class Meta:
        verbose_name = "房子"
        verbose_name_plural = "房子"

    def __str__(self):
        return '{}.{}'.format(self.description, self.address)

    def save(self, *args, **kwargs):
        if self.area < 50:
            self.area_class = Area.A1
        elif 50 <= self.area < 70:
            self.area_class = Area.A2
        elif 70 <= self.area < 90:
            self.area_class = Area.A3
        elif 90 <= self.area < 140:
            self.area_class = Area.A4
        else:
            self.area_class = Area.A5

        super().save(*args, **kwargs)





