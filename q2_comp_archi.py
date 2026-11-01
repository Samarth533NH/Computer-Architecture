def simulate_direct_mapped_cache():
    num_cache_lines = 8
    cache = [None] * num_cache_lines
    access_sequence = [3, 11, 3, 19, 11, 27, 3]
    hits = 0
    misses = 0
    
    print(f"{'Block':<10}{'Line Calculated':<20}{'Result':<10}{'Cache Contents (Line: Block)'}")
    print("-" * 75)
    
    for block in access_sequence:
        line = block % num_cache_lines
        
        if cache[line] == block:
            result = "HIT"
            hits += 1
        else:
            result = "MISS"
            misses += 1
            cache[line] = block
            
        cache_state = ", ".join([f"{i}:{cache[i]}" for i in range(num_cache_lines) if cache[i] is not None])
        if not cache_state:
            cache_state = "Empty"
            
        print(f"{block:<10}{line:<20}{result:<10}{cache_state}")
        
    total_accesses = len(access_sequence)
    hit_ratio = hits / total_accesses
    
    print("-" * 75)
    print("\nFINAL METRICS:")
    print(f"Total Hits   : {hits}")
    print(f"Total Misses : {misses}")
    print(f"Hit Ratio    : {hit_ratio:.4f} ({hit_ratio * 100:.2f}%)")
    print("-" * 75)

if __name__ == "__main__":
    simulate_direct_mapped_cache()
