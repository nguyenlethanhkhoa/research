import requests


resp = requests.get('https://shopee.vn/api/v4/pages/get_category_tree')
resp = resp.json()
categories = resp.get('data').get('category_list')

no = 0
for category in categories:
    no += 1
    print('Add ' + category.get('display_name'))
    resp = requests.post(
        'http://128.199.232.249:10000/product/categories',
        json={
            "title": category.get('name'),
            "parent_id": None,
            'display_name': category.get('display_name'),
            'level': category.get('level')
        }
    )
    print(resp.json())
    item = resp.json().get('data')

    for sub_category in category.get('children'):
        no += 1
        print('Add ' + sub_category.get('display_name'))
        resp = requests.post(
            'http://128.199.232.249:10000/product/categories',
            json={
                "title": sub_category.get('name'),
                "parent_id": item.get('id'),
                'display_name': sub_category.get('display_name'),
                'level': sub_category.get('level')
            }
        )
        print(resp.json())

print(f'Done with {no} items')

