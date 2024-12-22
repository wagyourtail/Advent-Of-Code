val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

fun nextSecret(input: Int): Int {
    var input = ((input shl 6) xor input).mod(0x1000000)
    input = ((input shr 5) xor input).mod(0x1000000)
    input = ((input shl 11) xor input).mod(0x1000000)
    return input
}

fun part1(src: String) {
    var c = 0L
    for (s in src.split("\n")) {
        var m = s.toInt()
        for (i in 0 ..< 2000) {
            m = nextSecret(m)
        }
        c += m
    }
    println(c)
}

fun part2(src: String) {
    val cc = mutableListOf<List<Int>>()
    for (s in src.split("\n")) {
        var m = s.toInt()
        val c = mutableListOf(m % 10)
        for (i in 0 ..< 2000) {
            m = nextSecret(m)
            c.add(m % 10)
        }
        cc.add(c)
    }
    val ccc = cc.map { c ->

        c.indices.asSequence().drop(5).map {
            val sl = c.subList(it - 5, it)
            sl.zipWithNext { a, b -> b - a } to sl.last()
        }.toList().reversed().toMap()
    }
    val keys = ccc.flatMap { it.keys }.toSet()
    println(keys.maxOf { key -> ccc.sumOf { it[key] ?: 0 } })
}
