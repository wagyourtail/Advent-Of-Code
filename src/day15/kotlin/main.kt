import xyz.wagyourtail.commonskt.position.Pos2
import xyz.wagyourtail.commonskt.position.max
import xyz.wagyourtail.commonskt.position.min

val obj = object {}

fun main() {
    part1(obj.javaClass.getResource("input1.txt").readText().trim())
    part2(obj.javaClass.getResource("input1.txt").readText().trim())
}

fun debugPrintRoom(robot: Pos2, walls: Set<Pos2>, boxes: Set<Pos2>) {
    val min = walls.min()
    val max = walls.max()
    for (y in min.y .. max.y) {
        for (x in min.x .. max.x) {
            when (Pos2(x, y)) {
                in walls -> print("#")
                in boxes -> print("O")
                robot -> print("@")
                else -> print(".")
            }
        }
        println()
    }
}

fun part1(src: String) {
    val (werehouse, moves) = src.split("\n\n")
    val walls = mutableSetOf<Pos2>()
    val boxes = mutableSetOf<Pos2>()
    var robot: Pos2? = null
    for ((y, line) in werehouse.lines().withIndex()) {
        for ((x, c) in line.withIndex()) {
            when (c) {
                '#' -> walls.add(Pos2(x, y))
                'O' -> boxes.add(Pos2(x, y))
                '@' -> robot = Pos2(x, y)
                else -> {}
            }
        }
    }
    for (move in moves) {
        if (robot == null) error("No robot found")
//        debugPrintRoom(robot, walls, boxes)
        val moveOp: Pos2.() -> Pos2 = when (move) {
            '<' -> Pos2::left
            '>' -> Pos2::right
            '^' -> Pos2::up
            'v' -> Pos2::down
            '\n' -> continue
            else -> error("Unexpected character: $move")
        }
//        println("\nMove: $move")
        var next = robot.moveOp()
        if (next in walls) continue
        val toMove = mutableListOf<Pos2>()
        while (next in boxes) {
            toMove.add(next)
            next = next.moveOp()
        }
        if (next in walls) continue
        robot = robot.moveOp()
        for (pos2 in toMove.reversed()) {
            boxes.remove(pos2)
            boxes.add(pos2.moveOp())
        }
    }
//    debugPrintRoom(robot!!, walls, boxes)
    println(boxes.sumOf { it.x + 100 * it.y })
}

fun debugPrintRoomP2(robot: Pos2, walls: Set<Pos2>, boxes: Set<Set<Pos2>>) {
    val min = walls.min()
    val max = walls.max()
    for (y in min.y .. max.y) {
        for (x in min.x .. max.x) {
            val p = Pos2(x, y)
            when (p) {
                in walls -> print("#")
                robot -> print("@")
                else -> {
                    val b = boxes.firstOrNull { p in it }
                    if (b == null) {
                        print(".")
                        continue
                    }
                    if (p == b.first()) {
                        print("[")
                    } else {
                        print("]")
                    }
                }
            }
        }
        println()
    }
}

fun part2(src: String) {
    var (werehouse, moves) = src.split("\n\n")

    werehouse = werehouse
        .replace("#", "##")
        .replace("O", "[]")
        .replace(".", "..")
        .replace("@", "@.")

    val walls = mutableSetOf<Pos2>()
    val boxes = mutableSetOf<MutableSet<Pos2>>()
    var robot: Pos2? = null
    for ((y, line) in werehouse.lines().withIndex()) {
        for ((x, c) in line.withIndex()) {
            when (c) {
                '#' -> walls.add(Pos2(x, y))
                '[' -> boxes.add(mutableSetOf(Pos2(x, y)))
                ']' -> boxes.last().add(Pos2(x, y))
                '@' -> robot = Pos2(x, y)
                else -> {}
            }
        }
    }
    outer@for (move in moves) {
        if (robot == null) error("No robot found")
//        debugPrintRoomP2(robot, walls, boxes)
        val moveOp: Pos2.() -> Pos2 = when (move) {
            '<' -> Pos2::left
            '>' -> Pos2::right
            '^' -> Pos2::up
            'v' -> Pos2::down
            '\n' -> continue
            else -> error("Unexpected character: $move")
        }
//        println("\nMove: $move")
        var next = setOf(robot.moveOp())
        if (next.any { it in walls }) continue
        val toMove = mutableSetOf<Set<Pos2>>()
        while (next.any { n ->  boxes.any { n in it } }) {
            val nextNext = mutableSetOf<Pos2>()
            for (pos in next) {
                if (pos in walls) continue@outer // hackfix, don't know why need this line, should be handled below...
                val p = boxes.firstOrNull { pos in it } ?: continue
                toMove += p
                nextNext.addAll(p.map { it.moveOp() } - next)
            }
            next = nextNext
        }
        if (next.any { it in walls }) continue
        robot = robot.moveOp()
        for (box in toMove.reversed()) {
            boxes.removeIf { it == box }
            boxes.add(box.map(moveOp).toMutableSet())
        }
    }
//    debugPrintRoomP2(robot!!, walls, boxes)
    println(boxes.map { it.first() }.sumOf { it.x + 100 * it.y })
}