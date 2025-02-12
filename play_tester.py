# import source code
from viewing_party.party import *

# import test data
from tests.test_constants import *

# import "pretty-print" library
import pprint
pp = pprint.PrettyPrinter(indent=4)

# play testing section
# print("\n-----Wave 01 test data-----")
# pp.pprint(HORROR_1)
# pp.pprint(FANTASY_1)
# pp.pprint(FANTASY_2)

# print("\n-----Wave 02 user_data-----")
# pp.pprint(clean_wave_2_data())

#print("\n-----Wave 03 user_data-----")
#pp.pprint(clean_wave_3_data())

# Wave 04 user data
# print("\n-----Wave 04 user_data-----")
# pp.pprint(clean_wave_4_data())
# amandas_data = {
#         "subscriptions": ["hulu", "disney+"],
#         "watched": [],
#         "friends": [
#             {
#                 "watched": [HORROR_1b]
#             },
#             {
#                 "watched": [FANTASY_3b]
#             }
#         ]
#     }

#     # Act
# recommendations = get_available_recs(amandas_data)
# print(recommendations)

# Wave 05 user data
#print("\n-----Wave 05 user_data-----")
#pp.pprint(clean_wave_5_data())
user_data = clean_wave_5_data()
genres = {}

for movie in user_data["watched"]:
    if movie["genre"] not in genres:
        genres[movie["genre"]] = 1
    else:
        genres[movie["genre"]] +=1

favorite_genre = max(genres, key=genres.get)

print(favorite_genre)
