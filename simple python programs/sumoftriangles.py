N = int(input("No of triangles:"));
for _ in range(N):
   n = int(input())
   triangle = []
   for i in range(n):
      row = list(map(int,input().split()))
      triangle.append(row)
   for i in range(n-2,-1,-1):
      for j in range(i+1):
         below_left = triangle[i+1][j]
         below_right = triangle[i+1][j+1]
         triangle[i][j] += max(below_left,below_right)
print(triangle[0][0])
