from app.api import app

def test_success():
    cliente = app.test_client()
    resp = cliente.post('/price', json={"price": 990, "coupon": "SALES10", "tax_rate": 0.19})
    assert resp.status_code == 200

def test_fail():
    cliente = app.test_client()
    resp = cliente.post('/price', json={"price": "990", "coupon": "SALES10", "tax_rate": 0.19})
    assert resp.status_code == 500

