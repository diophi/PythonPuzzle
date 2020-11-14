
class Solver:


    def convert_to_tuple(text):
        result = []
        for line in text:
            for char in line:
                result.append(char)
        return tuple(result)            

    def decrypt_path(string, n):
        path = ''
        prev = ''
        for char in string:
            if char != '-' :
                if prev == '-': #negative positions
                    if char == str(n):
                        path += 'U'
                    elif char =='1':
                        path += 'L'
                else: #positve positions
                    if char == str(n):
                        path += 'D'
                    elif char =='1':
                        path += 'R'
            prev = char
        return path

    def swap(t, zero, target):
        t = list(t) 
        t[zero], t[target] = t[target], t[zero]
        return tuple(t)
        
    def issafe(x,n):
        if 0 <= x <n**2:
            return True
        else:
            return False

    def solve(self, board, final, n:int) -> int:
        seen = set() 
        q = [(board, 0, 0,'')]

        pos = [-1,1,n,-n]

        while q: 
           
            board, level, move, path = q.pop(0)
            if board == final:
                return path
            
            i = board.index(1)

            nexts = []

            for p in pos:
                if Solver.issafe(i+p,n):
                    if ( (i+1)%n == 0 and p == 1) or (i%n == 0 and p == -1 ) :
                        continue
                    else:
                        nexts.append((Solver.swap(board,i,i+p),p))
            
            #print(nexts)
            for b,p in nexts:
                if b not in seen:
                    if b != final:
                        seen.add(b)
                    q.append((b, level+1, p, path+str(p)))
        
        return -1


def main():
    n= 3
    
    initial = Solver.convert_to_tuple([[2,3,1],[4,5,6],[7,8,9]])
    print(''.join(str(initial)))

    final = Solver.convert_to_tuple([[1,2,3],[4,5,6],[7,8,9]])
    print(''.join(str(final)))
    sol = Solver()
    print(Solver.decrypt_path(sol.solve(initial,final,n),n))



if __name__ == '__main__':
    main()
    