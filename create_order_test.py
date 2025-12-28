import sender_stand_request

import data 

# Екатерина Гавриленко , 38-я когорта — Финальный проект. Инженер по тестированию плюс

def test_create_order():
    create_order_response = sender_stand_request.create_order(data.order_body)
    
    assert create_order_response.status_code == 201

    track = create_order_response.json()["track"]

    get_order_by_track_response = sender_stand_request.get_order_by_track(track)

    assert get_order_by_track_response.status_code == 200