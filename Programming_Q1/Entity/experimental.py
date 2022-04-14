import collections
from collections import deque



def main():
        print("---------------")
        a = deque()
        a.append('1223456')
        b = deque('1223456')
        print(b)
        print(b.index('2'))

def binary_search(seq: list, search_number):
        start_pos = 0
        last_pos = len(seq) - 1
        
        while start_pos <= last_pos:
                middle_index = start_pos + (last_pos - start_pos) // 2
                print(f'========{middle_index}')
                if seq[middle_index] == search_number:
                        return(f'search index {middle_index}')
                elif search_number > seq[middle_index]:
                        start_pos = middle_index + 1
                elif search_number < seq[middle_index]:
                        last_pos = middle_index -1
                        
                        
                        
def binary_search_revers(seq: list, search_number, start_pos=None, end_pos=None):
        if start_pos is None and end_pos is None:
                start_pos = 0
                end_pos = len(seq) - 1
        middle_index = start_pos + (end_pos - start_pos) // 2
        # print(middle_index)
        if seq[middle_index] == search_number:
                return middle_index
        elif  search_number < seq[middle_index]:
                print('-------------------------')
                return binary_search_revers(seq, search_number,start_pos, middle_index -1 )
        else:
                print('+++++++++++++')
                return binary_search_revers(seq, search_number, middle_index + 1, end_pos )                
        
        
       
        
        
    
if __name__ == "__main__":
        arr = [1,3,4,5,7,11,12,15,34,45]
        print(binary_search(arr, 1))
        print(binary_search_revers(arr, 1))
