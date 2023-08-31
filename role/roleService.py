import user.userService as userService
import role.roleDao as roleDao


# this need a refactoring
def getUserRole():
    user = userService.getUser()
    role=roleDao.getRoleFromId(user.role_id)
    response = role.__dict__
    pivot= dict()
    pivot['user_id'] =user.id
    pivot['role_id'] = role.id
    response['piviot'] =pivot

    responseList= list()
    responseList.append(role)

    return ({
        "role": response
    })

