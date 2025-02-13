def canCompleteCircuit(gas, cost):
    total_gas, total_cost, tank, start = 0, 0, 0, 0

    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]

        # If the tank is negative, reset the starting point to the next station
        if tank < 0:
            start = i + 1
            tank = 0

    # If total gas is less than total cost, it's impossible to complete the circuit
    return start if total_gas >= total_cost else -1


gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]print(canCompleteCircuit(gas, cost))
# Output: 3

gas = [5, 1, 2, 3, 4]
cost = [4, 4, 1, 5, 1]
print(canCompleteCircuit(gas, cost))
# # Output 4

gas = [2, 3, 4]
cost = [3, 4, 3]
print(canCompleteCircuit(gas, cost))
# Output: -1
