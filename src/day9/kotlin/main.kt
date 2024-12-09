
val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

fun <T> Iterable<T>.repeat(n: Int): List<T> {
    return buildList {
        for (i in 0 until n) {
            addAll(this@repeat)
        }
    }
}

fun part1(src: String) {
    val seq = src.toCharArray().asSequence().map {
        it.toString().toInt()
    }.withIndex().flatMap { (i, c) -> if (i % 2 == 0) listOf(i / 2).repeat(c) else listOf(null).repeat(c) }.toMutableList()
    while (null in seq) {
        val last = seq.removeLast() ?: continue
        seq[seq.indexOf(null)] = last
    }
    println(seq.withIndex().sumOf { (it.index * it.value!!).toLong() })
}

fun part2(src: String) {
    val seq = src.toCharArray().asSequence().map {
        it.toString().toInt()
    }.withIndex().map { (i, c) -> if (i % 2 == 0) (i / 2) to c else null to c }.toMutableList()
    val remain = mutableListOf<Pair<Int?, Int>>()
    outer@while (seq.isNotEmpty()) {
        val last = seq.removeLast()
        val (id, size) = last
        if (id == null) {
            remain.addFirst(null to size)
            continue
        }
        for ((i, c) in seq.withIndex()) {
            if (c.first == null && c.second >= size) {
                seq.removeAt(i)
                if (c.second > size) {
                    seq.add(i, null to c.second - size)
                }
                seq.add(i, id to size)

                val newLast = seq.last()
                if (newLast.first == null) {
                    seq.removeLast()
                    seq.add(null to newLast.second + size)
                } else {
                    seq.addLast(null to size)
                }

                continue@outer
            }
        }
        remain.addFirst(last)
    }
    println(remain.flatMap { listOf(it.first).repeat(it.second) }.withIndex().sumOf { (it.index * (it.value ?: 0)).toLong() })
};