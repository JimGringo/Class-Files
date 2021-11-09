def addContacts(phoneContacts, name, cell, work):
    phoneContacts[name] = cell, work
    print(phoneContacts[name])

phoneContacts = {}

addContacts(phoneContacts, "Tom", "701-741-cell", "701-777-work")
addContacts(phoneContacts, "Cody", "701-701-cell", "701-377-work")
addContacts(phoneContacts, "Jimin", "701-791-cell", "701-747-work")

