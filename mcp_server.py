import sys
import json
from client import HopcroftKarpMatcher

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "match":
        adj = {int(k): v for k, v in params.get("adj", {}).items()}
        matcher = HopcroftKarpMatcher(adj, params.get("u_size", 0), params.get("v_size", 0))
        return matcher.find_max_matching()
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
