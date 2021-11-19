// Duck Typing
/*
	[Resource]
	가장 빨리 만나는 Go언어 by. 이재홍
*/

package main

import "fmt"

func main() {
	var donald Duck
	var john Person

	inTheForest(donald)
	/*
		꽥~!
		오리는 흰색과 회색 털을 갖고 있다.
	*/
	inTheForest(john)
	/*
		사람은 오리를 흉내낸다. 꽥~!
		사람은 땅에서 깃털을 주워서 보여준다.
	*/
}

// Duck
type Duck struct {
}

func (d Duck) quack() {
	fmt.Println("꽥~!")
}

func (d Duck) feathers() {
	fmt.Println("오리는 흰색과 회색 털을 갖고 있다.")
}

// Person
type Person struct {
}

func (p Person) quack() {
	fmt.Println("사람은 오리를 흉내낸다. 꽥~!")
}

func (p Person) feathers() {
	fmt.Println("사람은 땅에서 깃털을 주워서 보여준다.")
}

// Interface
type Quacker interface {
	quack()
	feathers()
}

// Function
func inTheForest(q Quacker) {
	q.quack()
	q.feathers()
}
