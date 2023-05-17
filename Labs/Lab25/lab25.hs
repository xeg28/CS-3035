-- Part 1 Code --
--Prelude> list1 = [1..5]
--Prelude> [x^2 | x <- list1]

-- Part 1 Output --
--[1,4,9,16,25]

-- Part 2 Code --
--Prelude> string = "California State University Los Angeles"
--Prelude> [x | x <- string, fromEnum x > 64, fromEnum x < 91]

-- Part 2 Output --
--"CSULA"

-- Part 3 Code --
--gradeFinder grade1 grade2  
--    | (grade1 + grade2) / 2 >= 70, (grade1 + grade2) / 2 < 80   = "Your grade: C."
--    | (grade1 + grade2) / 2 >= 80, (grade1 + grade2) / 2 < 90   = "Your grade: B."
--    | (grade1 + grade2) / 2 >= 90   = "Your grade: A."
--    | otherwise = "You did not pass."
    
--main = do
--   print(gradeFinder 70 92.5)
   
-- Part 3 Output  --

-- "Your grade: B."

-- Part 4 Code -- 

fibonacci x = 
    case x of
        0 -> 0
        1 -> 1
        n -> fibonacci (n-1) + fibonacci(n-2)
        
main = do
   print(fibonacci 6)
   
   
