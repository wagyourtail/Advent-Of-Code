import xyz.wagyourtail.commonskt.position.Pos2
import xyz.wagyourtail.commonskt.position.max
import xyz.wagyourtail.commonskt.position.min

val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

val up = Pos2(0, -1)
val down = Pos2(0, 1)
val left = Pos2(-1, 0)
val right = Pos2(1, 0)

fun resolveRegion(plants: MutableMap<Pos2, Char>, pos: Pos2, char: Char, region: MutableSet<Pos2> = mutableSetOf()): Set<Pos2> {
    region.add(pos)
    for (next in listOf(up, down, left, right)) {
        if (plants[pos + next] == char) {
            plants.remove(pos + next)
            resolveRegion(plants, pos + next, char, region)
        }
    }
    return region
}

fun perimeter(region: Set<Pos2>): Long {
    var p = 0
    for (pos in region) {
        for (next in listOf(up, down, left, right)) {
            if (pos + next !in region) p += 1
        }
    }
    return p.toLong() * region.size
}

fun part1(src: String) {
    val plants = mutableMapOf<Pos2, Char>()
    for ((y, line) in src.lines().withIndex()) {
        for ((x, c) in line.withIndex()) {
            plants[Pos2(x, y)] = c
        }
    }
    val regions = mutableListOf<Set<Pos2>>()
    while (plants.isNotEmpty()) {
        val entry = plants.entries.first()
        plants.remove(entry.key)
        regions.add(resolveRegion(plants, entry.key, entry.value))
    }
    println(regions.sumOf { perimeter(it) })
}

fun traverseSide(region: Set<Pos2>, pos: Pos2, next: Pos2): Set<Pos2> {
    val trav = if (next.y == 0) {
        setOf(
            up,
            down
        )
    } else {
        setOf(
            left,
            right
        )
    }
    val visited = mutableSetOf(pos)
    for (t in trav) {
        var p = pos
        while (p in region && p + next !in region) {
            visited.add(p)
            p += t
        }
    }
    return visited
}

fun sides(region: Set<Pos2>): Long {
    var s = 0
    val visitedSides = mutableSetOf<Pair<Pos2, Pos2>>()
//    val positions = mutableMapOf<Pos2, Int>()
    for (pos in region) {
        var c = 0
        for (next in listOf(up, down, left, right)) {
            if (pos to next in visitedSides) continue
            if (pos + next !in region) {
                visitedSides.addAll(traverseSide(region, pos, next).map { it to next })
                s += 1
//                c += 1
            }
        }
//        positions[pos] = c
    }
//    val minPos = region.reduce { acc, pos2 -> min(acc, pos2) } - Pos2(1, 1)
//    val maxPos = region.reduce { acc, pos2 -> max(acc, pos2) } + Pos2(1, 1)
//    for (y in minPos.y .. maxPos.y) {
//        for (x in minPos.x .. maxPos.x) {
//            val p = Pos2(x, y)
//            if (p in region) {
//                print(positions[p] ?: 0)
//            } else {
//                print(".")
//            }
//        }
//        println()
//    }
//    println("$s, ${region.size}")
    return s.toLong() * region.size
}

fun part2(src: String) {
    val plants = mutableMapOf<Pos2, Char>()
    for ((y, line) in src.lines().withIndex()) {
        for ((x, c) in line.withIndex()) {
            plants[Pos2(x, y)] = c
        }
    }
    val regions = mutableListOf<Set<Pos2>>()
    while (plants.isNotEmpty()) {
        val entry = plants.entries.first()
        plants.remove(entry.key)
        regions.add(resolveRegion(plants, entry.key, entry.value))
    }
    println(regions.sumOf { sides(it) })
}