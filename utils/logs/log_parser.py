import json

def parse_logs(path):
    with open(path) as file:
        for line in file:
            data = json.loads(line)
            if data.get("eventid") == "cowrie.command.input":
                print(f"> Attacker typed: {data['input']}")
