types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

def delete_dublicate():
    all_bugs = []
    for key in tickets.keys():
        unique_bugs = []
        for bug in tickets[key]:
            if bug not in all_bugs:
                all_bugs.append(bug)
                unique_bugs.append(bug)
        tickets[key] = unique_bugs
        
def create_dict(types, tickets):
    new_dict = {}

    for i in range(1, 6):
        new_dict[types[i]] = tickets[i]
    
    return new_dict

delete_dublicate()
new_dict = create_dict(types, tickets)

print(new_dict)