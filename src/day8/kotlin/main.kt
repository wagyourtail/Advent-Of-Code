import xyz.wagyourtail.commonskt.collection.defaultedMapOf

val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

operator fun Pair<Int, Int>.plus(p: Pair<Int, Int>): Pair<Int, Int> {
    return this.first + p.first to this.second + p.second
}

operator fun Pair<Int, Int>.minus(p: Pair<Int, Int>): Pair<Int, Int> {
    return this.first - p.first to this.second - p.second
}

operator fun Pair<Int, Int>.times(mul: Int): Pair<Int, Int> {
    return this.first * mul to this.second * mul
}

operator fun Pair<Int, Int>.div(mul: Int): Pair<Int, Int> {
    return this.first / mul to this.second / mul
}

fun <T> List<T>.permutations(size: Int): Sequence<List<T>> {
    if (size == 1) {
        return this.map { listOf(it) }.asSequence()
    }
    val queue = this@permutations.toMutableList()
    return sequence {
        while (queue.size >= size) {
            val first = queue.removeAt(0)
            val perms = queue.permutations(size - 1)
            yieldAll(perms.map { listOf(first) + it })
        }
    }
}

fun part1(src: String) {
    val freqs = defaultedMapOf<Char, MutableList<Pair<Int, Int>>> { mutableListOf() }
    var maxX = 0
    var maxY = 0
    for ((y, ln) in src.split('\n').withIndex()) {
        maxY = y
        maxX = ln.length - 1
        for ((x, c) in ln.withIndex()) {
            if (c != '.') {
                freqs[c].add(x to y)
            }
        }
    }
    var antinodes = mutableSetOf<Pair<Int, Int>>()
    for ((chr, nodes) in freqs) {
        nodes.permutations(2).forEach {
            val diff = it[0] - it[1]
            antinodes.add(it[0] + diff)
            antinodes.add(it[1] - diff)
        }
    }
    antinodes = antinodes.filter {
        val (x, y) = it
        x in 0 .. maxX && y in 0..maxY
    }.toMutableSet()
//    for (y in 0 .. maxY) {
//        outer@for (x in 0 .. maxX) {
//            if (x to y in antinodes) {
//                print("#")
//            } else {
//                for ((char, node) in freqs) {
//                    if (x to y in node) {
//                        print(char)
//                        continue@outer
//                    }
//                }
//                print(".")
//            }
//        }
//        println()
//    }
    println(antinodes.size)
}

// WHY IS THIS NOT STDLIB, I want my python functions
fun gcd(a: Int, b: Int): Int {
    var num1 = a
    var num2 = b
    while (num2 != 0) {
        val temp = num2
        num2 = num1 % num2
        num1 = temp
    }
    return num1
}

fun part2(src: String) {
    val freqs = defaultedMapOf<Char, MutableList<Pair<Int, Int>>> { mutableListOf() }
    var maxX = 0
    var maxY = 0
    for ((y, ln) in src.split('\n').withIndex()) {
        maxY = y
        maxX = ln.length - 1
        for ((x, c) in ln.withIndex()) {
            if (c != '.') {
                freqs[c].add(x to y)
            }
        }
    }
    var antinodes = mutableSetOf<Pair<Int, Int>>()
    for ((chr, nodes) in freqs) {
        nodes.permutations(2).forEach {
            var diff = it[0] - it[1]
            val gcd = gcd(diff.first, diff.second)
            diff /= gcd
            var pos = it[0]
            while (pos.first >= 0 && pos.second >= 0 && pos.first <= maxX && pos.second <= maxY) {
                antinodes.add(pos)
                pos += diff
            }
            pos = it[0]
            while (pos.first >= 0 && pos.second >= 0 && pos.first <= maxX && pos.second <= maxY) {
                antinodes.add(pos)
                pos -= diff
            }
        }
    }
//    for (y in 0 .. maxY) {
//        outer@for (x in 0 .. maxX) {
//            if (x to y in antinodes) {
//                print("#")
//            } else {
//                for ((char, node) in freqs) {
//                    if (x to y in node) {
//                        print(char)
//                        continue@outer
//                    }
//                }
//                print(".")
//            }
//        }
//        println()
//    }
    println(antinodes.size)
}