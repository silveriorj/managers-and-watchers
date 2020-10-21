import json

filename = 'data/source_file.json'


def read_file():
    with open(filename) as json_file:
        data = json.load(json_file)
        data = sorted(data, key=lambda k: k['priority'])
        return data


def get_managers(data=None):
    managers_list = list()

    for d in data:
        managers = [manager for manager in d['managers'] if manager not in managers_list]
        managers_list += managers
    return managers_list


def get_watchers(data=None):
    watchers_list = list()

    for d in data:
        watchers = [watcher for watcher in d['watchers'] if watcher not in watchers_list]
        watchers_list += watchers
    return watchers_list


def get_projects(watchers=None, managers=None, data=None):
    watchers_projects = dict()
    for w in watchers:
        watchers_projects[w] = list()
        for d in data:
            if w in d['watchers']:
                watchers_projects[w].append(d['name'])

    managers_projects = dict()
    for w in managers:
        managers_projects[w] = list()
        for d in data:
            if w in d['managers']:
                managers_projects[w].append(d['name'])

    return watchers_projects, managers_projects


def save_files(w_file, m_file):
    with open('managers.json', 'w') as outfile:
        json.dump(m_file, outfile, indent=4)

    with open('watchers.json', 'w') as outfile:
        json.dump(w_file, outfile, indent=4)


def start():
    data = read_file()
    managers = get_managers(data=data)
    watchers = get_watchers(data=data)
    w_projects, m_projects = get_projects(managers=managers, watchers=watchers, data=data)
    save_files(w_file=w_projects, m_file=m_projects)


if __name__ == '__main__':
    start()
