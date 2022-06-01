# Generated by Django 3.2 on 2022-05-31 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='縣市')),
                ('city', models.CharField(choices=[('KLU', '基隆市'), ('TPH', '新北市'), ('TPE', '臺北市'), ('TYC', '桃園市'), ('HSH', '新竹縣'), ('HSC', '新竹市'), ('MAC', '苗栗市'), ('MAL', '苗栗縣'), ('TXG', '臺中市'), ('CWH', '彰化縣'), ('CWS', '彰化市'), ('NTC', '南投市'), ('NTO', '南投縣'), ('YLH', '雲林縣'), ('CHY', '嘉義縣'), ('CYI', '嘉義市'), ('TNN', '臺南市'), ('KHH', '高雄市'), ('IUH', '屏東縣'), ('PTS', '屏東市'), ('ILN', '宜蘭縣'), ('ILC', '宜蘭市'), ('HWA', '花蓮縣'), ('HWC', '花蓮市'), ('TTC', '臺東市'), ('TTT', '臺東縣'), ('PEH', '澎湖縣'), ('GNI', '綠島'), ('KYD', '蘭嶼'), ('KMN', '金門縣'), ('MZW', '馬祖'), ('LNN', '連江縣')], max_length=5, verbose_name='城市')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
            ],
            options={
                'verbose_name': '縣市',
                'verbose_name_plural': '縣市',
            },
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=108, verbose_name='描述')),
                ('address', models.CharField(max_length=30, verbose_name='地址')),
                ('phone', models.CharField(max_length=30, verbose_name='電話')),
                ('bedroom', models.CharField(choices=[('1', '1室1廳'), ('2', '2室1廳'), ('3', '3室1廳'), ('4', '4室2廳')], max_length=1, verbose_name='房型')),
                ('direction', models.CharField(choices=[('e', '東'), ('s', '南'), ('w', '西'), ('n', '北')], max_length=2, verbose_name='朝向')),
                ('floor', models.CharField(choices=[('l', '低樓層'), ('m', '中樓層'), ('h', '高樓層')], max_length=1, verbose_name='樓層')),
                ('area', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='面積(平方米)')),
                ('area_class', models.CharField(blank=True, choices=[('1', '<50坪'), ('2', '50-70坪'), ('3', '70-90坪'), ('4', '90-140坪'), ('5', '>140坪')], max_length=1, null=True, verbose_name='面積')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='月租')),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='發布日期')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='修改日期')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.community', verbose_name='縣市')),
            ],
            options={
                'verbose_name': '房子',
                'verbose_name_plural': '房子',
            },
        ),
    ]
