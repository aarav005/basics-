package main

import (
	"fmt"
	"time"
)

///importing math package...

/*func main() {
•	    //using variables and constants

•	    var num1 int  = 2
•	    var num2 int = 3 ///uint only accepts positive value
•	    num3 :=8 // easy way to assign variable
•	    //var num1,num2 int ....varible with the same type can be assigned in the single line...
•	    num1,num2= 4,6 /// example of setting the variable in the same line
•	    const num4= 8 // using constant
•	    //num4=7 ...this cannot be done since num4 is declared as constant.
•	    fmt.Println("Hello aarav")
•	    fmt.Println((num1+ num2))
•	    fmt.Println(num3)
•	}*/

//functions

/*var num2 = 8 //package  level variable...it has to be declared,,
func calc(x int, y int) (int, int) {
	out1 := x + y
	out2 := x - y
	return out1, out2
}
func main() {
	num1 := 7 //num1 is a function level package...
	var num11 float64 = 9
	num3 := math.Sqrt(num11)
	result1, result2 := calc(num1, num2)
	fmt.Println("the result is ", result1, result2)
	fmt.Printf("the square root is %.2f", num3) ///printf for place holder
	loop()
}

//loop in go: there is only "for" loop
func loop() {
	i := 10
	j := 1
	for (i > 0) && (j < 8) { //initilazation,condition, increment can be includeed in the same line with
		fmt.Println(i)
		i = i - 1
		j++
	}
}*/

//example for if else   and switch
func main() {
	num := 5

	if num < 5 {
		fmt.Println("hi the number is", num)
	} else if num == 5 {
		defer fmt.Println("the number is equal to 5", num) // using defer this line is executed at last.
	} else {
		fmt.Println("the number is more than 5", num)
	}
	// using switch... when operation is not required,, switch can be used
	switch time.Now().Weekday() {
	case time.Saturday:
		fmt.Println("today is saturday")
	case time.Sunday:
		fmt.Println("today is weekend")
	default:
		fmt.Println("toady is weekday")
	}

	//structure
	// type can be declared outside the function as well
	type Student struct { // specifying student as a type itself of structure
		rollno int
		name   string
		marks  int
	}
	var s1 Student = Student{101, "aarav", 100}
	fmt.Println(s1)
	fmt.Println(s1.name)
	s2 := Student{marks: 100, name: "robin"}
	fmt.Println(s2.name)

}
