#nested dict

dx = {
    'name':'smit',
    'fav_game':['criket','football','hocky'],
    'sub':{'math':88,'sci':67,'eng':99}
}

d1 = {
    'name':'nitya',
    'fav_games':['criket','football','hocky'],
    'subject':{'math':90,'eng':88,'sci':70}
    }

for k,v in dx.items():
    print(f'{k} = {v}')

#access list as element from dict
print(dx['fav_game'][1])

#access dict element from another dict
