import xyz.wagyourtail.commonskt.collection.DefaultMap
import xyz.wagyourtail.commonskt.collection.defaultedMapOf

val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

val blink = defaultedMapOf<Long, List<Long>> {
    if (it == 0L) {
        return@defaultedMapOf listOf(1)
    }
    val inp = it.toString()
    if (inp.length % 2 == 0) {
        return@defaultedMapOf listOf(inp.substring(0, inp.length / 2).toLong(), inp.substring(inp.length / 2).toLong())
    }
    listOf(it * 2024)
}

val blinkP2 = run {
    lateinit var blinkP2: DefaultMap<Pair<Long, Int>, Long>

    blinkP2 = defaultedMapOf { (num, count) ->
        if (count == 0) return@defaultedMapOf 1L
        blink[num].sumOf { blinkP2[it to count - 1] }
    }

    blinkP2
}

fun part1(src: String) {
    var stones = src.split(" ").map { it.toLong() }
    for (i in 0 until 25) {
//        println(stones)
        stones = stones.flatMap { blink[it] }
    }
    println(stones.size)
}

fun part2(src: String) {
    val stones = src.split(" ").map { it.toLong() }
    println(stones.sumOf { blinkP2[it to 75] })
}
