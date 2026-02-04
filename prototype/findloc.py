from geopy.geocoders import Nominatim

#연속 요청 시 1초 이상의 간격으로!
def find_address_and_point(address, count=3):
    geolocator = Nominatim(user_agent="mobility-faq")
    try:
        locations = geolocator.geocode(address, exactly_one=False, limit=count)
        if locations:
            return [(location.address, (location.latitude, location.longitude)) for location in locations]
        else:
            print("결과를 찾을 수 없습니다.")
            return None
    except Exception as e:
        print(f"오류 발생: {e}")
        return None