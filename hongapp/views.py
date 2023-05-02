from django.shortcuts import render
from django.http import HttpResponse
from .models import Hong, Point
from django.core.paginator import Paginator
from django.utils import timezone
import hashlib
from geopy.geocoders import Nominatim


def cafe(request):
    page = request.GET.get('page', '')
    if not page: page = '1'
    page = int(page)

    prd = request.GET.get('prd', '')
    hong = Hong.objects.filter(name__contains=prd).order_by('id')
    p = Paginator(hong, 10)

    s_page = (page - 1) // 10 * 10 + 1
    e_page = s_page + 9
    pages = range(s_page, e_page + 1)

    return render(request, "hongapp/cafe.html", 
                    {
                      "hong": p.page(page),
                      'pages': pages,
                      'page': page
                    }
                )

def total(request):
    page = request.GET.get('page', '')
    if not page: page = '1'
    page = int(page)

    prd = request.GET.get('prd', '')
    hong = Hong.objects.filter(name__contains=prd).order_by('id')
    p = Paginator(hong, 10)

    s_page = (page - 1) // 10 * 10 + 1
    e_page = s_page + 9
    pages = range(s_page, e_page + 1)

    address_list = Nominatim(user_agent = 'South Korea', timeout=None)
    address = Hong.objects.values('address')
    geo = address_list.geocode(address)
    crd = {"lat": str(geo.latitude), "lng": str(geo.longitude)}

    for i in range(len(address_list)):
      a = address_list[i].split(' ')
      address_list[i] = " ".join(a[0:4])

    # 주소 리스트를 반복문으로 돌면서 위도 경도 정보 추출


     
    return render(request, "hongapp/total.html", 
                    {
                      "hong": p.page(page),
                      'pages': pages,
                      'page': page,
                      
                    }

                )

def main(request):
    return render(request, "hongapp/main.html", {})

def geo(request):

  geolocator = Nominatim(user_agent = 'South Korea', timeout=None)
  addresses = []
  hongs = Hong.objects.all()

  coords = []

  for hong in hongs:
    a = hong.address.split(' ')
    location = geolocator.geocode(" ".join(a[0:4]))

    if location:
        hong.lat = location.latitude
        hong.lng = location.longitude
        hong.save()

    coords.append({"lat": str(location.latitude), "lng": str(location.longitude)})

  print(coords)
  return render(request, 'hongapp/geo.html', {'coords': coords})
