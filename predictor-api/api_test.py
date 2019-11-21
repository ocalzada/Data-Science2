import requests
import json

if __name__ == '__main__':
    url = "http://127.0.0.1:5000/predictor"
    # url = 'http://127.0.0.1:5000/predictor' # if you want to test local
    # url = "my-heroku-app.heroku.com" # if you want to test deployed

    # this assumes that the agreed upon json key is `key`
    # photo_url = 'https://www.futurity.org/wp/wp-content/uploads/2019/02/viceroy-butterfly_1600.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/0/05/Underwoodfive.jpg'
    photo_url = 'https://upload.wikimedia.org/wikipedia/commons/e/eb/Ash_Tree_-_geograph.org.uk_-_590710.jpg'
    # 'key' is used within a route like a dictionary key
    val = {'url': photo_url, 'photo_id': 3209847}
    r_success = requests.post(url, data=json.dumps(val))

    print(f'request responded: {r_success}.')
    if r_success.status_code == 200:
        print(f'the content of the response was {r_success.json()}')
    else:
        print(r_success)
    # you'll get a 200 response if the keys align,
    # and something bad if the keys don't align.
