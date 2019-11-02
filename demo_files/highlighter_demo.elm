-- Module


module MyModule exposing (..)


-- Qualified Imports

import List as L exposing (foldl, map)
import Maybe exposing (Maybe(..))



-- A single line comment
{- A multiline comment
   {- can be nested -}
-}



True  : Bool
False : Bool

42    : number  -- Int or Float depending on usage
3.14  : Float

'a'   : Char
"abc" : String


-- multi-line String
"""
This is useful for holding JSON or other
content that has "quotation marks".
"""

True && not ( True || False )
( 2 + 4 ) * ( 4^2 - 9 )
"abc" ++ "def"


-- Lists

[ 1, 2, 3, 4 ]
1 :: [ 2,3,4 ]
1 :: 2 :: 3 :: 4 :: []


-- Conditionals
if powerLevel > 9000 then "OVER 9000!!!" else "meh"

if key == 40 then
    n + 1

else if key == 38 then
    n - 1

else
    n


-- Case
case maybeList of
    Just xs -> xs
    Nothing -> []

  case xs of
      [] ->
          Nothing
          first :: rest ->
              Just ( first, rest )

  case n of
      0 -> 1
      1 -> 1
      _ -> fib ( n - 1 ) + fib ( n - 2 )




-- Records
-- create records


origin =
    { x = 0, y = 0 }


point =
    { x = 3, y = 4 }



-- access fields

origin.x == 0
point.x == 3


-- field access function

List.map .x [ origin, point ] == [ 0, 3 ]


-- update a field

{ point | x = 6 } == { x = 6, y = 4 }


-- update many fields

{ point | x = point.x + 1, y = point.y + 1 }



-- Functions


square n =
    n ^ 2


hypotenuse a b =
    sqrt (square a + square b)


distance ( a, b ) ( x, y ) =
    hypotenuse (a - x) (b - y)


square =
    \n -> n ^ 2


squares =
    List.map (\n -> n ^ 2) (List.range 1 100)



-- Type Annotations


answer : Int
answer =
    42


factorial : Int -> Int
factorial n =
    List.product (List.range 1 n)


distance : { x : Float, y : Float } -> Float
distance { x, y } =
    sqrt (x ^ 2 + y ^ 2)



-- Operators


viewNames1 names =
    String.join ", " (List.sort names)


viewNames2 names =
    names
        |> List.sort
        |> String.join ", "



-- Let

let
    twentyFour =
        3 * 8

    sixteen =
        4 ^ 2
in
    twentyFour + sixteen


let
    name : String
    name =
        "Hermann"

    increment : Int -> Int
    increment n =
        n + 1
in
    increment 10



-- Applying Functions
-- alias for appending lists and two lists

append xs ys =
    xs ++ ys


xs =
    [ 1, 2, 3 ]


ys =
    [ 4, 5, 6 ]



-- All of the following expressions are equivalent:


a1 =
    append xs ys


a2 =
    xs ++ ys


b2 =
    (++) xs ys


c1 =
    append xs ys


c2 =
    (++) xs ys



-- Type Aliases


type alias Name =
    String


type alias Age =
    Int


info : ( Name, Age )
info =
    ( "Steve", 28 )


type alias Point =
    { x : Float, y : Float }


origin : Point
origin =
    { x = 0, y = 0 }



-- Custom Types


type User
    = Regular String Int
    | Visitor String
