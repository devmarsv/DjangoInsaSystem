from django.db import models
# Create your models here.
class Common(models.Model):
    gubun = models.CharField(max_length=30)
    code = models.TextField(max_length=10)
    name = models.CharField(max_length=10)
    note = models.CharField(max_length=20)
    
class User(models.Model):
	sabun = models.IntegerField()
	join_day = models.CharField(max_length=20, default='')
	retire_day = models.CharField(max_length=20, default='')
	put_yn = models.CharField(max_length=2, default='')
	name = models.CharField(max_length=20, default='')
	reg_no = models.CharField(max_length=20, default='')
	eng_name = models.CharField(max_length=20, default='')
	phone = models.CharField(max_length=20, default='')
	hp = models.CharField(max_length=20, default='')
	carrier = models.CharField(max_length = 100, default='')
	pos_gbn_code = models.CharField(max_length=10, default='')
	cmp_reg_no = models.CharField(max_length=100, default='')
	sex = models.CharField(max_length=10, default='')
	years = models.IntegerField(default=0)
	email = models.CharField(max_length = 30, default='')
	zip = models.CharField(max_length = 20, default='')
	addr1 = models.CharField(max_length= 100, default='')
	addr2 = models.CharField(max_length = 100, default='')
	dept_code = models.CharField(max_length = 20, default='')
	join_gbn_code = models.CharField(max_length = 30, default='')
	user_id = models.CharField(unique=True, max_length = 20, default='')
	pwd = models.CharField(max_length = 30, default='')
	salary = models.IntegerField(default=0)
	kosa_reg_yn = models.CharField(max_length = 4, default='')
	kosa_class_code = models.CharField(max_length = 10, default='')
	mil_yn = models.CharField(max_length = 4, default='')
	mil_type = models.CharField(max_length = 20, default='')
	mil_level = models.CharField(max_length = 20, default='')
	mil_startdate = models.CharField(max_length = 20, default='')
	mil_enddate = models.CharField(max_length = 20, default='')
	job_type = models.CharField(max_length = 20, default='')
	gart_level = models.CharField(max_length = 20, default='')
	self_intro = models.CharField(max_length = 100, default='')
	crm_name = models.CharField(max_length = 20, default='')
	profile = models.CharField(max_length = 100, default='')
	cmp_reg_image = models.CharField(max_length = 100, default='')

class Profilea(models.Model):
    file_path = models.FileField(upload_to='upload_files/')
    file_name = models.CharField(max_length = 200)
    upload_id = models.ForeignKey(User, on_delete = models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)

class Cmp_reg_imagea(models.Model):
	file_path = models.FileField(upload_to='upload_files/')
	file_name = models.CharField(max_length = 200)
	upload_id = models.ForeignKey(User, on_delete = models.CASCADE)
	create_time = models.DateTimeField(auto_now_add=True)

class Carriera(models.Model):
	file_path = models.FileField(upload_to='upload_files/')
	file_name = models.CharField(max_length = 200)
	upload_id = models.ForeignKey(User, on_delete = models.CASCADE)
	create_time = models.DateTimeField(auto_now_add=True)


