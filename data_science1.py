from collections import Counter

frdsh = [(0, 3), (2, 0), (3, 2), (1, 3), (4, 0)]
users: list[dict] = [{'id': [50], 'name': 'Sveta'}, {'id': 10, 'name': 'Jhon'}, {'id': 20, 'name': 'Ray'},
                     {'id': 30, 'name': 'Ciril'}, {'id': 40, 'name': 'David'}]

for user in users:
    # print(user)
    user['friends'] = []
    # print(user)
    # user['friends'] = []
    # print(user['name'], '///')
for i, j in frdsh:
    # print(i, j)
    # print('\t' * 3, (users[i])['friends'])

    # user['friends'] = []
    # print(user, ' ok')

    #     friends = [users[i],users[j]]

    users[i]['friends'].append(j)
    # print('\t' * 3, 'friends  ', (users[i])['friends'])
    users[j]['friends'].append(i)

print(users)


def not_the_same(user: [dict], other_user):
    # print( users[other_user]['id'], ' qqqqqqqq')
    # print(user['id'])
    # print(users[user]['id'], ' ppppppppppp')

    # print(users[0]['id']!= users[other_user]['id'])
    return user['id'] != users[other_user]['id']

    # print(user['id'], users[other_user]['id'], '  other_user')


# print(not_the_same(users[4], users[0]), '  not_the_same')


def not_friends(user, other_user):
    # print(user['friends'], ' други заданного юзера')
    # print(other_user,'  index other_user')
    # for friend in user['friends']:
    #     print(friend, ' friends  user ;  user index = ', users.index(user))
    # for friend1 in other_user['friends']:
    #     print(friend1, ' friends  other_user ;  other_user index =  ', users.index(other_user))

    return all(not_the_same(user, other_user) for friend in user['friends'])


# print(not_friends(users[4], users[1]), '  not_friends ')
def friends_of_friend_ids(user):
    for friend in user['friends']:
        print(friend, ' friend set user ->', users.index(user))
        print(users[friend]['friends'], 'friends  they are other_user and foat ->', friend)
    return Counter(foat for friend in user['friends'] for foat in users[friend]['friends']
                   if not_the_same(user, foat) and not_friends(user, foat))

    # return Counter(foat for friend in user['friends'] for foat in users[friend]['friends'] )


print(friends_of_friend_ids(users[0]))

var = [1, 2, 4, 8, 16]
vari = [16, 8, 4, 2, 1]
tot = [x + y for x, y in zip(var, vari)]
print(tot)
for j in [i for i in enumerate(var)]:
    print(j)
