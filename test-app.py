import requests
import os


def test_health_endpoint():
    """Test if the Flask app health endpoint is working"""
    response = requests.get('http://localhost:5000/health')
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'healthy'
    assert data['database'] == 'connected'
    print("✅ Health endpoint test passed!")


def test_homepage():
    """Test if the homepage loads"""
    response = requests.get('http://localhost:5000/')
    assert response.status_code == 200
    print("✅ Homepage test passed!")


if __name__ == '__main__':
    try:
        test_health_endpoint()
        test_homepage()
        print("\n🎉 All tests passed!")
    except Exception as e:
        print(f"\n❌ Tests failed: {e}")
        exit(1)
```

3. ** Update `requirements.txt`** - add this line at the end:
```
requests == 2.31.0
