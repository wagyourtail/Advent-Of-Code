import xyz.wagyourtail.commonskt.collection.DefaultMap
import xyz.wagyourtail.commonskt.collection.defaultedMapOf
import xyz.wagyourtail.commonskt.position.Pos2
import xyz.wagyourtail.commonskt.position.max
import kotlin.math.min

val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

fun part1(src: String) {
    val walkable = mutableSetOf<Pos2>()
    lateinit var startPos: Pos2
    lateinit var endPos: Pos2
    var maxPos = Pos2(0, 0)
    for ((y, line) in src.lines().withIndex()) {
        for ((x, c) in line.withIndex()) {
            maxPos = max(maxPos, Pos2(x, y))
            if (c == '#') continue
            walkable.add(Pos2(x, y))
            if (c == 'S') startPos = Pos2(x, y)
            if (c == 'E') endPos = Pos2(x, y)
        }
    }

    val distanceFromStart = mutableMapOf<Pos2, Int>()

    run {
        val unvisited = (Pos2(0, 0)..maxPos).associateWith { Int.MAX_VALUE }.toMutableMap()
        unvisited[startPos] = 0
        while (unvisited.isNotEmpty()) {
            val (current, score) = unvisited.minBy { it.value }
            distanceFromStart[current] = score
            unvisited.remove(current)
            if (score == Int.MAX_VALUE) continue
            for (next in listOf(current.up, current.down, current.left, current.right)) {
                if (next in walkable) {
                    unvisited.computeIfPresent(next) { _, v -> min(v, score + 1) }
                }
            }
        }
    }

    val distanceFromEnd = mutableMapOf<Pos2, Int>()

    run {
        val unvisited = (Pos2(0, 0)..maxPos).associateWith { Int.MAX_VALUE }.toMutableMap()
        unvisited[endPos] = 0
        while (unvisited.isNotEmpty()) {
            val (current, score) = unvisited.minBy { it.value }
            distanceFromEnd[current] = score
            unvisited.remove(current)
            for (next in listOf(current.up, current.down, current.left, current.right)) {
                if (next in walkable) {
                    unvisited.computeIfPresent(next) { _, v -> min(v, score + 1) }
                }
            }
        }
    }

    // find normal path by using distance from start from end
    val normalPath = mutableSetOf<Pos2>()
    run {
        var c = endPos
        while (c != startPos) {
            normalPath.add(c)
            c = listOf(c.up, c.down, c.left, c.right).minBy { distanceFromStart.getValue(it) }
        }
        normalPath.add(startPos)
    }

//    for (y in 0..maxPos.y) {
//        for (x in 0..maxPos.x) {
//            val p = Pos2(x, y)
//            print(if (p in normalPath) "O" else if (p in walkable) "." else "#")
//        }
//        println()
//    }

    val cheatList = defaultedMapOf<Int, MutableSet<Pair<Pos2, Pos2>>> { mutableSetOf() }

    for (x in normalPath) {
        val currentScore = distanceFromEnd.getValue(x)
        // step 3 tree
        for (a in listOf(x.up, x.down, x.left, x.right)) {
            for (b in listOf(a.up, a.down, a.left, a.right)) {
                if (b in walkable) {
                    val cScore = distanceFromEnd.getValue(b)
                    if (currentScore - cScore > 3) {
//                        println("$x -> $b: ${currentScore - cScore - 2}")
                        cheatList[currentScore - cScore - 2].add(x to b)
                    }
                }
            }
        }
    }

    var c = 0
    for (score in cheatList.keys.sorted()) {
        if (score < 100) continue
        c += cheatList[score].size
//        println("$score: ${cheatList[score].size}")
    }
    println(c)
}

fun part2(src: String) {

    val walkable = mutableSetOf<Pos2>()
    lateinit var startPos: Pos2
    lateinit var endPos: Pos2
    var maxPos = Pos2(0, 0)
    for ((y, line) in src.lines().withIndex()) {
        for ((x, c) in line.withIndex()) {
            maxPos = max(maxPos, Pos2(x, y))
            if (c == '#') continue
            walkable.add(Pos2(x, y))
            if (c == 'S') startPos = Pos2(x, y)
            if (c == 'E') endPos = Pos2(x, y)
        }
    }

    val distanceFromStart = mutableMapOf<Pos2, Int>()

    run {
        val unvisited = (Pos2(0, 0)..maxPos).associateWith { Int.MAX_VALUE }.toMutableMap()
        unvisited[startPos] = 0
        while (unvisited.isNotEmpty()) {
            val (current, score) = unvisited.minBy { it.value }
            distanceFromStart[current] = score
            unvisited.remove(current)
            if (score == Int.MAX_VALUE) continue
            for (next in listOf(current.up, current.down, current.left, current.right)) {
                if (next in walkable) {
                    unvisited.computeIfPresent(next) { _, v -> min(v, score + 1) }
                }
            }
        }
    }

    val distanceFromEnd = mutableMapOf<Pos2, Int>()

    run {
        val unvisited = (Pos2(0, 0)..maxPos).associateWith { Int.MAX_VALUE }.toMutableMap()
        unvisited[endPos] = 0
        while (unvisited.isNotEmpty()) {
            val (current, score) = unvisited.minBy { it.value }
            distanceFromEnd[current] = score
            unvisited.remove(current)
            for (next in listOf(current.up, current.down, current.left, current.right)) {
                if (next in walkable) {
                    unvisited.computeIfPresent(next) { _, v -> min(v, score + 1) }
                }
            }
        }
    }

    // find normal path by using distance from start from end
    val normalPath = mutableSetOf<Pos2>()
    run {
        var c = endPos
        while (c != startPos) {
            normalPath.add(c)
            c = listOf(c.up, c.down, c.left, c.right).minBy { distanceFromStart.getValue(it) }
        }
        normalPath.add(startPos)
    }

    // print
//    for (y in 0..maxPos.y) {
//        for (x in 0..maxPos.x) {
//            val p = Pos2(x, y)
//            print(if (p in normalPath) "O" else if (p in walkable) "." else "#")
//        }
//        println()
//    }

    val cheatList = defaultedMapOf<Int, MutableSet<Pair<Pos2, Pos2>>> { mutableSetOf() }

    for (x in normalPath) {
        val currentScore = distanceFromEnd.getValue(x)
        val endpoints = mutableMapOf<Pos2, Int>()
        endpoints[x] = 0
        var currentPositions = setOf(x)
        for (depth in 0 .. 20) {
            val nextPositions = mutableSetOf<Pos2>()
            for (y in currentPositions) {
                endpoints.putIfAbsent(y, depth)
                nextPositions.addAll(arrayOf(y.up, y.down, y.left, y.right))
            }
            currentPositions = nextPositions
        }
        for ((b, depth) in endpoints) {
            if (b !in walkable) continue
            val saveScore = (currentScore - distanceFromEnd.getValue(b)) - depth
            if (saveScore < 50) continue
            cheatList[saveScore].add(x to b)
        }
    }

    var c = 0
    for (score in cheatList.keys.sorted()) {
        if (score < 100) continue
        c += cheatList[score].size
//        println("$score: ${cheatList[score].size}")
    }
    println(c)

}