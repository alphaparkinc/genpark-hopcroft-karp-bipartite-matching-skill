from client import HopcroftKarpMatcher

def main():
    print("=== Hopcroft-Karp Bipartite Matching ===")
    adj = {0: [0, 1], 1: [1, 2], 2: [0]}
    matcher = HopcroftKarpMatcher(adj, u_size=3, v_size=3)

    res = matcher.find_max_matching()
    print("Matching Output:", res)
    assert res["max_matching_cardinality"] == 3
    assert len(res["matched_pairs"]) == 3

    print("Hopcroft-Karp Matcher verified successfully!")

if __name__ == "__main__":
    main()
