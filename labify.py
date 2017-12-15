#Gozde DOGAN
#131044019
#CSE 321 Introduction To Algorithm Design
#HW3
#findMinimumCostToLabifyGTU

import sys


def main():
	mapOfGTU = mapOfGTU = {
 							1 : set([2,3]),
 							2 : set([1,3]),
 							3 : set([1,2]) }
 				
	cost = findMinimumCostToLabifyGTU(2,1,mapOfGTU)
	print "\n----------------------------------"
	print "cost: ", cost
	print "----------------------------------\n"

	
def findMinimumCostToLabifyGTU(computerPrice,pathPrice,graph):
	price = -1
	priceMin = 1000
	for next in graph:
		visited = BFS(graph, next)
		if price <= priceMin:
			price = (len(visited)-1)*pathPrice + computerPrice
		
	return price
	
#Data Structures dersinden gorulen algoritma kullanildi
def BFS(graph, start):
   visited = []
   queue = [start]

   while queue:
       vertex = queue.pop(0)
       
       if vertex not in visited:
           visited.append(vertex)
           neighbours = graph[vertex]

           for neighbour in neighbours:
               queue.append(neighbour)
               
   return visited
			
			
if __name__ == '__main__':
    main()
