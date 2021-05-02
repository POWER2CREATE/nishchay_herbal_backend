from django.db import models

# Create your models here.


INDUSTRY = (
    ("Accountancy", "Accountancy"),
    ("Business", "Business"),
    ("Charity and Voluntary Work", "Charity and Voluntary Work"),
    ("Creative Arts and Design", "Creative Arts and Design"),
    ("Energy and Utilities", "Energy and Utilities"),
    ("Creative Arts and Design", "Creative Arts and Design"),
    ("Engineering and Manufacturing", "Engineering and Manufacturing"),
    ("Environment and Agriculture", "Environment and Agriculture"),
    ("Healthcare", "Healthcare"),
    ("Hospitality and Event Management", "Hospitality and Event Management"),
    ("Information Technology", "Information Technology"),
    ("Law", "Law"),
    ("Leisure, Sports, and Tourism", "Leisure, Sports, and Tourism"),
    ("Marketing, Advertising, and PR", "Marketing, Advertising, and PR"),
    ("Media and Internet", "Media and Internet"),
    ("Property and Consultation", "Property and Consultation"),
    ("Public Services and Administration", "Public Services and Administration"),
    ("Recruitment and HR", "Recruitment and HR"),
    ("Retail", "Retail"),
    ("Sales", "Sales"),
    ("Science and Pharmaceuticals", "Science and Pharmaceuticals"),
    ("Social Care", "Social Care"),
    ("Teacher Training and Education", "Teacher Training and Education"),
    ("Transport and Logistics", "Transport and Logistics"),
)

STATUS = (
    ("Applied", "Applied"),
    ("Selected", "Selected"),
    ("Not Selected", "Not Selected"),
    ("Shortlisted", "Shortlisted"),
)


class JobRecruiter(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    company_name = models.CharField(max_length=80)
    job_title = models.CharField(max_length=80)
    location = models.CharField(max_length=50)
    your_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    industry = models.CharField(max_length=80, choices=INDUSTRY)
    experience = models.CharField(max_length=20)
    salary_from = models.CharField(max_length=20)
    salary_to = models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    description = models.TextField()
    requirements = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.job_title)


class JobSeeker(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT)
    resume = models.FileField(upload_to="Job/Resume/")
    job = models.ForeignKey('job.JobRecruiter', on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    saved = models.BooleanField(default=False)
    applied = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=STATUS, default="Applied")

    def __str__(self):
        return str(self.user)
