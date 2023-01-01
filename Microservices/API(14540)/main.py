from fastapi import FastAPI

from routers import root, users, jokes


app = FastAPI()

app.include_router(root.router)
app.include_router(jokes.router)
app.include_router(users.router)



# {
# 'id': 0, # Auto generating
# 'username': 0, # POST
# 'token': '', # Auto
# 'data': {
#     'opened_boars': [], # Get info from database
#     'jokes': [],
#     'photos_uniq_ids': [],
#     'friends': [
#         {
#             'username': '',
#             'id': 0
#         },
#         {
#             'username': '',
#             'id': 0
#         }
#     ],
#     'is_admin': False, # For new users
#     'premium': False,

#     'wallet': {
#         'status': 'not_opened' # May be 'closed' or 'opened'
#         # 'count': 125,
#     }
# }
# }