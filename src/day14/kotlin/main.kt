import xyz.wagyourtail.commonskt.collection.defaultedMapOf
import xyz.wagyourtail.commonskt.position.Pos2
import xyz.wagyourtail.commonskt.utils.mutliAssociate
import xyz.wagyourtail.commonskt.utils.putMulti

val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

fun debugPrintRobots(robots: Map<Pos2, List<Pos2>>, size: Pos2): String = buildString {
    for (y in 0 ..< size.y) {
        for (x in 0  ..< size.x) {
            val p = Pos2(x, y)
            append(robots[p]?.size ?: ".")
        }
        append("\n")
    }
}

operator fun Pos2.rem(p: Pos2): Pos2 {
    val n = Pos2(x % p.x, y % p.y)
    return Pos2(if (n.x < 0) n.x + p.x else n.x, if (n.y < 0) n.y + p.y else n.y)
}

fun part1(src: String) {
    var robots = src.split("\n").map { Regex("-?\\d+").findAll(it).map { it.value.toInt() }.toList() }.withIndex().mutliAssociate { (i, it) -> Pos2(it[0], it[1]) to Pos2(it[2], it[3]) }.mapValues { it.value.toList() }
//    val size = Pos2(11, 7) // (101, 103)
    val size = Pos2(101, 103)
    val newRobots = mutableMapOf<Pos2, MutableList<Pos2>>()
    for (i in 0 ..< 100) {
        for ((pos, data) in robots) {
            for (robot in data) {
                newRobots.putMulti((pos + robot) % size, robot)
            }
        }
        robots = newRobots.toMap()
        newRobots.clear()
    }
    val halfY = size.y / 2
    val halfX = size.x / 2
    val quadrants = defaultedMapOf<Pair<Boolean, Boolean>, Int> { 0 }
    for (y in 0 ..< size.y) {
        for (x in 0 ..< size.x) {
            val c = robots[Pos2(x, y)]?.size ?: continue
            if (y < halfY) {
                if (x < halfX) {
                    quadrants[false to false] += c
                }
                if (x > halfX) {
                    quadrants[true to false] += c
                }
            }
            if (y > halfY) {
                if (x < halfX) {
                    quadrants[false to true] += c
                }
                if (x > halfX) {
                    quadrants[true to true] += c
                }
            }
        }
    }
//    debugPrintRobots(robots, size)
    println(quadrants.values.reduce { acc, i -> acc * i })
}

fun part2(src: String) {
    var robots = src.split("\n").map { Regex("-?\\d+").findAll(it).map { it.value.toInt() }.toList() }.withIndex().mutliAssociate { (i, it) -> Pos2(it[0], it[1]) to Pos2(it[2], it[3]) }.mapValues { it.value.toList() }
//    val size = Pos2(11, 7) // (101, 103)
    val size = Pos2(101, 103)
    val newRobots = mutableMapOf<Pos2, MutableList<Pos2>>()
    for (i in 0 ..< 10000) {
        for ((pos, data) in robots) {
            for (robot in data) {
                newRobots.putMulti((pos + robot) % size, robot)
            }
        }
        robots = newRobots.toMap()
        newRobots.clear()
        val s = debugPrintRobots(robots, size)
        if (s.contains("1111111111111") || i == 97) {
            println(s)
            println()
            println(i + 1)
            println()
        }
    }

}