from django.shortcuts import render
from faker import Faker
import requests
import os
from .models import Job


# Create your views here.
def index(request):
    return render(request, 'jobs/index.html')
    
def pastlife(request):
    name = request.GET.get('name')
    # db에 있는지 확인
    person = Job.objects.filter(name=name).first()
    # person = Job.objects.get(name=name) # 없으면 에러발생
    
    # 있으면, 원래 직업을 가져오고
    # 없으면 faker로 새로운 직업을 넣고 모델에 저장하고 가져옵니다.
    if person:
        pastjob = person.pastjob
    else:
        faker = Faker('ko_kr')
        pastjob = faker.job()
        person = Job(name=name, pastjob=pastjob)
        person.save()
        
    # giphy
    # GIPHY_API = 'lcFtInSNxo5rUMFiV9juaSI9qtM6ASE6'
    GIPHY_API = os.getenv("GIPHY_KEY")
    url = f'http://api.giphy.com/v1/gifs/search?api_key={GIPHY_API}&q={pastjob}&limit=1&lang=ko'
    data = requests.get(url).json()
    image = data.get('data')[0].get('images').get('original').get('url')
        
    return render(request, 'jobs/pastlife.html', {'person': person, 'image': image})
    