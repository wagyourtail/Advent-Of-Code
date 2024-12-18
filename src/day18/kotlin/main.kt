import xyz.wagyourtail.commonskt.position.Pos2
import kotlin.math.min

val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}


fun djikstra(bytes: List<Pos2>, startPos: Pos2 = Pos2(0, 0), endPos: Pos2 = Pos2(70, 70)): Int {
    val unvisited = (startPos..endPos).associateWith { Int.MAX_VALUE }.toMutableMap()
    for (b in bytes) {
        unvisited.remove(b)
    }
    val visited = mutableMapOf<Pos2, Int>()
    unvisited[startPos] = 0
    while (endPos in unvisited) {
        val (current, score) = unvisited.minBy { it.value }
        visited[current] = score
        unvisited.remove(current)
        for (next in listOf(current.up, current.down, current.left, current.right)) {
            unvisited.computeIfPresent(next) { k, v -> min(v, score + 1) }
        }
    }
    return visited.getValue(endPos)
}

fun part1(src: String) {
    val bytes = src.split("\n").map { it.split(",").map { it.toInt() } }.map { Pos2(it[0], it[1]) }.subList(0, 1024)
    println(djikstra(bytes))
}

fun part2(src: String) {
    val bytes = src.split("\n").map { it.split(",").map { it.toInt() } }.map { Pos2(it[0], it[1]) }
    val index = bytes.indices.toList().binarySearch { if (djikstra(bytes.subList(0, it)) < 0) 1 else -1 }
//    for (i in -index - 4 .. -index + 2) {
//        val d = djikstra(bytes.subList(0, i))
//        println("${bytes[i - 1]}: $d")
//    }
    println(bytes[-index - 2])
}