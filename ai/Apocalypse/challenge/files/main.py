def read_team_tries(filename):
    teams = {}
    with open(filename, 'r') as file:
        for line in file:
            team, tries = line.strip().split(':')
            teams[team] = int(tries)
    return teams

def update_team_tries(filename, teams):
    with open(filename, 'w') as file:
        for team, tries in teams.items():
            file.write(f"{team}:{tries}\n")

def verify_submission(submitted):
    true = "1011011110110011110111000001011110001110"
    ones_count = 0
    zombie = False

    if len(submitted) != len(true):
        return False
    
    for idx, value in enumerate(submitted):
        if value not in ['0', '1']:
            return False
        
        if value == '1' and true[idx] == '1':
            ones_count += 1 

        elif value == '1' and true[idx] != '1':
            zombie = True
            break
    
    return ones_count >= 10 and not zombie

teams_tries_file = "/data/teams_tries.txt"
teams_tries = read_team_tries(teams_tries_file)

user_id = input("Enter your team ID: ")

if user_id not in teams_tries:
    print("Team ID not found. You are not allowed to submit.")
    exit(1)

if teams_tries[user_id] > 10:
    print("You have exceeded the maximum number of tries.")
    exit(1)

user_input = input("Enter your submission: ")

success = verify_submission(user_input)

teams_tries[user_id] += 1
update_team_tries(teams_tries_file, teams_tries)

if success:
    print("ingeneer{M4ch1n3_L34rn1ng_1s_34sy!}")
    exit(0)
else:
    print("False")
    print(f"Only {10 - teams_tries[user_id]} Tries left for you")
    exit(1)
