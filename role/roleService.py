import user.userService as userService
import role.roleDao as roleDao
from flask import jsonify


# this need a refactoring
def getUserRole():
    user = userService.getUser()
    print("user role :" + user.role_id )
    role=roleDao.getRoleFromId(user.role_id)
    response = role.__dict__
    pivot= dict()
    pivot['user_id'] =user.id
    pivot['role_id'] = role.id
    response['pivot'] =pivot

    responseList= list()
    responseList.append(response)

    return jsonify({
        "role": responseList
    })

