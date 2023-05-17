--- Functions with explicit declarations ---

-- Part 1 code --
takeFromList :: [a] -> Int -> a
takeFromList [] y = error "Empty list"
takeFromList x y = x !! y
 
-- Part 1 ouput -- 
-- *Main> l1 = ['a', 'b', 'c', 'd']
-- *Main> takeFromList l1 2
-- 'c'


-- Part 2 code --
getSecondLast :: [a] -> a
getSecondLast [] = error "Empty list"
getSecondLast [x] = error "there is no secondLast"
getSecondLast [x , _] = x
getSecondLast (_:xs) = getSecondLast xs

-- Part 2 output --
-- *Main> l1 = [1,2,3,4,5]
-- *Main> getSecondLast l1
-- 4


-- Part 3 code --
third :: (a,b,c) -> c
third (x,y,z) = z

-- Part 3 output --
-- *Main> t1 = (1,2.2,'a')
-- *Main> third t1
-- 'a'

--- Functions with implicit declarations ---

-- Part 1 Code --
takeFromList1 :: [Int] -> Int -> Int
takeFromList1 [] y = error "Empty list"
takeFromList1 x y = x !! y

-- Part 1 Output -- 
-- *Main> l1 = [1,2,3,4,5]
-- *Main> takeFromList1 l1 2
--  3

-- Part 2 Code -- 
area :: Int -> Int -> Int
area x y = x * y

-- Part 2 Output -- 
-- *Main> area 12 3
-- 36

-- Part 3 Code --
makelist :: Int -> [Int]
makelist x = [1..x]

-- Part 3 Output --
-- *Main> l1 = makelist 10
-- *Main> l1
-- [1,2,3,4,5,6,7,8,9,10]

-- Part 4 Code --
checknum :: Int -> Int -> Int -> Bool
checknum a b c = a * b == c

-- Part 4 Output -- 
-- *Main> checknum 4 5 20
-- True
-- *Main> checknum 3 3 10
-- False

-- Part 5 Code --
checktriplets :: Int -> Int -> Int -> Bool
checktriplets a b c = a*a + b*b == c*c || a*a + c*c == b*b || b*b + c*c ==5  a*a

-- Part 5 Output -- 
-- *Main> checktriplets 3 4 5
-- True
-- *Main> checktriplets 5 4 3
-- True
-- *Main> checktriplets 4 4 2
-- False

