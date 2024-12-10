import xyz.wagyourtail.commonskt.position.Pos2

val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}


val up = Pos2(0, -1)
val down = Pos2(0, 1)
val left = Pos2(-1, 0)
val right = Pos2(1, 0)
fun Pos2.str() = "($x, $y)"

fun findNext(current: Pos2, next: Int, grid: Map<Pos2, Int>): Set<Pos2> {
    val toCheck = listOf(
        current + up,
        current + down,
        current + left,
        current + right,
    )
    val c = mutableSetOf<Pos2>()
    for (i in toCheck) {
        if (grid[i] == next) {
            if (next == 9) {
                c.add(i)
            } else {
                c.addAll(findNext(i, next + 1, grid))
            }
        }
    }
    return c
}

fun findNextP2(current: Pos2, next: Int, grid: Map<Pos2, Int>): Int {
    val toCheck = listOf(
        current + up,
        current + down,
        current + left,
        current + right,
    )
    var c = 0
    for (i in toCheck) {
        if (grid[i] == next) {
            c += if (next == 9) {
                1
            } else {
                findNextP2(i, next + 1, grid)
            }
        }
    }
    return c
}

fun part1(src: String) {
    val positions = mutableMapOf<Pos2, Int>()
    val zeros = mutableSetOf<Pos2>()
    for ((y, chars) in src.lines().withIndex()) {
        for ((x, char) in chars.withIndex()) {
            positions[Pos2(x, y)] = char.toString().toInt()
            if (char == '0') {
                zeros.add(Pos2(x, y))
            }
        }
    }
    println(zeros.map { findNext(it, 1, positions).count() }.sum())
}

fun part2(src: String) {

    val positions = mutableMapOf<Pos2, Int>()
    val zeros = mutableSetOf<Pos2>()
    for ((y, chars) in src.lines().withIndex()) {
        for ((x, char) in chars.withIndex()) {
            positions[Pos2(x, y)] = char.toString().toInt()
            if (char == '0') {
                zeros.add(Pos2(x, y))
            }
        }
    }
    println(zeros.map { findNextP2(it, 1, positions) }.sum())
}