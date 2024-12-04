val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

val XMAS = setOf("XMAS", "XMAS".reversed())

fun part1(src: String) {
    val search = src.lines().map { it.toCharArray() }.toTypedArray()
    val board = mutableMapOf<Pair<Int, Int>, Char>()
    for ((x, line) in search.withIndex()) {
        for ((y, char) in line.withIndex()) {
            board[x to y] = char
        }
    }
    var c = 0
    for ((pos, entry) in board) {
        if (entry == 'X') {
            val up = buildString {
                for (i in 0..3) {
                    append(board[pos.first - i to pos.second])
                }
            }
            if (up in XMAS) c++
            val down = buildString {
                for (i in 0..3) {
                    append(board[pos.first + i to pos.second])
                }
            }
            if (down in XMAS) c++
            val left = buildString {
                for (i in 0..3) {
                    append(board[pos.first to pos.second - i])
                }
            }
            if (left in XMAS) c++
            val right = buildString {
                for (i in 0..3) {
                    append(board[pos.first to pos.second + i])
                }
            }
            if (right in XMAS) c++
            val upLeft = buildString {
                for (i in 0..3) {
                    append(board[pos.first - i to pos.second - i])
                }
            }
            if (upLeft in XMAS) c++
            val upRight = buildString {
                for (i in 0..3) {
                    append(board[pos.first - i to pos.second + i])
                }
            }
            if (upRight in XMAS) c++
            val downLeft = buildString {
                for (i in 0..3) {
                    append(board[pos.first + i to pos.second - i])
                }
            }
            if (downLeft in XMAS) c++
            val downRight = buildString {
                for (i in 0..3) {
                    append(board[pos.first + i to pos.second + i])
                }
            }
            if (downRight in XMAS) c++
        }
    }
    println(c)
}

val MS = setOf('M', 'S')

fun part2(src: String) {
    val search = src.lines().map { it.toCharArray() }.toTypedArray()
    val board = mutableMapOf<Pair<Int, Int>, Char>()
    for ((x, line) in search.withIndex()) {
        for ((y, char) in line.withIndex()) {
            board[x to y] = char
        }
    }
    var c = 0
    for ((pos, entry) in board) {
        if (entry == 'A') {
            val upLeft = pos.first - 1 to pos.second - 1
            val upRight = pos.first - 1 to pos.second + 1
            val downLeft = pos.first + 1 to pos.second - 1
            val downRight = pos.first + 1 to pos.second + 1
            if (setOf(board[upLeft], board[downRight]) == MS && setOf(board[upRight], board[downLeft]) == MS) {
                c += 1
            }
        }
    }
    println(c)
}