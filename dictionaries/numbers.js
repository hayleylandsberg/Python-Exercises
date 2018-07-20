const numbers = [4, 3, 2, 6, 5, 6, 7, 5, 3, 4, 1, 12, 98, 23, 43, 23, 65]

//Figure out how many times a number exists in the array
//Big O notation - interviewers love to ask this question

const numberCounts = {}
numbers.forEach(sourceNumber => {
    if(numberCounts[sourceNumber]) {
        numberCounts[sourceNumber]++
    } else {
        numberCounts[sourceNumber] = 1
    }
})

//OR

numbers.forEach(sourceNumber => {
    let numberOfTimesItExists = 0

    numbers.forEach(targetNumber => {
        if (targetNumber === sourceNumber) {
            numberOfTimesItExists++
        }
    })
})