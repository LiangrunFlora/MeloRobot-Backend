from DAO.notify import find_user, get_list


def get_notify_list(id: int):
    exist = find_user(id)
    if exist:
        notify_list = get_list(id)
        object_list = []
        for notify in notify_list:
            n_dict = notify.to_dict()
            object_list.append(n_dict)
        return object_list
    else:
        return []
