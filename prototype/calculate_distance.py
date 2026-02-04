import numpy as np

# 거리계산 로직
# SQL query로 대체 예정
def calculate_distance(lat1, lng1, lat2, lng2):
    """
    두 지점 사이의 거리를 km 단위로 계산 (Haversine 공식)
    """
    R = 6371  # 지구 반지름 (km)

    # 라디안 변환
    phi1, phi2 = np.radians(lat1), np.radians(lat2)
    dphi = np.radians(lat2 - lat1)
    dlamb = np.radians(lng2 - lng1)

    # 하버사인 공식 수식
    # a = sin²(Δφ/2) + cos φ1 ⋅ cos φ2 ⋅ sin²(Δλ/2)
    a = np.sin(dphi / 2) ** 2 + np.cos(phi1) * np.cos(phi2) * np.sin(dlamb / 2) ** 2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    return R * c