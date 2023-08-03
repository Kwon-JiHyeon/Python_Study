'''
DNA 판별 프로그램

조건
코돈 : 염기 3개 묶음
시작 코돈 : ATG
종결 코돈 : TAA, TGA, TAG
중간에 TAA, TGA, TAG 가 있으면 안된다.
문자열의 크기 : 3의 배수
'''

def isPotentialGene(dna):
    if len(dna) % 3 != 0:
        return False
        start_list = ['ATG']
        end_list = ['TAA', 'TGA', 'TAG']
        if dna.startswith(tuple(start_list)) and dna.endswith(tuple(end_list)):
            middle = [dna[i:i+3] for i in range(3, len(dna)-3, 3)]
            middle_list = ['TAA', 'TGA', 'TAG']
            if not any(m in middle_list for m in middle):
                return True
    return False

# test
test1 = 'ATGCGCCTGCGTCTGTACTAG'
isPotentialGene(test1)

test2 = 'ATGCGCTGCGTCTGTACTAG'
isPotentialGene(test2)

test3 = 'ATGCGCCTGCGTCTGTAGTAG'
isPotentialGene(test3)
