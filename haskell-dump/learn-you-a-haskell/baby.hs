
doubleSmallNumber x = if x > 100
                       then x
                       else x*2

doubleSmallNumber' x = (if x > 100 then x else x*2) + 1

length' xs = sum [1 | _ <- xs]

removeNonUppercase :: String -> String
removeNonUppercase st = [ c | c <- st, c `elem` ['A'..'Z']]

addThree :: Int -> Int -> Int -> Int
addThree x y z = x + y + z

circumference :: Double -> Double
circumference r = 2 * pi * r

meow :: Int -> (Int, Int)
meow r = (2 * r, r)

