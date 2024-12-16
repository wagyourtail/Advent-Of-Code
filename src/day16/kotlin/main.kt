import xyz.wagyourtail.commonskt.position.Pos2
import xyz.wagyourtail.commonskt.position.max
import kotlin.math.min

val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

enum class Direction(val step: Pos2.() -> Pos2, val unstep: Pos2.() -> Pos2) {
    NORTH(Pos2::up, Pos2::down),
    WEST(Pos2::left, Pos2::right),
    SOUTH(Pos2::down, Pos2::up),
    EAST(Pos2::right, Pos2::left);
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
    val unvisitedNodes = walkable.flatMap { p -> Direction.entries.map { p to it } }.associateWith { Int.MAX_VALUE }.toMutableMap()
    val visitedNodes = mutableMapOf<Pair<Pos2, Direction>, Int>()
    unvisitedNodes[startPos to Direction.EAST] = 0
    while (unvisitedNodes.isNotEmpty() && unvisitedNodes.keys.any { endPos == it.first }) {
        val node = unvisitedNodes.minBy { it.value }
        val (pos, currentDir) = node.key
        visitedNodes[node.key] = node.value
        unvisitedNodes.remove(node.key)
        for (i in -1..1) {
            val dir = Direction.entries[(currentDir.ordinal + i).mod(4)]
            val next = dir.step(pos)
            if ((next to dir) !in unvisitedNodes) continue
            val cost = node.value + 1 + if (i != 0) 1000 else 0
            if (unvisitedNodes.getValue(next to dir) > cost) {
                unvisitedNodes[next to dir] = cost
            }
        }
    }
    println(visitedNodes.entries.filter { it.key.first == endPos }.minOfOrNull { it.value })
//    val visitedCosts = mutableMapOf<Pos2, Int>()
//    for ((node, cost) in visitedNodes) {
//        visitedCosts[node.first] = min(visitedCosts[node.first] ?: Int.MAX_VALUE, cost)
//    }
//    for (y in 0 .. maxPos.y) {
//        for (x in 0 .. maxPos.x) {
//            val pos = Pos2(x, y)
//            if (pos in walkable) {
//                if (pos in visitedCosts) {
//                    print("|")
//                    print(visitedCosts[pos].toString().padStart(5, '0'))
//                    print("|")
//                } else {
//                    print("|.....|")
//                }
//            } else {
//                print("|#####|")
//            }
//        }
//        println("")
//        println("")
//    }
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
    val unvisitedNodes = walkable.flatMap { p -> Direction.entries.map { p to it } }.associateWith { Int.MAX_VALUE }.toMutableMap()
    val visitedNodes = mutableMapOf<Pair<Pos2, Direction>, Int>()
    unvisitedNodes[startPos to Direction.EAST] = 0
    while (unvisitedNodes.isNotEmpty() && unvisitedNodes.keys.any { endPos == it.first }) {
        val node = unvisitedNodes.minBy { it.value }
        val (pos, currentDir) = node.key
        visitedNodes[node.key] = node.value
        unvisitedNodes.remove(node.key)
        for (i in -1..1) {
            val dir = Direction.entries[(currentDir.ordinal + i).mod(4)]
            val next = if (i == 0) dir.step(pos) else pos
            if ((next to dir) !in unvisitedNodes) continue
            val cost = node.value + if (i != 0) 1000 else 1
            if (unvisitedNodes.getValue(next to dir) > cost) {
                unvisitedNodes[next to dir] = cost
            }
        }
    }
    val min = visitedNodes.entries.filter { it.key.first == endPos }.minOfOrNull { it.value }
    val reVisited = mutableSetOf<Pos2>()
    for (dir in Direction.entries) {
        if (visitedNodes[endPos to dir] == min) {
            val toVisit = mutableListOf<Pair<Pos2, Direction>>()
            toVisit.add(endPos to dir)
            while (toVisit.isNotEmpty()) {
                val node = toVisit.removeFirst()
                reVisited.add(node.first)
                val score = visitedNodes[node]!!
                for (i in -1..1) {
                    val dir = Direction.entries[(node.second.ordinal + i).mod(4)]
                    val next = if (i != 0) node.first else node.second.unstep(node.first)
                    val nextScore = score - (if (i != 0) 1000 else 1)
                    if (visitedNodes[next to dir] == nextScore) {
                        toVisit.add(next to dir)
                    }
                }
            }
        }
    }
    println(reVisited.size)

}