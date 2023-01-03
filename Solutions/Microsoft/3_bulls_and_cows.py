# Leetcode 299: Bulls and Cows
# https://leetcode.com/problems/bulls-and-cows/
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_map = {}
        guess_map = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if secret[i] in secret_map:
                    secret_map[secret[i]] += 1
                else:
                    secret_map[secret[i]] = 1
                if guess[i] in guess_map:
                    guess_map[guess[i]] += 1
                else:
                    guess_map[guess[i]] = 1
        for key in guess_map:
            if key in secret_map:
                cows += min(guess_map[key], secret_map[key])
        return str(bulls) + 'A' + str(cows) + 'B'