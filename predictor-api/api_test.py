import requests
import json

if __name__ == '__main__':
    url = "https://pic-metric-1.herokuapp.com/predictor"
    # url = 'http://127.0.0.1:5000/predictor' # if you want to test local
    # url = "my-heroku-app.heroku.com" # if you want to test deployed

    # these work:
    # photo_url = 'https://www.futurity.org/wp/wp-content/uploads/2019/02/viceroy-butterfly_1600.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/0/05/Underwoodfive.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/e/eb/Ash_Tree_-_geograph.org.uk_-_590710.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/0/08/Espadon-Morges.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/8/8f/Windsor_Castle_at_Sunset_-_Nov_2006.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/d/dc/Fountain_in_the_Parc_de_Versailles_%282519408544%29.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/7/70/Jan_Vermeer_van_Delft_013.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/d/d4/Pelikan_Walvis_Bay.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/2/23/Georgia_Aquarium_-_Giant_Grouper_edit.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/P-51_Mustang_edit1.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/7/71/2010-kodiak-bear-1.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/0/00/Ladder_aluminum.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/1/15/Late_model_Ford_Model_T.jpg'

    # another 10:
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/1/15/Les_Paul_57_Custom.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/4/47/Taiwan_2009_Tainan_City_Organic_Farm_Watermelon_FRD_7962.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/a/ae/Watermelon_cross_BNC.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/a/a4/Albert_Eckhout_1610-1666_Brazilian_fruits.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/c/cc/Watermelon_seedless.jpg'
    # photo_url = 'https://upload.wikimedia.org/wikipedia/commons/c/cb/Pineapple_and_cross_section.jpg'
    photo_url = 'https://upload.wikimedia.org/wikipedia/commons/3/3a/Charles-pineapple.jpg'
    # photo_url = 'https://images-na.ssl-images-amazon.com/images/I/81WJyO53YAL._SL1500_.jpg'
    # photo_url = 'https://media.self.com/photos/5b4371cc4d0c3c282a8878d3/4:3/w_752,c_limit/pineapple.jpg'
    # photo_url = 'https://www.squishable.com/mm5/graphics/00000001/squish_pineapple_15.jpg'

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
