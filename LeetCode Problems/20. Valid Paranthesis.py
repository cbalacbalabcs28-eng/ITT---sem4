class Solution(object):
    def isValid(self, sequence):
         
        while True:
            if '()' in sequence:
                sequence = sequence.replace('()', '')
            elif '{}' in sequence:
                sequence = sequence.replace('{}', '')
            elif '[]' in sequence:
                sequence = sequence.replace('[]', '')
            else:
                return not sequence

if __name__ == '__main__':
    solution = Solution()
    sequence = '{[()]}'
    print('Is {} valid? : {}'.format(sequence, solution.isValid(sequence)))
    sequence1 = '{[()]}{]{}}'
    print('Is {} valid? : {}'.format(sequence1, solution.isValid(sequence1)))
