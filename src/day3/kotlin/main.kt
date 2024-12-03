
val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText())
    part2(obj.javaClass.getResource("input1.txt").readText())
}

val mulRegex = Regex("mul\\((\\d+),(\\d+)\\)")

fun part1(src: String) {
    println(mulRegex.findAll(src).map { it.groupValues[1].toInt() * it.groupValues[2].toInt() }.sum())
}

val progRegex = Regex("(mul)\\((\\d+),(\\d+)\\)|do\\(\\)|don't\\(\\)")

fun part2(src: String) {
    var mul = true
    var sum = 0
    for (matchResult in progRegex.findAll(src)) {
        if (matchResult.groupValues[0] == "do()") {
            mul = true
        }
        if (matchResult.groupValues[0] == "don't()") {
            mul = false
        }
        if (mul && matchResult.groupValues[1] == "mul") {
            sum += matchResult.groupValues[2].toInt() * matchResult.groupValues[3].toInt()
        }
    }
    println(sum)
}