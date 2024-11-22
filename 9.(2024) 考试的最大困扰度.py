class Solution:
    def maxConsecutiveAnswers(self, answerKey, k):
        answer_f = self.answer_f(answerKey, k)
        answer_t = self.answer_t(answerKey, k)
        max_length = max(answer_t, answer_f)

        return max_length

    def answer_f(self, answerKey, k):
        max_length = 0
        left = 0
        different_answer_f = {}
        for right in range(len(answerKey)):
            different_answer_f[answerKey[right]] = different_answer_f.get(answerKey[right], 0) + 1
            # 避免 KeyError, F == 0
            while different_answer_f.get('F', 0) > k:
                different_answer_f[answerKey[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
        return max_length


    def answer_t(self, answerKey, k):
        max_length = 0
        left = 0
        different_answer_t = {}
        for right in range(len(answerKey)):
            different_answer_t[answerKey[right]] = different_answer_t.get(answerKey[right], 0) + 1
            # 避免 KeyError, F == 0
            while different_answer_t.get('T', 0) > k:
                different_answer_t[answerKey[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)
        return max_length


solution = Solution()
print(solution.maxConsecutiveAnswers("TTFTTFTTTT", 1))