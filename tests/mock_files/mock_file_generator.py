import json
import tempfile
from datetime import datetime, timezone

def create_mock_cowrie_log(path=None):
    sample_events = [
        {"eventid": "cowrie.command.input", "input": "ls", "timestamp": str(datetime.now(timezone.utc))},
        {"eventid": "cowrie.command.input", "input": "cd /", "timestamp": str(datetime.now(timezone.utc))},
        {"eventid": "cowrie.command.input", "input": "cat /etc/passwd", "timestamp": str(datetime.now(timezone.utc))}
    ]

    if path is None:
        tmpfile = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.json')
        path = tmpfile.name
    else:
        tmpfile = open(path, 'w')

    for event in sample_events:
        tmpfile.write(json.dumps(event) + "\n")
    
    tmpfile.flush()
    tmpfile.close()

    return path

