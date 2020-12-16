def toString(List):
        distance = 0
        List = [int(i) for i in List] 
        for i in range(len(List)):
                if i == len(List)-1:
                        distance += grid[List[i]][List[0]]
                else:
                        distance += grid[List[i]][List[i+1]]
        print (List,distance)
  
def permute(a, l, r): 
    if l==r: 
        toString(a) 
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l]


def perm(grid):
        cities = [str(i) for i in range(len(grid))]
        permute(cities,0,len(cities)-1)
