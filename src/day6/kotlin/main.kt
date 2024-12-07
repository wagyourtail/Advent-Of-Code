import kotlin.math.max

val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

val steps = listOf(
    (0 to -1),
    (1 to 0),
    (0 to 1),
    (-1 to 0)
)

operator fun Pair<Int, Int>.plus(p: Pair<Int, Int>): Pair<Int, Int> {
    return this.first + p.first to this.second + p.second
}

fun part1(src: String) {
    val obstacles = mutableMapOf<Pair<Int, Int>, Boolean>()
    lateinit var guardPos: Pair<Int, Int>
    for ((y, ln) in src.split('\n').withIndex()) {
        for ((x, c) in ln.withIndex()) {
            if (c == '^') {
                guardPos = Pair(x, y)
            }
            obstacles[x to y] = c == '#'
        }
    }
    var visited = mutableSetOf<Pair<Int, Int>>()
    var direction = 0
    while (guardPos in obstacles) {
        visited.add(guardPos)
        while (obstacles[guardPos + steps[direction]] == true) {
            direction++
            direction %= 4
        }
        guardPos += steps[direction]
    }
    println(visited.size)
}

fun willLoop(obstacles: Map<Pair<Int, Int>, Boolean>, guardPos: Pair<Int, Int>): Boolean {
    var guardPos = guardPos
    var visited = mutableSetOf<Triple<Int, Int, Int>>()
    var direction = 0
    while (guardPos in obstacles) {
        while (obstacles[guardPos + steps[direction]] == true) {
            direction++
            direction %= 4
        }
        val pos = Triple(guardPos.first, guardPos.second, direction)
        if (pos in visited) {
            return true
        }
        visited.add(pos)
        guardPos += steps[direction]
    }
    return false
}

fun part2(src: String) {
    val obstacles = mutableMapOf<Pair<Int, Int>, Boolean>()
    lateinit var guardPos: Pair<Int, Int>
    var maxX = 0
    var maxY = 0
    for ((y, ln) in src.split('\n').withIndex()) {
        maxY = y
        for ((x, c) in ln.withIndex()) {
            maxX = max(x, maxX)
            if (c == '^') {
                guardPos = Pair(x, y)
            }
            obstacles[x to y] = c == '#'
        }
    }
    var c = 0
    for (y in 0 .. maxY) {
        for (x in 0..maxX) {
            if (x to y == guardPos || obstacles[x to y]!!) continue
            if (willLoop(obstacles.toMutableMap().also {
                it[x to y] = true
            }, guardPos)) c++
        }
    }
    println(c)
}