import xyz.wagyourtail.commonskt.collection.DefaultMap
import xyz.wagyourtail.commonskt.collection.defaultedMapOf

val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

fun part1(src: String) {
    val (t, p) = src.split("\n\n")
    val towels = t.split(",").map { it.trim() }
    val patterns = p.split("\n")


    lateinit var towelDFS: DefaultMap<String, Boolean>
    towelDFS = defaultedMapOf { rem ->
        if (rem.isEmpty()) return@defaultedMapOf true
        for (towel in towels) {
            if (rem.startsWith(towel)) {
                if (towelDFS[rem.substring(towel.length)]) {
                    return@defaultedMapOf true
                }
            }
        }
        return@defaultedMapOf false
    }

    var c = 0
    for (pattern in patterns) {
        if (towelDFS[pattern]) {
            c += 1
        }
    }
    println(c)
}

fun part2(src: String) {

    val (t, p) = src.split("\n\n")
    val towels = t.split(",").map { it.trim() }
    val patterns = p.split("\n")


    lateinit var towelDFS: DefaultMap<String, Long>
    towelDFS = defaultedMapOf { rem ->
        if (rem.isEmpty()) return@defaultedMapOf 1L
        var c = 0L
        for (towel in towels) {
            if (rem.startsWith(towel)) {
                c += towelDFS[rem.substring(towel.length)]
            }
        }
        c
    }

    var c = 0L
    for (pattern in patterns) {
       c += towelDFS[pattern]
    }
    println(c)
}