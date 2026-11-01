def simulate_cpu():
    memory = {100: 12, 104: 8, 108: 0}
    registers = {"R1": 0, "R2": 0, "R3": 0}
    instructions = [
        "a) LOAD R1, 100",
        "b) LOAD R2, 104",
        "c) ADD R3, R1, R2",
        "d) STORE R3, 108"
    ]
    
    print("=" * 50)
    print("STARTING CPU SIMULATION")
    print("=" * 50)
    print(f"Initial Memory State: M[100]={memory[100]}, M[104]={memory[104]}\n")
    
    print(f"Executing Step: {instructions[0]}")
    registers["R1"] = memory[100]
    print(f"Current Registers: {registers}\n")
    
    print(f"Executing Step: {instructions[1]}")
    registers["R2"] = memory[104]
    print(f"Current Registers: {registers}\n")
    
    print(f"Executing Step: {instructions[2]}")
    registers["R3"] = registers["R1"] + registers["R2"]
    print(f"Current Registers: {registers}\n")
    
    print(f"Executing Step: {instructions[3]}")
    memory[108] = registers["R3"]
    print(f"Current Registers: {registers}\n")
    
    print("=" * 50)
    print("FINAL RESULTS AFTER EXECUTION")
    print("=" * 50)
    print(f"Register R1: {registers['R1']}")
    print(f"Register R2: {registers['R2']}")
    print(f"Register R3: {registers['R3']}")
    print(f"Memory Location 108 (Final Content): {memory[108]}")
    print("=" * 50)

if __name__ == "__main__":
    simulate_cpu()
