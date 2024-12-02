
val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText())
    part2(obj.javaClass.getResource("input1.txt").readText())
}

fun part1(src: String) {
    val safe = src.lines().filter { line ->
        p1Check(line.split(" ").filter { it.isNotEmpty() }.map { it.toInt() }.zipWithNext())
    }
    println(safe.size)
}

fun p1Check(l: List<Pair<Int, Int>>): Boolean {
    return l.all { it.first < it.second && it.second - it.first <= 3 } || l.all { it.first > it.second && it.first - it.second <= 3 }
}

fun part2(src: String) {
    val safe = src.lines().filter { line ->
        val l = line.split(" ").filter { it.isNotEmpty() }.map { it.toInt() }
        if (p1Check(l.zipWithNext())) {
            return@filter true
        }
        for (i in l.indices) {
            val ml = l.toMutableList()
            ml.removeAt(i)
            if (p1Check(ml.zipWithNext())) {
                return@filter true
            }
        }
        return@filter false
    }
    println(safe.size)
}