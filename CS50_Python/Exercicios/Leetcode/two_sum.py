def two_sum(nums, target):
    # Solução 1: Força Bruta (O(n²))
    def brute_force(nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
    # Solução 2: HashMap (O(n))
    def hash_map_solution(nums, target):
        
        num_dict = {} 
        # HashMap (Armaneza os números encontrados e os seus índices)
        
        for i, num in enumerate(nums):
            num2 = target - num

            # Verifica se o complemento já foi visto
            if num2 in num_dict:
                return [num_dict[num2], i]
            num_dict[num] = i
        return []
    return hash_map_solution(nums, target)

# Exemplos de teste
print(two_sum([2,7,11,15], 9))     # Output: [0, 1]
print(two_sum([3,2,4], 6))         # Output: [1, 2]
print(two_sum([3,3], 6))           # Output: [0, 1]